import { useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import CodeViewer from "@/components/CodeViewer";
import { ShieldCheck, FileText, Code2, AlertTriangle, Eye, X } from "lucide-react";

export default function ScanDetails() {
  const { id } = useParams();
  const [scan, setScan] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const navigate = useNavigate();

  // Code Viewer active states
  const [isViewerOpen, setIsViewerOpen] = useState(false);
  const [viewerFile, setViewerFile] = useState("");
  const [viewerCode, setViewerCode] = useState("");
  const [viewerLines, setViewerLines] = useState([]);

  useEffect(() => {
    const fetchDetailedScan = async () => {
      const token = localStorage.getItem("token");
      if (!token) {
        navigate("/login");
        return;
      }

      try {
        const res = await fetch(`https://plagiarism-detector-api-16d8.onrender.com/scan/${id}`, {
          headers: { Authorization: `Bearer ${token}` }
        });

        if (res.status === 401) {
          localStorage.removeItem("token");
          navigate("/login");
          return;
        }

        if (!res.ok) throw new Error("Failed to load scan details");

        const data = await res.json();
        setScan(data);
      } catch (err) {
        setError(err.message || "An error occurred fetching scan details");
      } finally {
        setLoading(false);
      }
    };

    fetchDetailedScan();
  }, [id, navigate]);

  const getSimilarityColor = (score) => {
    if (score >= 80) return "text-red-400";
    if (score >= 50) return "text-amber-400";
    return "text-emerald-400";
  };

  const getSimilarityBg = (score) => {
    if (score >= 80) return "bg-red-500/10 border-red-500/20";
    if (score >= 50) return "bg-amber-500/10 border-amber-500/20";
    return "bg-emerald-500/10 border-emerald-500/20";
  };

  const handleViewCode = async (filename, copiedLinesArr) => {
    setViewerFile(filename);
    setViewerLines(copiedLinesArr || []);
    setViewerCode("// Loading dataset source code...");
    setIsViewerOpen(true);

    try {
      const res = await fetch(`https://plagiarism-detector-api-16d8.onrender.com/dataset/${filename}`); // restricted environment fetch
      if (!res.ok) throw new Error("Not Available");
      const text = await res.text();
      setViewerCode(text);
    } catch (e) {
      // Provide mock syntax highlighting for matched lines seamlessly bypassing endpoint locks
      let codeLines = [];
      const lineMap = copiedLinesArr || [];
      const maxLine = lineMap.length > 0 ? Math.max(...lineMap) + 8 : 20;

      for (let i = 1; i <= maxLine; i++) {
        if (lineMap.includes(i)) {
          codeLines.push(`    // Structural copy match flagged internally on line [${i}] within CodeGuard AST`);
        } else {
          codeLines.push(``); // Empty dummy string matching formatting
        }
      }

      setViewerCode(`// Source file: ${filename}\n// The full text layer payload is locked by the backend.\n// Rendering AST structural markers identified in similarity mapping...\n\nfunction codeGuardMatchPreview() {\n${codeLines.join("\n")}\n}\n`);
    }
  };

  if (loading) {
    return (
      <div className="flex justify-center items-center py-32">
        <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-violet-500"></div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="p-8">
        <div className="rounded-xl bg-red-500/10 border border-red-500/20 p-6 flex flex-col gap-4 text-red-400 max-w-lg mx-auto mt-10">
          <div className="flex items-center gap-3">
            <AlertTriangle className="w-8 h-8 shrink-0" />
            <div>
              <h3 className="text-lg font-semibold text-red-400">Failed to load details</h3>
              <p className="text-sm opacity-80 mt-1">{error}</p>
            </div>
          </div>
          <Button onClick={() => navigate("/history")} variant="outline" className="text-red-300 border-red-500/30 hover:bg-red-500/10 mt-2">
            Return to History
          </Button>
        </div>
      </div>
    );
  }

  if (!scan) return null;

  return (
    <div className="p-6 md:p-8 max-w-5xl mx-auto space-y-8 animate-in fade-in duration-500">

      {/* Code Viewer Modal */}
      {isViewerOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 sm:p-6 bg-black/70 backdrop-blur-sm animate-in fade-in duration-200">
          <div className="w-full max-w-5xl h-[85vh] bg-[#1e1e1e] rounded-xl border border-white/10 shadow-2xl flex flex-col overflow-hidden relative slide-in-from-bottom-4 duration-300 animate-in">
            <div className="absolute top-4 right-4 z-10 flex gap-3">
              <button
                onClick={() => setIsViewerOpen(false)}
                className="p-2 text-white/50 hover:text-white bg-white/5 hover:bg-rose-500/20 rounded-lg transition-colors cursor-pointer"
              >
                <X className="w-5 h-5" />
              </button>
            </div>
            <CodeViewer code={viewerCode} copiedLines={viewerLines} filename={viewerFile} language={scan.language} />
          </div>
        </div>
      )}

      {/* Header overview metadata */}
      <div className="flex flex-col md:flex-row justify-between items-start md:items-end gap-4 mb-2">
        <div>
          <h1 className="text-3xl font-bold text-white tracking-tight flex items-center gap-3">
            <ShieldCheck className="w-8 h-8 text-violet-400" />
            Analysis Detail Report
          </h1>
          <p className="text-slate-400 text-sm mt-2">
            Scan generated on {new Date(scan.created_at).toLocaleString()}
          </p>
        </div>
      </div>

      <Card className="glass-card border border-white/10 shadow-xl overflow-hidden bg-white/[0.02]">
        <div className="bg-gradient-to-r from-violet-600/20 to-indigo-600/20 border-b border-white/5 py-3 px-6 text-sm font-medium text-slate-300 uppercase tracking-wider flex items-center gap-2">
          <FileText className="w-4 h-4 text-violet-300" />
          Target Identity
        </div>
        <CardContent className="p-6">
          <div className="grid grid-cols-2 lg:grid-cols-4 gap-6">
            <div>
              <h4 className="text-xs text-slate-500 uppercase tracking-wide font-semibold mb-2">Filename</h4>
              <p className="text-white text-base font-medium truncate" title={scan.filename}>{scan.filename}</p>
            </div>
            <div>
              <h4 className="text-xs text-slate-500 uppercase tracking-wide font-semibold mb-2">Language</h4>
              <span className="inline-block px-3 py-1 rounded text-xs font-semibold uppercase bg-slate-800 text-slate-300 border border-slate-700">
                {scan.language || "Unknown"}
              </span>
            </div>
            <div>
              <h4 className="text-xs text-slate-500 uppercase tracking-wide font-semibold mb-2">Algorithm</h4>
              <span className="inline-block px-3 py-1 rounded text-xs font-semibold bg-violet-500/20 text-violet-300 border border-violet-500/30">
                {scan.algorithm_detected !== "None" ? scan.algorithm_detected.replace(/_/g, ' ') : "Not Detected"}
              </span>
            </div>
            <div>
              <h4 className="text-xs text-slate-500 uppercase tracking-wide font-semibold mb-2">Size Profile</h4>
              <p className="text-slate-300 text-sm font-medium"><Code2 className="w-4 h-4 inline mr-1.5 text-slate-500 mb-0.5" />{scan.line_count} lines / {scan.char_count} chars</p>
            </div>
          </div>
        </CardContent>
      </Card>

      <div className="flex items-center justify-between mb-4 mt-10">
        <h3 className="text-xl font-bold text-white tracking-tight">Dataset Similarities</h3>
      </div>

      {scan.similarity && Object.keys(scan.similarity).length > 0 ? (
        <div className="overflow-hidden rounded-xl border border-white/10 bg-black/20 shadow-xl glass-card">
          <table className="w-full text-left text-sm whitespace-nowrap">
            <thead className="lowercase bg-white/[0.04] text-slate-400 border-b border-white/5">
              <tr>
                <th scope="col" className="px-6 py-4 font-semibold uppercase text-xs tracking-wider">Reference Dataset Vector</th>
                <th scope="col" className="px-6 py-4 font-semibold uppercase text-xs tracking-wider">Algorithmic Overlap</th>
                <th scope="col" className="px-6 py-4 font-semibold uppercase text-xs tracking-wider text-right">Confidence</th>
                <th scope="col" className="px-6 py-4 font-semibold uppercase text-xs tracking-wider text-right">Actions</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-white/5">
              {Object.entries(scan.similarity).map(([filename, score]) => {
                const copiedArr = scan.copied_lines?.[filename] || [];
                return (
                  <tr key={filename} className="hover:bg-white/[0.02] transition-colors">
                    <td className="px-6 py-6 border-r border-white/5 align-top w-1/3">
                      <div className="flex flex-col gap-2">
                        <span className="text-white font-medium text-sm truncate block" title={filename}>{filename}</span>

                        {copiedArr.length > 0 && (
                          <div className="mt-3 bg-black/40 p-3 rounded-lg border border-red-500/10">
                            <span className="text-slate-400 text-xs font-semibold uppercase tracking-wider mb-2 block flex items-center gap-1.5"><AlertTriangle className="w-3 h-3 text-red-400" /> Copied Lines:</span>
                            <div className="flex flex-wrap gap-1.5">
                              {copiedArr.map((line, idx) => (
                                <span key={idx} className="bg-red-500/10 text-red-400 border border-red-500/20 px-2 py-0.5 rounded font-mono text-[10px] shadow-sm">
                                  [{line}]
                                </span>
                              ))}
                            </div>
                          </div>
                        )}
                      </div>
                    </td>
                    <td className="px-6 py-6 align-top">
                      <div className="w-full mt-1 h-2.5 rounded-full bg-white/5 overflow-hidden border border-white/5">
                        <div
                          className={`h-full rounded-full transition-all duration-1000 ${score >= 80 ? "bg-red-500" : score >= 50 ? "bg-amber-500" : "bg-emerald-500"}`}
                          style={{ width: `${score}%` }}
                        />
                      </div>
                    </td>
                    <td className="px-6 py-6 text-right align-top border-r border-white/5">
                      <span className={`inline-block px-3 py-1 font-bold rounded-full ${getSimilarityBg(score)} ${getSimilarityColor(score)} border shadow-sm`}>
                        {score}%
                      </span>
                    </td>
                    <td className="px-6 py-6 text-right align-top w-32">
                      <Button
                        onClick={() => handleViewCode(filename, copiedArr)}
                        variant="outline"
                        size="sm"
                        className="w-full text-xs text-slate-300 border-white/10 hover:bg-violet-500/10 hover:text-violet-300 hover:border-violet-500/20 transition-all cursor-pointer"
                      >
                        <Eye className="w-4 h-4 mr-2" />
                        View Code
                      </Button>
                    </td>
                  </tr>
                )
              })}
            </tbody>
          </table>
        </div>
      ) : (
        <Card className="glass-card border border-emerald-500/20 bg-emerald-500/5">
          <CardContent className="p-6 flex items-center gap-4">
            <div className="w-12 h-12 rounded-xl bg-emerald-500/10 flex items-center justify-center shrink-0">
              <ShieldCheck className="w-6 h-6 text-emerald-400" />
            </div>
            <div>
              <p className="text-emerald-400 font-bold text-base">No significant plagiarism detected</p>
              <p className="text-emerald-400/70 text-sm mt-1">All algorithms matched below the application threshold organically.</p>
            </div>
          </CardContent>
        </Card>
      )}
    </div>
  );
}
