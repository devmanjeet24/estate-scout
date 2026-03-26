import PropertyCard from "./PropertyCard";
import { MdRealEstateAgent } from "react-icons/md";


export default function PropertyPanel({ properties }) {
  return (
    <div className="h-full flex flex-col">

      {/* Header */}
      <div className="px-4 py-4 border-b border-slate-200 bg-white/80 backdrop-blur flex flex-col gap-3">

        {/* Title */}
        <div className="flex items-center gap-2">
          <div className="p-2.5 bg-gradient-to-r from-pink-500 to-purple-500 text-white rounded-xl shadow">
            <MdRealEstateAgent />
          </div>

          <h2 className="text-sm font-semibold text-slate-800">
            Properties
          </h2>
        </div>

        {/* Search Box (UI only)
        <div className="flex items-center gap-2 bg-slate-100 rounded-xl px-3 py-2">
          <SearchNormal1 size="16" color="#64748b" />
          <input
            placeholder="Search location..."
            className="bg-transparent outline-none text-sm flex-1 text-slate-700 placeholder-slate-400"
          />
        </div> */}
      </div>

      {/* Content */}
      <div className="flex-1 overflow-y-auto p-4 space-y-4">

        {properties && properties.length > 0 ? (
          properties.map((property, index) => (
            <PropertyCard
              key={index}
              property={property}
              index={index}
            />
          ))
        ) : (
          <div className="flex flex-col items-center justify-center mt-24 text-slate-500">

            <div className="text-4xl mb-2">🏠</div>

            <p className="text-sm font-medium">
              No properties yet
            </p>

            <span className="text-xs text-slate-400">
              Try chatting to get results
            </span>
          </div>
        )}

      </div>
    </div>
  );
}