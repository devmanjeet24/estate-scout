"use client";

import { useForm } from "react-hook-form";
import { Mail, Lock, User } from "lucide-react";

export default function AuthForm({ onSubmit, type, error, loading }) {
  const { register, handleSubmit } = useForm();

  return (
    <form
      onSubmit={handleSubmit(onSubmit)}
      className="flex flex-col gap-5"
    >
      {/* Title */}
      <h2 className="text-lg font-semibold text-center text-slate-800">
        {type === "login" ? "Login" : "Create Account"}
      </h2>

      {/* Name */}
      {type === "register" && (
        <div className="relative">
          <User className="absolute left-3 top-1/2 -translate-y-1/2 text-slate-500" size={18} />
          <input
            {...register("name")}
            placeholder="Full Name"
            className="w-full pl-10 pr-3 py-3 rounded-xl bg-white border border-slate-200 text-slate-800 placeholder-slate-400 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 outline-none transition"
          />
        </div>
      )}

      {/* Email */}
      <div className="relative">
        <Mail className="absolute left-3 top-1/2 -translate-y-1/2 text-slate-500" size={18} />
        <input
          {...register("email")}
          placeholder="Email address"
          className="w-full pl-10 pr-3 py-3 rounded-xl bg-white border border-slate-200 text-slate-800 placeholder-slate-400 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 outline-none transition"
        />
      </div>

      {/* Password */}
      <div className="relative">
        <Lock className="absolute left-3 top-1/2 -translate-y-1/2 text-slate-500" size={18} />
        <input
          {...register("password")}
          type="password"
          placeholder="Password"
          className="w-full pl-10 pr-3 py-3 rounded-xl bg-white border border-slate-200 text-slate-800 placeholder-slate-400 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 outline-none transition"
        />
      </div>

      {/* Error */}
      {error && (
        <p className="text-red-500 text-sm text-center">
          {error}
        </p>
      )}

      {/* Button */}
      <button
        className="w-full py-3 rounded-xl bg-gradient-to-r from-indigo-500 to-purple-500 text-white font-semibold shadow-lg transition-all duration-200 hover:opacity-90 active:scale-[0.98]"
      >
        {loading ? "Loading..." : type === "login" ? "Login" : "Register"}
      </button>
    </form>
  );
}