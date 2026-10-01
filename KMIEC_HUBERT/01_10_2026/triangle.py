try:
    sides = [float(input(f"Side {i+1}: ")) for i in range(3)]
    
    longest = max(sides)
    total_sum = sum(sides)
    
    if longest < (total_sum - longest):
        print("The sides can form a triangle.")
        
        distinct_counts = len(set(sides))
        
        types_map = {1: "equilateral", 2: "isosceles", 3: "scalene"}
        print(f"Type: {types_map[distinct_counts]}")
    else:
        print("The sides cannot form a triangle.")
        
except (ValueError, KeyError):
    print("Error processing data.")
