import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";

import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import {
  Field,
  FieldDescription,
  FieldGroup,
  FieldLabel,
  FieldSeparator,
} from "@/components/ui/field";
import { Input } from "@/components/ui/input";

const SignupForm = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const navigate = useNavigate();

  const handleSignup = async (e) => {
    e.preventDefault();
    setError("");

    if (!username.trim() || !password.trim()) {
      setError("Please fill in all fields.");
      return;
    }
    if (username.trim().length < 3) {
      setError("Username must be at least 3 characters.");
      return;
    }
    if (password.length < 8) {
      setError("Password must be at least 8 characters and include a number");
      return;
    }
    if (!(/[a-zA-Z]/.test(password)) || !(/[0-9]/.test(password))) {
      setError("Password must be at least 8 characters and include a number");
      return;
    }
    if (password !== confirmPassword) {
      setError("Passwords do not match.");
      return;
    }

    setLoading(true);

    try {
      const res = await fetch("https://plagiarism-detector-api-16d8.onrender.com/signup", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ username, password }),
      });

      const data = await res.json();

      if (!res.ok) {
        setError(data.detail || "Signup failed. Please try again.");
        return;
      }

      if (data.message) {
        navigate("/login", { state: { signupSuccess: true } });
      } else {
        setError("Signup failed. Please try again.");
      }
    } catch (err) {
      setError("Unable to connect to server. Please try again later.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <section className="login-bg min-h-screen flex items-center justify-center relative overflow-hidden">
      {/* Animated gradient orbs */}
      <div className="pointer-events-none absolute inset-0">
        <div className="absolute -top-32 -right-32 h-[500px] w-[500px] rounded-full bg-gradient-to-bl from-emerald-600/25 to-cyan-600/20 blur-3xl animate-pulse" />
        <div className="absolute -bottom-40 -left-40 h-[600px] w-[600px] rounded-full bg-gradient-to-tr from-violet-500/20 to-indigo-600/15 blur-3xl animate-pulse" style={{ animationDelay: "1s" }} />
        <div className="absolute top-1/3 left-1/2 -translate-x-1/2 h-[300px] w-[300px] rounded-full bg-gradient-to-r from-blue-500/10 to-purple-500/10 blur-3xl animate-pulse" style={{ animationDelay: "2s" }} />
      </div>

      <div className="py-10 md:py-20 max-w-md px-4 sm:px-0 mx-auto w-full relative z-10">
        <Card className="glass-card border border-white/10 px-6 py-8 sm:p-10 gap-6 shadow-2xl shadow-black/40">
          <CardHeader className="text-center gap-4 p-0">
            {/* Brand icon */}
            <div className="mx-auto w-12 h-12 rounded-xl bg-gradient-to-br from-emerald-500 to-cyan-600 flex items-center justify-center shadow-lg shadow-emerald-500/25 mb-2">
              <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="white" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2" /><circle cx="9" cy="7" r="4" /><line x1="19" y1="8" x2="19" y2="14" /><line x1="22" y1="11" x2="16" y2="11" /></svg>
            </div>

            <div className="flex flex-col gap-1">
              <CardTitle className="text-2xl font-semibold text-white tracking-tight">
                Join CodeGuard
              </CardTitle>
              <CardDescription className="text-sm text-slate-400 font-normal">
                Create your account to get started
              </CardDescription>
            </div>
          </CardHeader>

          <CardContent className="p-0">
            <form onSubmit={handleSignup}>
              <FieldGroup className="gap-5">
                <FieldSeparator className="*:data-[slot=field-separator-content]:bg-transparent text-xs text-slate-500 uppercase tracking-widest bg-transparent">
                  <span className="px-3">create account</span>
                </FieldSeparator>

                {error && (
                  <div className="rounded-lg bg-red-500/10 border border-red-500/20 px-4 py-3 text-sm text-red-400 flex items-center gap-2">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><circle cx="12" cy="12" r="10" /><line x1="12" y1="8" x2="12" y2="12" /><line x1="12" y1="16" x2="12.01" y2="16" /></svg>
                    {error}
                  </div>
                )}

                <div className="flex flex-col gap-4">
                  <Field className="gap-1.5">
                    <FieldLabel className="text-sm text-slate-300 font-normal">
                      Username
                    </FieldLabel>
                    <Input
                      id="signup-username"
                      placeholder="Choose a username"
                      required
                      className="glass-input h-10"
                      value={username}
                      onChange={(e) => setUsername(e.target.value)}
                    />
                  </Field>

                  <Field className="gap-1.5">
                    <FieldLabel className="text-sm text-slate-300 font-normal">
                      Password
                    </FieldLabel>
                    <Input
                      id="signup-password"
                      type="password"
                      placeholder="Create a password"
                      required
                      className="glass-input h-10"
                      value={password}
                      onChange={(e) => setPassword(e.target.value)}
                    />
                  </Field>

                  <Field className="gap-1.5">
                    <FieldLabel className="text-sm text-slate-300 font-normal">
                      Confirm Password
                    </FieldLabel>
                    <Input
                      id="signup-confirm-password"
                      type="password"
                      placeholder="Confirm your password"
                      required
                      className="glass-input h-10"
                      value={confirmPassword}
                      onChange={(e) => setConfirmPassword(e.target.value)}
                    />
                  </Field>
                </div>

                <Field className="gap-4">
                  <Button
                    id="signup-submit"
                    type="submit"
                    size="lg"
                    disabled={loading}
                    className="rounded-lg h-11 bg-gradient-to-r from-emerald-600 to-cyan-600 hover:from-emerald-500 hover:to-cyan-500 text-white font-medium cursor-pointer transition-all duration-300 shadow-lg shadow-emerald-600/25 hover:shadow-emerald-500/40 disabled:opacity-50 disabled:cursor-not-allowed"
                  >
                    {loading ? (
                      <span className="flex items-center gap-2">
                        <svg className="animate-spin h-4 w-4" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                          <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" />
                          <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z" />
                        </svg>
                        Creating account...
                      </span>
                    ) : (
                      "Create Account"
                    )}
                  </Button>

                  <FieldDescription className="text-center text-sm font-normal text-slate-500">
                    Already have an account?{" "}
                    <Link to="/login" className="font-medium text-emerald-400 hover:text-emerald-300 transition-colors">
                      Sign in
                    </Link>
                  </FieldDescription>
                </Field>
              </FieldGroup>
            </form>
          </CardContent>
        </Card>
      </div>
    </section>
  );
};

export default SignupForm;
