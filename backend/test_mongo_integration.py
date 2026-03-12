import os
import sys
import json
from fastapi.testclient import TestClient
sys.path.append('a:/plagiarism/backend')
from main import app
from database import users_collection, scans_collection

client = TestClient(app)

def setup():
    users_collection.delete_many({})
    scans_collection.delete_many({})

def run_tests():
    print("Testing Signup...")
    res = client.post("/signup", json={"username": "testuser", "password": "password123"})
    assert res.status_code == 200, f"Signup failed: {res.text}"
    print("  Signup OK")
    
    # duplicate check
    res_dup = client.post("/signup", json={"username": "testuser", "password": "password123"})
    assert res_dup.status_code == 400
    print("  Duplicate checks OK")

    print("\nTesting Login...")
    res = client.post("/login", json={"username": "testuser", "password": "password123"})
    assert res.status_code == 200
    token = res.json().get("access_token")
    assert token, "No token returned"
    print("  Login OK")
    
    headers = {"Authorization": f"Bearer {token}"}
    
    print("\nTesting Upload & Scan...")
    code = "def bubble_sort(arr):\n    for i in range(len(arr)):\n        for j in range(len(arr)-i-1):\n            if arr[j] > arr[j+1]:\n                arr[j], arr[j+1] = arr[j+1], arr[j]\n    return arr"
    
    files = {"file": ("test_upload.py", code, "text/plain")}
    res = client.post("/compare", headers=headers, files=files)
    assert res.status_code == 200, f"Compare failed: {res.text}"
    print("  Compare returned OK")
    
    print("\nTesting History...")
    res = client.get("/history", headers=headers)
    assert res.status_code == 200
    history = res.json()
    assert len(history) == 1, f"Expected 1 scan, got {len(history)}"
    
    s = history[0]
    scan_id = s.get("scan_id")
    assert scan_id, "Missing scan_id"
    assert s.get("filename") == "test_upload.py"
    print(s)
    print("  History API OK")
    
    print("\nTesting Scan Details...")
    res = client.get(f"/scan/{scan_id}", headers=headers)
    assert res.status_code == 200
    details = res.json()
    assert details["_id"] == scan_id
    assert details["language"] == "python"
    assert details["line_count"] == 6
    assert "similarity" in details
    print("  Detail API OK")

if __name__ == "__main__":
    setup()
    run_tests()
    print("\nALL MONGO TESTS PASSED!")
