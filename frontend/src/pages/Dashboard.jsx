import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card";
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, PieChart, Pie, Cell, LineChart, Line, CartesianGrid } from "recharts";
import { ShieldAlert, FileCode2, History, AlertTriangle } from "lucide-react";

const COLORS = ['#8b5cf6', '#34d399', '#f59e0b', '#ef4444', '#3b82f6'];

export default function Dashboard() {
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    const fetchStats = async () => {
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

        if (!res.ok) throw new Error("Failed to load dashboard statistics");

        const data = await res.json();
        setHistory(data);
      } catch (err) {
        setError(err.message || "Network error loading dashboard");
      } finally {
        setLoading(false);
      }
    };

    fetchStats();
  }, [navigate]);

  if (loading) {
    return (
      <div className="flex h-full items-center justify-center py-32">
        <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-violet-500"></div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="p-8">
        <div className="rounded-xl bg-red-500/10 border border-red-500/20 p-6 flex items-start gap-4 text-red-400">
          <AlertTriangle className="w-6 h-6 mt-0.5 shrink-0" />
          <div>
            <h3 className="text-lg font-semibold text-red-400 mb-1">Failed to load Dashboard</h3>
            <p className="text-sm opacity-80">{error}</p>
          </div>
        </div>
      </div>
    );
  }

  // Analytics Math
  const totalScans = history.length;
  let algorithmCounts = {};
  let languageCounts = {};
  let totalSimilarity = 0;
  let scansWithMatches = 0;

  // Time series data formatting
  let recentActivityMap = {};

  history.forEach(scan => {
    // algorithms
    let algo = scan.algorithm_detected;
    if (algo && algo !== "None") {
      algo = algo.replace(/_/g, " ");
      algorithmCounts[algo] = (algorithmCounts[algo] || 0) + 1;
    }

    // language
    let lang = scan.language || "unknown";
    languageCounts[lang] = (languageCounts[lang] || 0) + 1;

    // similarities
    if (scan.similarity) {
      const highest = Object.values(scan.similarity).sort((a, b) => b - a)[0];
      if (highest) {
        totalSimilarity += highest;
        scansWithMatches++;
      }
    }

    // Dates for line chart
    const d = new Date(scan.created_at);
    const dateStr = d.toLocaleDateString(undefined, { month: 'short', day: 'numeric' });
    recentActivityMap[dateStr] = (recentActivityMap[dateStr] || 0) + 1;
  });

  const avgSimilarity = scansWithMatches > 0 ? Math.round(totalSimilarity / scansWithMatches) : 0;
  const mostDetectedAlgo = Object.entries(algorithmCounts).sort((a, b) => b[1] - a[1])[0] || ["None", 0];

  const algorithmData = Object.entries(algorithmCounts).map(([name, count]) => ({ name, count }));
  const languageData = Object.entries(languageCounts).map(([name, value]) => ({ name, value }));
  const timeData = Object.entries(recentActivityMap).reverse().map(([date, scans]) => ({ date, scans })).slice(-10);

  return (
    <div className="p-6 md:p-8 max-w-7xl mx-auto space-y-8 animate-in fade-in duration-500">
      <div className="mb-4">
        <h1 className="text-3xl font-bold text-white tracking-tight">Dashboard Overview</h1>
        <p className="text-slate-400 mt-1">Analytics spanning your entire CodeGuard history</p>
      </div>

      {/* Hero KPIs */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        <Card className="glass-card border border-white/10 bg-white/[0.02]">
          <CardContent className="p-6">
            <div className="flex items-center justify-between mb-4">
              <p className="text-sm font-medium text-slate-400 uppercase tracking-wider">Total Scans</p>
              <div className="w-8 h-8 rounded-lg bg-violet-500/10 flex items-center justify-center">
                <History className="w-4 h-4 text-violet-400" />
              </div>
            </div>
            <p className="text-3xl font-bold text-white">{totalScans}</p>
          </CardContent>
        </Card>

        <Card className="glass-card border border-white/10 bg-white/[0.02]">
          <CardContent className="p-6">
            <div className="flex items-center justify-between mb-4">
              <p className="text-sm font-medium text-slate-400 uppercase tracking-wider">Average Similarity</p>
              <div className="w-8 h-8 rounded-lg bg-emerald-500/10 flex items-center justify-center">
                <ShieldAlert className="w-4 h-4 text-emerald-400" />
              </div>
            </div>
            <div className="flex items-baseline gap-2">
              <p className="text-3xl font-bold text-white">{avgSimilarity}%</p>
            </div>
          </CardContent>
        </Card>

        <Card className="glass-card border border-white/10 bg-white/[0.02]">
          <CardContent className="p-6">
            <div className="flex items-center justify-between mb-4">
              <p className="text-sm font-medium text-slate-400 uppercase tracking-wider">Top Algorithm</p>
              <div className="w-8 h-8 rounded-lg bg-amber-500/10 flex items-center justify-center">
                <FileCode2 className="w-4 h-4 text-amber-400" />
              </div>
            </div>
            <p className="text-xl font-bold text-white truncate capitalize">{mostDetectedAlgo[0]}</p>
          </CardContent>
        </Card>

        <Card className="glass-card border border-white/10 bg-white/[0.02]">
          <CardContent className="p-6">
            <div className="flex items-center justify-between mb-4">
              <p className="text-sm font-medium text-slate-400 uppercase tracking-wider">Stored Profiles</p>
              <div className="w-8 h-8 rounded-lg bg-blue-500/10 flex items-center justify-center">
                <ShieldAlert className="w-4 h-4 text-blue-400" />
              </div>
            </div>
            <p className="text-3xl font-bold text-white">530</p>
          </CardContent>
        </Card>
      </div>

      {totalScans > 0 && (
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          {/* Algorithms Bar Chart */}
          <Card className="glass-card border border-white/10 bg-black/20">
            <CardHeader className="pb-2">
              <CardTitle className="text-lg font-medium text-white">Algorithms Detected</CardTitle>
              <CardDescription className="text-slate-400">Distribution of structural footprints</CardDescription>
            </CardHeader>
            <CardContent className="h-72">
              <ResponsiveContainer width="100%" height="100%">
                <BarChart data={algorithmData} margin={{ top: 20, right: 30, left: 0, bottom: 5 }}>
                  <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.05)" vertical={false} />
                  <XAxis dataKey="name" stroke="#64748b" fontSize={11} tickLine={false} axisLine={false} />
                  <YAxis stroke="#64748b" fontSize={11} tickLine={false} axisLine={false} allowDecimals={false} />
                  <Tooltip
                    cursor={{ fill: 'rgba(255,255,255,0.05)' }}
                    contentStyle={{ backgroundColor: 'rgba(15,23,42,0.9)', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '8px' }}
                    itemStyle={{ color: '#fff' }}
                  />
                  <Bar dataKey="count" fill="#8b5cf6" radius={[4, 4, 0, 0]} maxBarSize={50} />
                </BarChart>
              </ResponsiveContainer>
            </CardContent>
          </Card>

          {/* Scans Over Time Line Chart */}
          <Card className="glass-card border border-white/10 bg-black/20">
            <CardHeader className="pb-2">
              <CardTitle className="text-lg font-medium text-white">Recent Scan Activity</CardTitle>
              <CardDescription className="text-slate-400">Submissions verified across the last 10 days</CardDescription>
            </CardHeader>
            <CardContent className="h-72">
              <ResponsiveContainer width="100%" height="100%">
                <LineChart data={timeData} margin={{ top: 20, right: 30, left: 0, bottom: 5 }}>
                  <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.05)" vertical={false} />
                  <XAxis dataKey="date" stroke="#64748b" fontSize={11} tickLine={false} axisLine={false} />
                  <YAxis stroke="#64748b" fontSize={11} tickLine={false} axisLine={false} allowDecimals={false} />
                  <Tooltip
                    contentStyle={{ backgroundColor: 'rgba(15,23,42,0.9)', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '8px' }}
                    itemStyle={{ color: '#fff' }}
                  />
                  <Line type="monotone" dataKey="scans" stroke="#34d399" strokeWidth={3} dot={{ fill: '#34d399', r: 4 }} activeDot={{ r: 6, strokeWidth: 0 }} />
                </LineChart>
              </ResponsiveContainer>
            </CardContent>
          </Card>

          {/* Languages Pie Chart */}
          <Card className="glass-card border border-white/10 bg-black/20 lg:col-span-2">
            <CardHeader className="pb-2">
              <CardTitle className="text-lg font-medium text-white">Language Diagnostics</CardTitle>
              <CardDescription className="text-slate-400">File extension distributions evaluated natively</CardDescription>
            </CardHeader>
            <CardContent className="h-72 flex items-center justify-center">
              <ResponsiveContainer width="100%" height="100%">
                <PieChart>
                  <Tooltip
                    contentStyle={{ backgroundColor: 'rgba(15,23,42,0.9)', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '8px' }}
                    itemStyle={{ color: '#fff' }}
                  />
                  <Pie
                    data={languageData}
                    cx="50%"
                    cy="50%"
                    innerRadius={60}
                    outerRadius={100}
                    paddingAngle={5}
                    dataKey="value"
                    label={({ name, percent }) => `${name.toUpperCase()} ${(percent * 100).toFixed(0)}%`}
                    labelLine={false}
                  >
                    {languageData.map((entry, index) => (
                      <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} stroke="rgba(0,0,0,0.2)" />
                    ))}
                  </Pie>
                </PieChart>
              </ResponsiveContainer>
            </CardContent>
          </Card>
        </div>
      )}
    </div>
  );
}
