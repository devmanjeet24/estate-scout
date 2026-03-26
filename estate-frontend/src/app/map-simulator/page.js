"use client";

import { useState } from "react";
import { FaSearchLocation } from "react-icons/fa";

export default function MapSimulator() {
  const [image, setImage] = useState(null);

  const handleSearch = () => {
    const random = Math.floor(Math.random() * 5) + 1;
    setImage(`/street/street${random}.jpg`);
  };

  return (
    <div className="h-full flex items-center justify-center p-6">

      {/* Card */}
      <div className="w-full max-w-xl bg-white/70 backdrop-blur-xl rounded-3xl shadow-xl border border-white/40 p-6 flex flex-col gap-5">

        {/* Header */}
        <div className="text-center">
          <h2 className="text-xl font-semibold text-gray-800">
            Street View Finder 🗺️
          </h2>
          <p className="text-sm text-gray-500">
            Enter any address to preview location
          </p>
        </div>

        {/* Search Box */}
        <div className="flex gap-2">
          
          <div className="relative flex-1">
            <input
              id="search-box"
              placeholder="Enter address..."
              className="w-full pl-4 pr-3 py-3 rounded-xl bg-gray-100 text-gray-800 placeholder-gray-400 focus:bg-white border border-transparent focus:border-green-400 outline-none transition text-sm"
            />
          </div>

          <button
            id="search-btn"
            onClick={handleSearch}
            className="flex items-center gap-2 px-4 py-3 bg-green-500 hover:bg-green-600 text-white rounded-xl shadow-md transition-all duration-200 hover:scale-[1.05] active:scale-[0.95]"
          >
            <FaSearchLocation />
            Search
          </button>
        </div>

        {/* Image */}
        {image && (
          <div className="w-full h-[260px] rounded-2xl overflow-hidden shadow-lg border border-gray-200 animate-fade-in">
            <img
              id="street-view-image"
              src={image}
              alt="street"
              className="w-full h-full object-cover transition-transform duration-300 hover:scale-105"
            />
          </div>
        )}

      </div>
    </div>
  );
}