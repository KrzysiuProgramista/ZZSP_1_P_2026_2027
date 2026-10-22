# Mars Rescue: Telemetry Blackout — Individual Quest

**Work mode:** individual, no pair programming  
**Time:** 45–60 minutes, plus bonus  
**Deliverable:** completed Python file saved as `mars_rescue_<your_name>.py`

## Your mission
The Mars rover is about to lose contact. Analyse its data, count commands, decode the emergency beacon, and decide whether the rover can continue operating.

## How to work
1. Open `Mars_Rescue_Individual_Starter.py` in your IDE.
2. Save a copy under your own filename before editing.
3. Complete TODOs in order. Run the script after each mission.
4. Do not change the supplied data.
5. Do not use `sum()`, `min()`, `max()` or `list.count()` for the required calculations. The goal is to practise loops.
6. At the end, make sure your program prints the mission report and commit/save your final version.

## Suggested grading (20 points + 4 bonus)
- Mission 1 — countdown with `range()`: 2 points
- Mission 2 — count measurements, identify first/last level, total battery consumption: 4 points
- Mission 3 — average, count critical temperatures, highest temperature: 4 points
- Mission 4 — command counters: 3 points
- Mission 5 — decode a string character by character: 3 points
- Final mission — score and rover status: 2 points
- Clear labels, sensible variable names and correct output: 2 points
- Bonus — find the largest battery drop and which readings it occurred between: up to 4 points

## Output checks (do not look until you have tried)
Your finished program should report:
- 10 battery measurements
- Starting battery: 100%; final battery: 51%
- Total battery used: 49 percentage points
- Average temperature: 27.9 C
- Readings at or above 35 C: 2
- Highest temperature: 39 C
- Commands: MOVE = 5, SCAN = 2, DRILL = 1, TRANSMIT = 1
- Decoded beacon: `SOSMARS7`
- Mission score: 41
- Rover status: `ROVER STABLE`
- Bonus: largest drop = 7 points; it first occurs between readings 4 and 5
