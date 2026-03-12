import { useState, useRef, useCallback } from "react";
import { useNavigate } from "react-router-dom";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { toast } from "sonner";
import { UploadCloud, FileType2, ShieldCheck, FileSearch, ArrowRight } from "lucide-react";

export default function Upload() {
  const [file, setFile] = useState(null);
  const [isDragging, setIsDragging] = useState(false);
  const [loading, setLoading] = useState(false);
  const [progress, setProgress] = useState(0);
  const [results, setResults] = useState(null);
  const fileInputRef = useRef(null);
  const navigate = useNavigate();

  const handleDragOver = useCallback((e) => {
    e.preventDefault();
    setIsDragging(true);
  }, []);

  const handleDragLeave = useCallback((e) => {
    e.preventDefault();
    setIsDragging(false);
  }, []);

  const handleDrop = useCallback((e) => {
    e.preventDefault();
    setIsDragging(false);
    const droppedFile = e.dataTransfer.files[0];
    if (droppedFile) {
      setFile(droppedFile);
      setResults(null);
      toast.success("File selected successfully");
    }
  }, []);

  const handleFileSelect = (e) => {
    const selectedFile = e.target.files[0];
    if (selectedFile) {
      setFile(selectedFile);
      setResults(null);
      toast.success("File selected successfully");
    }
  };

  const simulateProgress = () => {
    setProgress(0);
    const interval = setInterval(() => {
      setProgress((prev) => {
        if (prev >= 95) {
          clearInterval(interval);
          return 95;
        }
        return prev + 5;
      });
    }, 150);
    return interval;
  };

  const handleUpload = async () => {
    if (!file) {
      toast.error("Please select a file first.");
      return;
    }

    const token = localStorage.getItem("token");
    if (!token) {
      toast.error("Session expired. Please log in again.");
      navigate("/login");
      return;
    }

    setLoading(true);
    setResults(null);
    const progInterval = simulateProgress();

    try {
      const formData = new FormData();
      formData.append("file", file);

      const res = await fetch("https://plagiarism-detector-api-16d8.onrender.com/compare", {
        method: "POST",
        headers: { Authorization: `Bearer ${token}` },
        body: formData,
      });

      clearInterval(progInterval);
      setProgress(100);

      if (res.status === 401) {
        toast.error("Unauthorized. Please log in again.");
        localStorage.removeItem("token");
        navigate("/login");
        return;
      }

      if (!res.ok) {
        const errData = await res.json();
        throw new Error(errData.detail || "Comparison failed");
      }

      const data = await res.json();
      setResults(data);
      toast.success("Analysis completed successfully!");
    } catch (err) {
      clearInterval(progInterval);
      toast.error(err.message || "Failed to connect to the analysis engine.");
    } finally {
      setTimeout(() => {
        setLoading(false);
        setProgress(0);
      }, 500);
    }
  };

  const detectedAlgorithm =
    (results?.algorithm_detected || "Not Detected").replace(/_/g, " ");

  return (
    <div className="p-6 md:p-8 max-w-4xl mx-auto space-y-8 animate-in fade-in duration-500">
      <div className="text-center mb-8">
        <h1 className="text-3xl font-bold text-white tracking-tight mb-2">
          Code Analysis
        </h1>
        <p className="text-slate-400 text-base">
          Upload your source code to detect algorithmic signatures and verify dataset integrity
        </p>
      </div>

      <Card className="glass-card border border-white/10 shadow-2xl overflow-hidden mb-8 bg-black/20">
        <div className="h-1 w-full bg-white/5">
          <div
            className="h-full bg-violet-500 transition-all duration-300"
            style={{ width: `${progress}%` }}
          />
        </div>

        <CardContent className="p-6 sm:p-10">
          <div
            onDragOver={handleDragOver}
            onDragLeave={handleDragLeave}
            onDrop={handleDrop}
            onClick={() => fileInputRef.current?.click()}
            className={`
              relative cursor-pointer rounded-2xl border-2 border-dashed transition-all duration-300 p-12
              flex flex-col items-center justify-center gap-4 text-center
              ${isDragging
                ? "border-violet-500 bg-violet-500/10 scale-[1.02]"
                : file
                  ? "border-emerald-500/40 bg-emerald-500/5 hover:bg-emerald-500/10"
                  : "border-white/15 hover:border-violet-500/40 hover:bg-white/[0.03]"
              }
            `}
          >
            <input
              ref={fileInputRef}
              type="file"
              accept=".py,.js,.java,.cpp,.c,.txt"
              onChange={handleFileSelect}
              className="hidden"
            />

            {file ? (
              <>
                <div className="w-16 h-16 rounded-2xl bg-emerald-500/20 flex items-center justify-center animate-bounce-slow">
                  <FileType2 className="w-8 h-8 text-emerald-400" />
                </div>
                <div>
                  <p className="text-white font-medium text-lg">{file.name}</p>
                  <p className="text-emerald-400/80 text-sm mt-1">
                    {(file.size / 1024).toFixed(1)} KB • Ready for scan
                  </p>
                </div>
              </>
            ) : (
              <>
                <div className="w-16 h-16 rounded-2xl bg-white/5 flex items-center justify-center">
                  <UploadCloud className="w-8 h-8 text-slate-400" />
                </div>
                <div>
                  <p className="text-slate-200 font-medium text-lg">
                    {isDragging ? "Drop code file here" : "Drag & drop code file here"}
                  </p>
                  <p className="text-slate-500 text-sm mt-1">
                    or click to browse local files (.py, .java, .cpp, .c)
                  </p>
                </div>
              </>
            )}
          </div>

          <Button
            onClick={handleUpload}
            disabled={!file || loading}
            className="w-full mt-8 h-14 rounded-xl bg-violet-600 hover:bg-violet-500 text-white font-medium text-lg transition-all shadow-lg shadow-violet-600/20 disabled:opacity-50"
          >
            {loading ? (
              <span className="flex items-center gap-2">
                <svg
                  className="animate-spin h-5 w-5 text-white"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                >
                  <circle
                    className="opacity-25"
                    cx="12"
                    cy="12"
                    r="10"
                    stroke="currentColor"
                    strokeWidth="4"
                  />
                  <path
                    className="opacity-75"
                    fill="currentColor"
                    d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z"
                  />
                </svg>
                Analyzing... {progress}%
              </span>
            ) : (
              <span className="flex items-center gap-2">
                <FileSearch className="w-5 h-5" /> Execute Security Scan
              </span>
            )}
          </Button>
        </CardContent>
      </Card>

      {results && !results.error && (
        <Card className="glass-card border border-emerald-500/30 shadow-xl overflow-hidden bg-emerald-950/20 animate-in slide-in-from-bottom-4 duration-500">
          <CardContent className="p-6">
            <div className="flex items-center justify-between flex-wrap gap-4">
              <div className="flex items-center gap-4">
                <div className="w-12 h-12 rounded-full bg-emerald-500/20 flex items-center justify-center shrink-0">
                  <ShieldCheck className="w-6 h-6 text-emerald-400" />
                </div>

                <div>
                  <h3 className="text-lg font-bold text-white">Scan Complete</h3>

                  <div className="flex items-center gap-2 mt-1">
                    <span className="text-sm text-slate-400">
                      Detected Signature:
                    </span>

                    <span className="px-2.5 py-0.5 rounded-md bg-emerald-500/10 border border-emerald-500/20 text-emerald-400 text-xs font-bold uppercase tracking-wider">
                      {detectedAlgorithm}
                    </span>
                  </div>
                </div>
              </div>

              <Button
                onClick={() => navigate("/history")}
                className="bg-white/10 hover:bg-white/20 text-white border border-white/10"
              >
                View in History Dashboard
                <ArrowRight className="w-4 h-4 ml-2" />
              </Button>
            </div>
          </CardContent>
        </Card>
      )}
    </div>
  );
}