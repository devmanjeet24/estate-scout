"use client";

import { useEffect, useState } from "react";
import { getHistory } from "@/lib/api";
import { User, Cpu } from "iconsax-react";

export default function History() {
  const [data, setData] = useState([]);

  useEffect(() => {
    load();
  }, []);

  const load = async () => {
    const res = await getHistory();
    setData(res.data.messages || []);
  };

  return (
    <div className="h-full overflow-y-auto px-6 py-6 bg-gradient-to-br from-indigo-50 via-purple-50 to-pink-50">

      {/* Title */}
      <h1 className="text-xl font-semibold text-slate-800 mb-4">
        Chat History
      </h1>

      {/* Empty */}
      {data.length === 0 && (
        <div className="flex flex-col items-center justify-center mt-24 text-slate-500">
          <div className="text-4xl mb-2">🕓</div>
          <p className="text-sm">No history yett</p>
        </div>
      )}

      {/* List */}
      <div className="flex flex-col gap-4">
        {data.map((m, i) => {
          const isUser = i % 2 === 0;

          return (
            <div
              key={i}
              className="flex items-start gap-3 bg-white/80 backdrop-blur border border-white/40 shadow-md rounded-2xl p-4"
            >
              {/* Icon */}
              <div
                className={`p-2.5 rounded-xl ${
                  isUser
                    ? "bg-indigo-500/10"
                    : "bg-purple-500/10"
                }`}
              >
                {isUser ? (
                  <User size="20" color="#6366f1" variant="Bold" />
                ) : (
                  <Cpu size="20" color="#a855f7" variant="Bold" />
                )}
              </div>

              {/* Content */}
              <div className="flex-1">
                <p className="text-sm text-slate-700 leading-relaxed">
                  {m.content}
                </p>

                {/* Meta (optional future) */}
                <span className="text-xs text-slate-400 mt-1 block">
                  {isUser ? "You" : "AI"}
                </span>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}