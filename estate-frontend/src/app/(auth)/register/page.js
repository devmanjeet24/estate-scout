"use client";

import { useRouter } from "next/navigation";
import AuthForm from "@/components/AuthForm";
import { registerUser } from "@/lib/api";
import Link from "next/link";
import { FaUserPlus, FaSignInAlt } from "react-icons/fa";

export default function Register() {
  const router = useRouter();

  const onSubmit = async (data) => {
    await registerUser(data);
    router.push("/login");
  };

  return (
    <div className="h-screen flex items-center justify-center bg-gradient-to-br from-pink-100 via-purple-100 to-indigo-100 overflow-hidden">
      
      {/* Card */}
      <div className="w-full max-w-sm bg-white/80 backdrop-blur-xl rounded-3xl shadow-2xl p-5 border border-white/40 flex flex-col justify-center gap-4">

        {/* Header */}
        <div className="text-center">
          <div className="flex justify-center mb-2">
            <div className="p-2 rounded-full bg-pink-500 text-white text-lg shadow-md">
              <FaUserPlus />
            </div>
          </div>

          <h1 className="text-xl font-bold text-gray-800">
            Create Account 
          </h1>
          <p className="text-gray-500 text-xs">
            Join us and get started
          </p>
        </div>

        {/* Form */}
        <div className="scale-[0.95]">
          <AuthForm type="register" onSubmit={onSubmit} />
        </div>

        {/* Login Link */}
        <p className="text-center text-xs text-gray-600">
          Already have an account?{" "}
          <Link
            href="/login"
            className="inline-flex items-center gap-1 font-semibold text-indigo-600 hover:text-indigo-800 transition"
          >
            <FaSignInAlt />
            Login
          </Link>
        </p>
      </div>
    </div>
  );
}