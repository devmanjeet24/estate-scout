"use client";

import { useEffect } from "react";
import { useRouter } from "next/navigation";
import ChatWindow from "@/components/ChatWindow";
import PropertyPanel from "@/components/PropertyPanel";
import { useChat } from "@/hooks/useChat";
import { MdOutlineRealEstateAgent } from "react-icons/md";

export default function ChatPage() {
  const router = useRouter();
  const { messages, send, properties } = useChat();

  useEffect(() => {
    const token = localStorage.getItem("token");
    if (!token) router.push("/login");
  }, []);

  return (
    <div className="h-screen w-full flex overflow-hidden bg-gradient-to-br from-indigo-100 via-purple-100 to-pink-100">

      {/* LEFT SIDE (CHAT) */}
      <div className="flex-1 flex flex-col p-6 gap-4">

        {/* Header */}
        <div className="flex items-center gap-3 px-5 py-4 rounded-2xl bg-white/80 backdrop-blur border border-white/40 shadow-md">
          <div className="p-3 bg-indigo-500 text-white rounded-xl shadow">
            <MdOutlineRealEstateAgent size={20}/> 
          </div>

          <div>
            <h1 className="text-lg font-semibold text-slate-900">
              Property AI
            </h1>
            <p className="text-xs text-slate-500">
              Find your perfect home with AI
            </p>
          </div>
        </div>

        {/* Chat Box */}
        <div className="flex-1 rounded-3xl bg-white/70 backdrop-blur-xl border border-white/40 shadow-lg overflow-hidden flex flex-col">
          <ChatWindow messages={messages} send={send} />
        </div>

      </div>

      {/* RIGHT SIDE (PROPERTY PANEL) */}
      <div className="w-[380px] p-6">

        <div className="h-full rounded-3xl bg-white/80 backdrop-blur-xl border border-white/40 shadow-lg flex flex-col">

          {/* Panel Header */}
          <div className="px-5 py-4 border-b border-slate-200">
            <h2 className="text-sm font-semibold text-slate-800">
              Recommended Properties
            </h2>
          </div>

          {/* Panel Content */}
          <div className="flex-1 overflow-auto">
            <PropertyPanel properties={properties} />
          </div>

        </div>

      </div>

    </div>
  );
}