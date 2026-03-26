import { create } from "zustand";
import { sendMessage } from "@/lib/api";

export const useChat = create((set) => ({
  messages: [],
  properties: [],

  send: async (text) => {
    const userMsg = { role: "user", content: text };

    set((state) => ({
      messages: [...state.messages, userMsg],
    }));

    try {
      const res = await sendMessage(text);

      set((state) => ({
        messages: [
          ...state.messages,
          { role: "assistant", content: res.data.reply },
        ],
        properties: res.data.properties || [],
      }));
    } catch {
      set((state) => ({
        messages: [
          ...state.messages,
          { role: "assistant", content: "Error occurred" },
        ],
      }));
    }
  },

  clearChat: () =>
    set({
      messages: [],
      properties: [],
    }),
}));