from fastapi import FastAPI, UploadFile, File
from similarity import compare_code
from auth import router as auth_router
from dependencies import verify_token
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Depends, HTTPException
from database import users_collection, save_scan_result, scans_collection
from preprocess import get_code_stats
from bson import ObjectId
from datetime import datetime
import shutil
import os

app = FastAPI()

@app.on_event("startup")
async def preload_cache():
    from similarity import get_cache
    cache = get_cache()
    print(f"Dataset cache loaded: {len(cache.files)} files")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth_router)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "..", "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.get("/")
def home():
    return {"message": "Plagiarism Detector API Running"}


@app.post("/upload")
async def upload_file(file: UploadFile = File(...), user=Depends(verify_token)):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"message": f"{file.filename} uploaded successfully"}


@app.post("/compare")
async def compare(file: UploadFile = File(...), user=Depends(verify_token)):

    upload_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(upload_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    with open(upload_path, "r", encoding="utf-8", errors="replace") as f:
        uploaded_raw = f.read()

    results = compare_code(upload_path)

    # Safety defaults — never return null values
    if results.get("algorithm_detected") is None:
        results["algorithm_detected"] = "Unknown"
    if results.get("similarity") is None:
        results["similarity"] = {}
    if results.get("copied_lines") is None:
        results["copied_lines"] = {}
    if results.get("score_details") is None:
        results["score_details"] = {}
    
    # 1. Lookup user
    username = user.get("sub")
    db_user = users_collection.find_one({"username": username})
    if not db_user:
        raise HTTPException(status_code=401, detail="User not found")
        
    user_id = db_user["_id"]
    
    # 2. Extract stats
    line_count, char_count = get_code_stats(uploaded_raw)
    
    # 3. Detect language
    ext = os.path.splitext(file.filename)[1].lower()
    ext_map = {
        ".py": "python",
        ".c": "c",
        ".cpp": "cpp",
        ".java": "java"
    }
    language = ext_map.get(ext, "unknown")
    
    # 4. Save scan to db
    save_scan_result(
        user_id=user_id,
        filename=file.filename,
        language=language,
        line_count=line_count,
        char_count=char_count,
        algorithm_detected=results.get("algorithm_detected", "Unknown"),
        similarity=results.get("similarity", {}),
        copied_lines=results.get("copied_lines", {})
    )

    return results

@app.get("/history")
async def get_history(user=Depends(verify_token)):
    username = user.get("sub")
    db_user = users_collection.find_one({"username": username})
    if not db_user:
        raise HTTPException(status_code=401, detail="User not found")
        
    user_id = db_user["_id"]
    scans = scans_collection.find({"user_id": user_id}).sort("created_at", -1).limit(50)
    
    history_list = []
    for s in scans:
        sim = s.get("similarity", {})
        top_match = {}
        if sim:
            top_k = list(sim.keys())[0]
            top_match = {top_k: sim[top_k]}
            
        history_list.append({
            "id": str(s["_id"]),
            "filename": s.get("filename", "unknown"),
            "language": s.get("language", "unknown"),
            "algorithm_detected": s.get("algorithm_detected") or "Unknown",
            "line_count": s.get("line_count", 0),
            "char_count": s.get("char_count", 0),
            "similarity": sim if sim is not None else {},
            "copied_lines": s.get("copied_lines") or {},
            "created_at": s.get("created_at", datetime.utcnow()).isoformat()
        })
        
    return history_list

@app.get("/scan/{scan_id}")
async def get_scan_details(scan_id: str, user=Depends(verify_token)):
    if not ObjectId.is_valid(scan_id):
        raise HTTPException(status_code=400, detail="Invalid scan ID")
        
    scan = scans_collection.find_one({"_id": ObjectId(scan_id)})
    if not scan:
        raise HTTPException(status_code=404, detail="Scan not found")
        
    # verify ownership
    username = user.get("sub")
    db_user = users_collection.find_one({"username": username})
    if not db_user or db_user["_id"] != scan["user_id"]:
        raise HTTPException(status_code=401, detail="Unauthorized access to scan")
        
    # clean objectids
    scan["id"] = str(scan.pop("_id"))
    scan["user_id"] = str(scan["user_id"])
    if "created_at" in scan:
        scan["created_at"] = scan["created_at"].isoformat()
        
    return scan