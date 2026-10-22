"""
Piotr Michalak helped me

MARS RESCUE: TELEMETRY BLACKOUT
Individual Python quest

STORY
The Mars rover has sent one final telemetry packet before losing contact.
Your mission is to analyse the data, decode the emergency beacon, and decide
whether the rover can continue operating.

RULES
- Work individually.
- Complete every TODO in order.
- Keep the data below unchanged.
- Use loops to calculate counts, totals, averages and maximums.
- Do not use sum(), min(), max() or list.count() for the required calculations.
- You may use variables, lists, strings, arithmetic, for, range(), len(), and if/elif/else.
- Run the script regularly and fix errors as you go.

Suggested time: 45-60 minutes + bonus mission.
"""

# ============================================================
# MISSION DATA — DO NOT CHANGE THESE VALUES
# ============================================================

battery_levels = [100, 96, 91, 87, 80, 74, 69, 63, 58, 51]
temperatures_c = [18, 19, 21, 24, 28, 31, 36, 39, 34, 29]
commands = ["MOVE", "MOVE", "SCAN", "MOVE", "DRILL", "SCAN", "MOVE", "TRANSMIT", "MOVE"]
beacon = "S.O.S - MARS 7"

print("=" * 55)
print("MARS RESCUE: TELEMETRY BLACKOUT")
print("=" * 55)

# ============================================================
# MISSION 1 — RECONNECT THE ROVER
# ============================================================

print("\n[MISSION 1] RECONNECTION COUNTDOWN")

# TODO 1: The stop value is -1, because range() excludes its stop value.
# This makes 0 appear in the countdown.
for i in range(30, -1, -5):
    print(i)


# ============================================================
# MISSION 2 — BATTERY FORENSICS
# ============================================================

print("\n[MISSION 2] BATTERY FORENSICS")

measurement_count = 0
starting_battery = 0
final_battery = 0
total_battery_used = 0

# TODO 2a: Count the measurements.
for b in battery_levels:
    measurement_count += 1

# TODO 2b: The first reading.
starting_battery = battery_levels[0]

# TODO 2c: The last reading, found with len() and an index.
final_battery = battery_levels[len(battery_levels) - 1]

# TODO 2d: Add up each drop between consecutive readings.
for i in range(1, len(battery_levels)):
    drop = battery_levels[i - 1] - battery_levels[i]
    total_battery_used += drop

print("Battery measurements:", measurement_count)
print("Starting battery:", starting_battery, "%")
print("Final battery:", final_battery, "%")
print("Total battery used:", total_battery_used, "percentage points")


# ============================================================
# MISSION 3 — TEMPERATURE ALERT
# ============================================================

print("\n[MISSION 3] TEMPERATURE ALERT")

temperature_total = 0
average_temperature = 0
hot_readings = 0
highest_temperature = temperatures_c[0]

# TODO 3: Total, count hot readings, and track the highest value.
for t in temperatures_c:
    temperature_total += t
    if t >= 35:
        hot_readings += 1
    if t > highest_temperature:
        highest_temperature = t

average_temperature = temperature_total / len(temperatures_c)

print("Average temperature:", average_temperature, "C")
print("Readings at or above 35 C:", hot_readings)
print("Highest temperature:", highest_temperature, "C")


# ============================================================
# MISSION 4 — COMMAND-CENTER AUDIT
# ============================================================

print("\n[MISSION 4] COMMAND-CENTER AUDIT")

move_count = 0
scan_count = 0
drill_count = 0
transmit_count = 0

# TODO 4: Count each command type.
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


# ============================================================
# MISSION 5 — DECODE THE EMERGENCY BEACON
# ============================================================

print("\n[MISSION 5] EMERGENCY BEACON")

decoded_beacon = ""

# TODO 5: Keep every character that is not a dot, space or dash.
for char in beacon:
    if char != "." and char != " " and char != "-":
        decoded_beacon += char

print("Decoded beacon:", decoded_beacon)


# ============================================================
# FINAL MISSION — CAN THE ROVER SURVIVE?
# ============================================================

print("\n[FINAL MISSION] ROVER STATUS")

mission_score = 0

# TODO 6a: Calculate the mission score.
mission_score = 100 - total_battery_used - (hot_readings * 5)

# TODO 6b: Decide the rover status.
if final_battery >= 50 and hot_readings < 3:
    print("ROVER STABLE")
else:
    print("EMERGENCY MODE")

print("Mission score:", mission_score)
print("Beacon code:", decoded_beacon)
print("Mission analysis complete.")


# ============================================================
# BONUS MISSION — FIND THE BIGGEST BATTERY DROP
# ============================================================

print("\n[BONUS MISSION] BIGGEST BATTERY DROP")

largest_drop = 0
reading_before_drop = 0
reading_after_drop = 0

# TODO BONUS: Track the largest drop and the readings it falls between.
# Readings are numbered from 1, so the pair at indexes i-1 and i
# is readings i and i + 1.
for i in range(1, len(battery_levels)):
    drop = battery_levels[i - 1] - battery_levels[i]
    if drop > largest_drop:
        largest_drop = drop
        reading_before_drop = i
        reading_after_drop = i + 1

print("Largest drop:", largest_drop, "points")
print("Between readings:", reading_before_drop, "and", reading_after_drop)
