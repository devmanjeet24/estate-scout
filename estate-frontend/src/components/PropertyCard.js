import { Location, Home2 } from "iconsax-react";

export default function PropertyCard({ property, index }) {
  const img = `/properties/apartment${(index % 6) + 1}.jpg`;
  const street = `/street/street${(index % 6) + 1}.jpg`;

  return (
    <div className="group bg-white/80 backdrop-blur border border-white/40 rounded-2xl shadow-md hover:shadow-xl transition-all duration-300 overflow-hidden">

      {/* Image */}
      <div className="relative overflow-hidden">
        <img
          src={img}
          alt="property"
          className="h-44 w-full object-cover transition-transform duration-300 group-hover:scale-105"
        />

        {/* Price Badge */}
        <div className="absolute top-3 left-3 bg-gradient-to-r from-indigo-500 to-purple-500 text-white text-xs px-3 py-1 rounded-full shadow-md">
          ₹ {property.price}
        </div>
      </div>

      {/* Content */}
      <div className="p-4 flex flex-col gap-2">

        {/* Title */}
        <h3 className="font-semibold text-slate-800 text-sm leading-snug flex items-center gap-2">
          <Home2 size="18" color="#6366f1" variant="Bold" />
          {property.title}
        </h3>

        {/* Address */}
        <p className="text-xs text-slate-500 flex items-center gap-1">
          <Location size="16" color="#ec4899" variant="Bold" />
          {property.address}
        </p>

        {/* Divider */}
        <div className="h-px bg-slate-200 my-1" />

        {/* Street Preview */}
        <div className="rounded-xl overflow-hidden border border-slate-200">
          <img
            src={street}
            alt="street"
            className="h-28 w-full object-cover transition-transform duration-300 group-hover:scale-105"
          />
        </div>

      </div>
    </div>
  );
}