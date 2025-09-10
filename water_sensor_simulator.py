import time
import random

def read_water_level():
    # Simulate water level sensor readings (in meters)
    return round(random.uniform(0.5, 3.5), 2)

print("Starting IoT water sensor simulation...")
while True:
    water_level = read_water_level()
    print(f"Current water level: {water_level} m")
    if water_level > 2.5:
        print("⚠️ ALERT: High water level detected!")
    time.sleep(5)  # simulate delay between readings
