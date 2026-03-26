"use client";

import { useChat } from "@/hooks/useChat";
import { useRouter } from "next/navigation";
import { useState } from "react";
import {
  HambergerMenu,
  ArrowLeft2,
  AddSquare,
  Clock,
  Logout,
} from "iconsax-react";

export default function Sidebar() {
  const [open, setOpen] = useState(true);
  const router = useRouter();
  const { clearChat } = useChat();

  return (
    <div
      className={`h-screen ${
        open ? "w-64" : "w-20"
      } bg-[#0f172a] flex flex-col transition-all duration-300`}
    >
      {/* Top */}
      <div className="flex items-center justify-between p-4">
        {open && (
          <h1 className="text-lg font-semibold text-white">
            Property AI
          </h1>
        )}

        <button
          onClick={() => setOpen(!open)}
          className="p-2 rounded-lg bg-white/10 hover:bg-white/20 transition"
        >
          {open ? (
            <ArrowLeft2 size="20" color="#fff" />
          ) : (
            <HambergerMenu size="20" color="#fff" />
          )}
        </button>
      </div>

      {/* Menu */}
      <div className="flex flex-col gap-3 px-3 mt-4">

        {/* New Chat */}
        <button
          onClick={() => {
            clearChat();
            router.push("/chat");
          }}
          className="flex items-center gap-3 p-3 rounded-xl bg-indigo-500/10 hover:bg-indigo-500/20 transition"
        >
          <AddSquare size="22" color="#818cf8" variant="Bold" />
          {open && (
            <span className="text-white text-sm font-medium">
              New Chat
            </span>
          )}
        </button>

        {/* History */}
        <button
          onClick={() => router.push("/history")}
          className="flex items-center gap-3 p-3 rounded-xl bg-purple-500/10 hover:bg-purple-500/20 transition"
        >
          <Clock size="22" color="#c084fc" variant="Bold" />
          {open && (
            <span className="text-white text-sm font-medium">
              History
            </span>
          )}
        </button>
      </div>

      {/* Bottom */}
      <div className="mt-auto p-3">
        <button
          onClick={() => {
            localStorage.removeItem("token");
            router.push("/login");
          }}
          className="w-full flex items-center gap-3 p-3 rounded-xl bg-red-500/10 hover:bg-red-500/20 transition"
        >
          <Logout size="22" color="#f87171" variant="Bold" />
          {open && (
            <span className="text-red-400 text-sm font-medium">
              Logout
            </span>
          )}
        </button>
      </div>
    </div>
  );
}