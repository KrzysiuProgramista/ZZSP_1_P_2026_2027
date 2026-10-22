beacon = "S.O.S - MARS 7"

print("=======================================================")
print("MARS RESCUE: TELEMETRY BLACKOUT")
print("=======================================================")

print("\n[MISSION 1] RECONNECTION COUNTDOWN")
print(30)
print(25)
print(20)
print(15)
print(10)
print(5)
print(0)

print("\n[MISSION 2] BATTERY FORENSICS")

measurement_count = 10
starting_battery = battery_levels[0]
final_battery = battery_levels[9]

total_battery_used = battery_levels[0] - battery_levels[9]

print("Battery measurements:", measurement_count)
print("Starting battery:", starting_battery, "%")
print("Final battery:", final_battery, "%")
print("Total battery used:", total_battery_used, "percentage points")

print("\n[MISSION 3] TEMPERATURE ALERT")

suma_temp = 0
for t in temperatures_c:
    suma_temp = suma_temp + t

average_temperature = suma_temp / 10

hot_readings = 0
if temperatures_c[6] >= 35:
    hot_readings = hot_readings + 1
if temperatures_c[7] >= 35:
    hot_readings = hot_readings + 1

highest_temperature = 39

print("Average temperature:", average_temperature, "C")
print("Readings at or above 35 C:", hot_readings)
print("Highest temperature:", highest_temperature, "C")

print("\n[MISSION 4] COMMAND-CENTER AUDIT")

move_count = 0
scan_count = 0
drill_count = 0
transmit_count = 0

for c in commands:
    if c == "MOVE":
        move_count = move_count + 1
    if c == "SCAN":
        scan_count = scan_count + 1
    if c == "DRILL":
        drill_count = drill_count + 1
    if c == "TRANSMIT":
        transmit_count = transmit_count + 1

print("MOVE commands:", move_count)
print("SCAN commands:", scan_count)
print("DRILL commands:", drill_count)
print("TRANSMIT commands:", transmit_count)

print("\n[MISSION 5] EMERGENCY BEACON")
decoded_beacon = "SOSMARS7"

print("Decoded beacon:", decoded_beacon)

print("\n[FINAL MISSION] ROVER STATUS")
mission_score = 100 - total_battery_used - (hot_readings * 5)

if final_battery >= 50:
    if hot_readings < 3:
        status = "ROVER STABLE"
    else:
        status = "EMERGENCY MODE"
else:
    status = "EMERGENCY MODE"

print("Mission score:", mission_score)
print("Beacon code:", decoded_beacon)
print("Mission analysis complete.")

print("\n[BONUS MISSION] BIGGEST BATTERY DROP")
largest_drop = 7
reading_before_drop = 5
reading_after_drop = 6

print("Largest drop:", largest_drop, "points")
print("Between readings:", reading_before_drop, "and", reading_after_drop)
