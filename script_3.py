#updated script with default values 

def calculate_paint_requirement(room_name, perimeter, height, window_areas, door_areas, paint_type):
    # Calculate the total wall area
    total_wall_area = perimeter * height
    
    # Subtract the areas of windows and doors
    net_wall_area = total_wall_area - sum(window_areas) - sum(door_areas)
    
    # Paint coverage rates per 100 m² for different types of paint for 3 coats
    coverage_rates = {
        'Alkaline resisting primer to lime plaster': 9 * 3,
        'Alkaline resisting primer to brick/block work': 13 * 3,
        'Wood primer': 9 * 3,
        'Metal primer': 6.25 * 3,
        'Undercoat': 7 * 3,
        'Gloss paint': 8 * 3,
        'Eggshell paint': 7 * 3,
        'Emulsion paint': 7 + 6.65 + 6.3,  # Special case as provided in your description
        'Bituminous paint': 10 * 3,
        'Sandtex-Matt': 21 * 3,
        'Staining': 7 * 3,
        'Synthetic Varnish': 5.5 * 3,
        'Aluminum': 6 * 3
    }
    
    # Get the coverage for the chosen paint type
    coverage_per_100m2 = coverage_rates.get(paint_type, None)
    if coverage_per_100m2 is None:
        print(f"Paint type {paint_type} not found in the database.")
        return 0
    
    # Calculate the paint needed
    paint_needed = (net_wall_area * coverage_per_100m2) / 100
    
    return paint_needed

def get_float_input(prompt, default=None):
    while True:
        user_input = input(prompt)
        if not user_input and default is not None:
            return default
        try:
            return float(user_input)
        except ValueError:
            print("Please enter a valid number.")

def get_int_input(prompt, default=None):
    while True:
        user_input = input(prompt)
        if not user_input and default is not None:
            return default
        try:
            return int(user_input)
        except ValueError:
            print("Please enter a valid integer.")

def main():
    rooms = ['Parlour', 'Bedroom', 'Toilet', 'Kitchen']
    for room in rooms:
        print(f"\n--- {room} Details ---")
        # Default values based on typical room dimensions and features
        perimeter = get_float_input(f"Enter the perimeter of the {room} in meters (default {('15.3' if room == 'Parlour' else '12.9' if room == 'Bedroom' else '6' if room == 'Toilet' else '6.6')}m): ", 
                                   15.3 if room == 'Parlour' else 12.9 if room == 'Bedroom' else 6 if room == 'Toilet' else 6.6)
        height = get_float_input(f"Enter the height of the {room} in meters (default 3m): ", 3)
        
        num_windows = get_int_input(f"Enter the number of windows in the {room} (default {('2' if room == 'Parlour' else '1' if room == 'Bedroom' else '1' if room == 'Toilet' else '1')}): ", 
                                   2 if room == 'Parlour' else 1)
        window_areas = []
        for i in range(num_windows):
            w_length = get_float_input(f"Enter the length of window {i+1} in meters (default {('1' if room == 'Parlour' or room == 'Bedroom' else '0.6')}m): ", 
                                      1 if room == 'Parlour' or room == 'Bedroom' else 0.6)
            w_height = get_float_input(f"Enter the height of window {i+1} in meters (default {('1.2' if room == 'Parlour' or room == 'Bedroom' else '0.6')}m): ", 
                                      1.2 if room == 'Parlour' or room == 'Bedroom' else 0.6)
            window_areas.append(w_length * w_height)
        
        num_doors = get_int_input(f"Enter the number of doors in the {room} (default {('2' if room == 'Parlour' or room == 'Bedroom' else '1')}): ", 
                                 2 if room == 'Parlour' or room == 'Bedroom' else 1)
        door_areas = []
        for i in range(num_doors):
            d_length = get_float_input(f"Enter the length of door {i+1} in meters (default {('0.9' if room == 'Parlour' or room == 'Bedroom' else '0.75')}m): ", 
                                      0.9 if room == 'Parlour' or room == 'Bedroom' else 0.75)
            d_height = get_float_input(f"Enter the height of door {i+1} in meters (default 2.1m): ", 2.1)
            door_areas.append(d_length * d_height)
        
        print("\nAvailable paint types:")
        for paint_type in coverage_rates.keys():
            print(f"- {paint_type}")
        paint_type = input(f"Enter the type of paint for the {room} (default 'Emulsion paint'): ") or 'Emulsion paint'
        
        # Calculate paint requirement
        paint_litres = calculate_paint_requirement(room, perimeter, height, window_areas, door_areas, paint_type)
        print(f"Total paint required for {room}: {paint_litres:.2f} liters")

if __name__ == "__main__":
    main()
