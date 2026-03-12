import { useState } from "react";
import { Link, useLocation, Outlet, useNavigate } from "react-router-dom";
import { LayoutDashboard, FileUp, History, LogOut, Menu, X, ShieldAlert } from "lucide-react";
import { Button } from "@/components/ui/button";

export default function SidebarLayout() {
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);
  const location = useLocation();
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem("token");
    navigate("/login");
  };

  const navItems = [
    { name: "Dashboard", href: "/dashboard", icon: LayoutDashboard },
    { name: "Upload Code", href: "/upload", icon: FileUp },
    { name: "Scan History", href: "/history", icon: History },
  ];

  return (
    <div className="flex h-screen bg-slate-950 text-white overflow-hidden upload-bg relative">
      {/* Background gradients */}
      <div className="pointer-events-none absolute inset-0 z-0 overflow-hidden">
        <div className="absolute top-0 right-0 h-[500px] w-[500px] rounded-full bg-gradient-to-bl from-violet-600/10 to-transparent blur-3xl opacity-50" />
        <div className="absolute bottom-0 left-0 h-[500px] w-[500px] rounded-full bg-gradient-to-tr from-cyan-600/10 to-transparent blur-3xl opacity-50" />
      </div>

      {/* Mobile sidebar backdrop */}
      {isMobileMenuOpen && (
        <div 
          className="fixed inset-0 z-40 bg-black/50 backdrop-blur-sm lg:hidden transition-opacity"
          onClick={() => setIsMobileMenuOpen(false)}
        />
      )}

      {/* Sidebar */}
      <aside 
        className={`fixed inset-y-0 left-0 z-50 w-64 glass-card border-r border-white/5 flex flex-col transition-transform duration-300 ease-in-out lg:static lg:translate-x-0 ${isMobileMenuOpen ? "translate-x-0" : "-translate-x-full"}`}
      >
        <div className="flex items-center justify-between h-20 px-6 border-b border-white/5 shrink-0">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-violet-500 to-indigo-600 flex items-center justify-center shadow-lg shadow-violet-500/20">
              <ShieldAlert className="w-5 h-5 text-white" />
            </div>
            <span className="text-xl font-bold tracking-tight text-white">CodeGuard</span>
          </div>
          <button 
            className="lg:hidden text-slate-400 hover:text-white transition-colors"
            onClick={() => setIsMobileMenuOpen(false)}
          >
            <X className="w-6 h-6" />
          </button>
        </div>

        <nav className="flex-1 px-4 py-6 space-y-2 overflow-y-auto">
          {navItems.map((item) => {
            const isActive = location.pathname.startsWith(item.href);
            return (
              <Link key={item.name} to={item.href} onClick={() => setIsMobileMenuOpen(false)}>
                <span className={`flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-200 group ${isActive ? "bg-violet-500/15 text-violet-300 border border-violet-500/20 shadow-inner" : "text-slate-400 hover:bg-white/5 hover:text-slate-200 border border-transparent"}`}>
                  <item.icon className={`w-5 h-5 ${isActive ? "text-violet-400" : "text-slate-500 group-hover:text-slate-300 transition-colors"}`} />
                  <span className="font-medium text-sm">{item.name}</span>
                </span>
              </Link>
            );
          })}
        </nav>

        <div className="p-4 border-t border-white/5 shrink-0 bg-white/[0.02]">
          <Button 
            onClick={handleLogout} 
            variant="ghost" 
            className="w-full flex items-center justify-start gap-3 px-4 py-3 h-auto rounded-xl text-slate-400 hover:text-rose-400 hover:bg-rose-500/10 cursor-pointer transition-all"
          >
            <LogOut className="w-5 h-5" />
            <span className="font-medium text-sm">Logout</span>
          </Button>
        </div>
      </aside>

      {/* Main Content Area */}
      <div className="flex-1 flex flex-col min-w-0 z-10 relative h-full">
        {/* Mobile Header */}
        <header className="lg:hidden h-16 flex items-center justify-between px-4 border-b border-white/5 glass-card shrink-0">
          <div className="flex items-center gap-2">
            <div className="w-8 h-8 rounded-lg bg-gradient-to-br from-violet-500 to-indigo-600 flex items-center justify-center">
              <ShieldAlert className="w-4 h-4 text-white" />
            </div>
            <span className="font-bold text-white">CodeGuard</span>
          </div>
          <button 
            className="text-slate-400 hover:text-white"
            onClick={() => setIsMobileMenuOpen(true)}
          >
            <Menu className="w-6 h-6" />
          </button>
        </header>

        {/* Dynamic Outlet */}
        <main className="flex-1 overflow-x-hidden overflow-y-auto h-full scroll-smooth">
          <Outlet />
        </main>
      </div>
    </div>
  );
}
