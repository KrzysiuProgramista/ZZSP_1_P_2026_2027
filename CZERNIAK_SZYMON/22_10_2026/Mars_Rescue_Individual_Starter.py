battery_levels = [100, 96, 91, 87, 80, 74, 69, 63, 58, 51]
temperatures_c = [18, 19, 21, 24, 28, 31, 36, 39, 34, 29]
commands = ["MOVE", "MOVE", "SCAN", "MOVE", "DRILL", "SCAN", "MOVE", "TRANSMIT", "MOVE"]
beacon = "S.O.S - MARS 7"

print("=" * 55)
print("MARS RESCUE: TELEMETRY BLACKOUT")
print("=" * 55)



print("\n[MISSION 1] RECONNECTION COUNTDOWN")

for seconds in range(30, -1, -5):
    print(seconds)



print("\n[MISSION 2] BATTERY FORENSICS")

measurement_count = 0
starting_battery = 0
final_battery = 0
total_battery_used = 0

for reading in battery_levels:
    measurement_count += 1

starting_battery = battery_levels[0]

final_battery = battery_levels[len(battery_levels) - 1]

for i in range(1, len(battery_levels)):
    drop = battery_levels[i - 1] - battery_levels[i]
    total_battery_used += drop

print("Battery measurements:", measurement_count)
print("Starting battery:", starting_battery, "%")
print("Final battery:", final_battery, "%")
print("Total battery used:", total_battery_used, "percentage points")



print("\n[MISSION 3] TEMPERATURE ALERT")

temperature_total = 0
average_temperature = 0
hot_readings = 0
highest_temperature = temperatures_c[0]

for temperature in temperatures_c:
    temperature_total += temperature

    if temperature >= 35:
        hot_readings += 1

    if temperature > highest_temperature:
        highest_temperature = temperature

average_temperature = temperature_total / len(temperatures_c)

print("Average temperature:", average_temperature, "C")
print("Readings at or above 35 C:", hot_readings)
print("Highest temperature:", highest_temperature, "C")



print("\n[MISSION 4] COMMAND-CENTER AUDIT")

move_count = 0
scan_count = 0
drill_count = 0
transmit_count = 0

for command in commands:
    if command == "MOVE":
        move_count += 1
    elif command == "SCAN":
        scan_count += 1
    elif command == "DRILL":
        drill_count += 1
    elif command == "TRANSMIT":
        transmit_count += 1

print("MOVE commands:", move_count)
print("SCAN commands:", scan_count)
print("DRILL commands:", drill_count)
print("TRANSMIT commands:", transmit_count)



print("\n[MISSION 5] EMERGENCY BEACON")

decoded_beacon = ""

for character in beacon:
    if character != "." and character != " " and character != "-":
        decoded_beacon += character

print("Decoded beacon:", decoded_beacon)



print("\n[FINAL MISSION] ROVER STATUS")

mission_score = 100 - total_battery_used - (hot_readings * 5)

if final_battery >= 50 and hot_readings < 3:
    print("ROVER STABLE")
else:
    print("EMERGENCY MODE")

print("Mission score:", mission_score)
print("Beacon code:", decoded_beacon)
print("Mission analysis complete.")



print("\n[BONUS MISSION] BIGGEST BATTERY DROP")

largest_drop = 0
reading_before_drop = 0
reading_after_drop = 0

for i in range(1, len(battery_levels)):
    drop = battery_levels[i - 1] - battery_levels[i]

    if drop > largest_drop:
        largest_drop = drop
        reading_before_drop = i
        reading_after_drop = i + 1

print("Largest drop:", largest_drop, "points")
print("Between readings:", reading_before_drop, "and", reading_after_drop)
