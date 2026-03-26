"use client";

import { useForm } from "react-hook-form";
import {  User, Cpu } from "iconsax-react";
import { IoIosSend } from "react-icons/io";


export default function ChatWindow({ messages, send }) {
  const { register, handleSubmit, reset } = useForm();

  const onSubmit = (data) => {
    if (!data.message) return;
    send(data.message);
    reset();
  };

  return (
    <div className="flex flex-col h-full">

      {/* Messages */}
      <div className="flex-1 overflow-y-auto px-6 py-6 space-y-5">

        {/* Empty State */}
        {messages.length === 0 && (
          <div className="flex flex-col items-center justify-center mt-24 text-center text-slate-500">
            <div className="text-4xl mb-3">🤖</div>
            <p className="text-sm">Start chatting with AI</p>
          </div>
        )}

        {/* Messages */}
        {messages.map((m, i) => {
          const isUser = m.role === "user";

          return (
            <div
              key={i}
              className={`flex items-end gap-3 ${isUser ? "justify-end" : "justify-start"
                }`}
            >
              {/* Bot Icon */}
              {!isUser && (
                <div className="p-2.5 bg-purple-500/10 rounded-full">
                  <Cpu size="20" color="#a855f7" variant="Bold" />
                </div>
              )}

              {/* Message Bubble */}
              <div
                className={`px-5 py-3 rounded-2xl max-w-[70%] text-sm leading-relaxed shadow-sm transition
                ${isUser
                    ? "bg-gradient-to-r from-indigo-500 to-purple-500 text-white rounded-br-sm"
                    : "bg-white border border-slate-200 text-slate-800 rounded-bl-sm"
                  }`}
              >
                {m.content}
              </div>

              {/* User Icon */}
              {isUser && (
                <div className="p-2.5 bg-indigo-500/10 rounded-full">
                  <User size="20" color="#6366f1" variant="Bold" />
                </div>
              )}
            </div>
          );
        })}
      </div>

      {/* Input */}
      <form
        onSubmit={handleSubmit(onSubmit)}
        className="p-4 border-t border-slate-200 bg-white/80 backdrop-blur-xl"
      >
        <div className="flex items-center gap-3 bg-white rounded-2xl shadow-md px-3 py-2">

          <input
            {...register("message")}
            placeholder="Ask anything about property..."
            className="flex-1 px-3 py-2 outline-none text-sm text-slate-700 placeholder-slate-400"
          />

          <button
            className="flex items-center gap-2 px-4 py-2.5 bg-indigo-500 hover:bg-indigo-600 text-white rounded-xl shadow transition"
          >
            <IoIosSend />
            <span className="text-sm font-medium">Send</span>
          </button>
        </div>
      </form>
    </div>
  );
}