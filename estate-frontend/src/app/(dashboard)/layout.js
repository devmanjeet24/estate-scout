"use client";

import Sidebar from "@/components/Sidebar";

export default function DashboardLayout({ children }) {
  return (
    <div className="flex h-screen w-full bg-slate-100">

      {/* Sidebar */}
      <Sidebar />

      {/* Main Content */}
      <div className="flex-1 flex flex-col overflow-hidden">

        {/* Inner Content Wrapper */}
        <div className="flex-1 w-full overflow-auto">
          {children}
        </div>

      </div>
    </div>
  );
}