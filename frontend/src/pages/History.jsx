import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { FileCode2, Calendar, FileText, Cpu, Database } from "lucide-react";

export default function History() {
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    const fetchHistory = async () => {
      const token = localStorage.getItem("token");
      if (!token) {
        navigate("/login");
        return;
      }

      try {
        const res = await fetch("https://plagiarism-detector-api-16d8.onrender.com/history", {
          headers: { Authorization: `Bearer ${token}` }
        });

        if (res.status === 401) {
          localStorage.removeItem("token");
          navigate("/login");
          return;
        }

        if (!res.ok) throw new Error("Failed to fetch history");

        const data = await res.json();
        setHistory(Array.isArray(data) ? data : []);
      } catch (err) {
        setError(err.message || "An error occurred");
      } finally {
        setLoading(false);
      }
    };

    fetchHistory();
  }, [navigate]);

  return (
    <div className="p-6 md:p-8 max-w-7xl mx-auto space-y-8 animate-in fade-in duration-500">
      <div className="mb-4">
        <h1 className="text-3xl font-bold text-white tracking-tight">Scan History</h1>
        <p className="text-slate-400 mt-1">Review past plagiarism detection reports</p>
      </div>

      {error && (
        <div className="rounded-lg bg-red-500/10 border border-red-500/20 px-4 py-3 text-sm text-red-400">
          {error}
        </div>
      )}

      {loading ? (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {[1, 2, 3, 4, 5, 6].map(i => (
            <Card key={i} className="glass-card border border-white/5 animate-pulse">
              <CardContent className="p-6 h-40 bg-white/[0.02]"></CardContent>
            </Card>
          ))}
        </div>
      ) : history.length === 0 ? (
        <Card className="glass-card border border-white/10 py-16 text-center bg-white/[0.02]">
          <div className="flex justify-center mb-4">
            <div className="w-16 h-16 rounded-2xl bg-white/5 flex items-center justify-center">
              <FileText className="w-8 h-8 text-slate-500" />
            </div>
          </div>
          <h3 className="text-xl font-medium text-white mb-2">No history found</h3>
          <p className="text-slate-400 mb-6">You haven't scanned any files yet.</p>
          <Button onClick={() => navigate("/upload")} className="bg-violet-600 hover:bg-violet-500 text-white">
            Analyze Your First File
          </Button>
        </Card>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {history.map((scan) => {

            const date = scan?.created_at
              ? new Date(scan.created_at).toLocaleDateString(undefined, {
                year: "numeric",
                month: "short",
                day: "numeric"
              })
              : "Unknown";

            const similarity = scan?.similarity || {};
            const topMatchFile = Object.keys(similarity)[0] || null;
            const topMatchScore = topMatchFile ? similarity[topMatchFile] : 0;

            const algoName =
              (scan?.algorithm_detected || "Not Detected")
                .replace(/_/g, " ");

            return (
              <Card
                key={scan?.id || Math.random()}
                onClick={() => navigate(`/scan/${scan?.id}`)}
                className="glass-card border border-white/10 hover:border-violet-500/50 hover:bg-white/[0.04] cursor-pointer transition-all duration-300 group overflow-hidden flex flex-col hover:-translate-y-1 hover:shadow-xl hover:shadow-violet-500/10"
              >
                <div className="h-1.5 w-full bg-white/5 relative overflow-hidden">
                  <div
                    className={`absolute inset-y-0 left-0 transition-all duration-1000 ${topMatchScore >= 80
                      ? "bg-red-500"
                      : topMatchScore >= 50
                        ? "bg-amber-500"
                        : "bg-emerald-500"
                      }`}
                    style={{ width: `${topMatchScore}%` }}
                  />
                </div>

                <CardContent className="p-6 flex-1 flex flex-col">
                  <div className="flex justify-between items-start mb-6">
                    <div className="flex items-center gap-3 overflow-hidden">
                      <div className="w-10 h-10 rounded-lg bg-white/5 flex items-center justify-center shrink-0 group-hover:bg-violet-500/20 transition-colors">
                        <FileCode2 className="w-5 h-5 text-slate-400 group-hover:text-violet-400" />
                      </div>

                      <div className="overflow-hidden">
                        <h3
                          className="text-white font-medium text-base truncate"
                          title={scan?.filename}
                        >
                          {scan?.filename || "Unknown file"}
                        </h3>

                        <div className="flex items-center gap-2 mt-1 text-xs text-slate-500">
                          <span className="uppercase tracking-wider font-semibold text-slate-400">
                            {scan?.language || "TXT"}
                          </span>
                          <span>•</span>
                          <span className="flex items-center gap-1">
                            <Calendar className="w-3 h-3" /> {date}
                          </span>
                        </div>
                      </div>
                    </div>
                  </div>

                  <div className="space-y-3 mt-auto">
                    <div className="flex items-center justify-between text-sm border-t border-white/5 pt-3">
                      <span className="text-slate-400 flex items-center gap-2">
                        <Cpu className="w-4 h-4" /> Algorithm
                      </span>
                      <span className="text-white font-medium capitalize">
                        {algoName}
                      </span>
                    </div>

                    <div className="flex items-center justify-between text-sm">
                      <span className="text-slate-400 flex items-center gap-2">
                        <Database className="w-4 h-4" /> Top Match
                      </span>

                      <span
                        className={`font-bold ${topMatchScore >= 80
                          ? "text-red-400"
                          : topMatchScore >= 50
                            ? "text-amber-400"
                            : "text-emerald-400"
                          }`}
                      >
                        {topMatchScore}%
                      </span>
                    </div>
                  </div>
                </CardContent>
              </Card>
            );
          })}
        </div>
      )}
    </div>
  );
}