import folium

# Bandung coordinates
map_center = [-6.934469, 107.604953]
flood_map = folium.Map(location=map_center, zoom_start=12)

# Example flood risk areas (lat, lon, risk_level)
flood_zones = [
    (-6.975, 107.63, "High"),
    (-6.95, 107.60, "Medium"),
    (-6.90, 107.62, "Low"),
]

for lat, lon, risk in flood_zones:
    color = "red" if risk == "High" else "orange" if risk == "Medium" else "green"
    folium.CircleMarker(
        location=[lat, lon],
        radius=10,
        color=color,
        fill=True,
        fill_opacity=0.6,
        popup=f"Flood Risk: {risk}",
    ).add_to(flood_map)

# Save map
flood_map.save("bandung_flood_risk_map.html")
print("Flood risk map generated: bandung_flood_risk_map.html")
