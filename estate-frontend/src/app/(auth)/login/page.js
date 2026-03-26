"use client";

import { useRouter } from "next/navigation";
import AuthForm from "@/components/AuthForm";
import { loginUser } from "@/lib/api";
import { useState } from "react";
import Link from "next/link";
import { UserPlus } from "lucide-react";

export default function Login() {
  const router = useRouter();
  const [error, setError] = useState("");

  const onSubmit = async (data) => {
    try {
      const res = await loginUser(data);
      localStorage.setItem("token", res.data.access_token);
      router.push("/chat");
    } catch {
      setError("Invalid credentials");
    }
  };

  return (
    <div className="min-h-screen w-full flex items-center justify-center relative overflow-hidden bg-gradient-to-br from-indigo-300 via-purple-300 to-pink-300">

      {/* Background Glow */}
      <div className="absolute w-[500px] h-[500px] bg-purple-500 opacity-20 blur-3xl top-[-150px] left-[-150px] rounded-full"></div>
      <div className="absolute w-[500px] h-[500px] bg-pink-500 opacity-20 blur-3xl bottom-[-150px] right-[-150px] rounded-full"></div>

      {/* Card */}
      <div className="relative w-full max-w-md mx-4 bg-white/90 backdrop-blur-xl rounded-3xl shadow-[0_20px_60px_rgba(0,0,0,0.15)] border border-white/40 p-8 space-y-6">

        {/* Header */}
        <div className="text-center space-y-2">
          <h1 className="text-3xl font-semibold text-slate-900">
            Welcome Back 👋
          </h1>
          <p className="text-sm text-slate-600">
            Let’s get you inside
          </p>
        </div>

        {/* Form */}
        <AuthForm type="login" onSubmit={onSubmit} error={error} />

        {/* Footer */}
        <p className="text-center text-sm text-slate-700">
          Don’t have an account?{" "}
          <Link
            href="/register"
            className="inline-flex items-center gap-1 font-medium text-indigo-600 hover:text-indigo-700 transition"
          >
            <UserPlus size={16} />
            Register
          </Link>
        </p>
      </div>
    </div>
  );
}