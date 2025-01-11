def calculate_paint_requirement(room_name, perimeter, height, window_areas, door_areas, paint_type):
    """
    Calculates the total amount of paint needed for a room, taking into account windows and doors.

    Args:
        room_name (str): Name of the room.
        perimeter (float): The perimeter of the room in meters.
        height (float): The height of the room in meters.
        window_areas (list of float): List of individual window areas in square meters.
        door_areas (list of float): List of individual door areas in square meters.
        paint_type (str): The type of paint to be used (e.g., 'Emulsion paint').

    Returns:
        float: The total amount of paint needed in liters for 3 coats of paint, or 0 if the paint type is not found.
    """
    # Calculate the total wall area by multiplying the perimeter by the height
    total_wall_area = perimeter * height
    
    # Calculate the net wall area by subtracting the total area of the windows and doors
    net_wall_area = total_wall_area - sum(window_areas) - sum(door_areas)
    
    # Define a dictionary to store the coverage rate for each paint type, for three coats. 
    # The values are in liters per 100 square meters as per the provided problem description.
    coverage_rates = {
        'Alkaline resisting primer to lime plaster': 9 * 3,
        'Alkaline resisting primer to brick/block work': 13 * 3,
        'Wood primer': 9 * 3,
        'Metal primer': 6.25 * 3,
        'Undercoat': 7 * 3,
        'Gloss paint': 8 * 3,
        'Eggshell paint': 7 * 3,
        'Emulsion paint': 7 + 6.65 + 6.3,  # Special case - sum of three coats of emulsion as per description
        'Bituminous paint': 10 * 3,
        'Sandtex-Matt': 21 * 3,
        'Staining': 7 * 3,
        'Synthetic Varnish': 5.5 * 3,
        'Aluminum': 6 * 3
    }
    
    # Attempt to get the coverage for the provided paint type from our coverage_rates dictionary.
    #The get method is used to provide a default of None in case the key does not exist.
    coverage_per_100m2 = coverage_rates.get(paint_type, None)
    
    # Check to see if a coverage rate was found for the given paint type.
    if coverage_per_100m2 is None:
        print(f"Paint type {paint_type} not found in the database.")
        return 0 #Return 0 if the coverage type was not found.

    # Calculate the total paint needed (in liters) by multiplying the net area with coverage per 100 m2.
    #This also divides by 100 to take into account that the coverage is in m^2 /100m^2
    paint_needed = (net_wall_area * coverage_per_100m2) / 100
    
    return paint_needed # Return the paint_needed calculation

def main():
    """
    Gets user input for various rooms, calculates the amount of paint needed, and then reports this back to the user.
    """
    # List of rooms to calculate paint needed for.
    rooms = ['Parlour', 'Bedroom', 'Toilet', 'Kitchen']
    
    # Loops through the rooms, prompting for user input and then calculating the paint needed.
    for room in rooms:
        print(f"\nEnter details for {room}:") # User prompt for the current room
        
        # Prompt user for the perimeter of the room and convert the input to a float
        perimeter = float(input(f"Enter the perimeter of the {room} in meters: "))
        
        # Prompt user for the height of the room and convert the input to a float
        height = float(input(f"Enter the height of the {room} in meters: "))
        
        # Prompt user for the number of windows, convert to int and store the value
        num_windows = int(input(f"Enter the number of windows in the {room}: "))
        
        # Creates an empty list to store window areas.
        window_areas = []
        # Iterate through the range of values, prompting the user for the height and length of each window
        for i in range(num_windows):
            w_length = float(input(f"Enter the length of window {i+1} in meters: "))
            w_height = float(input(f"Enter the height of window {i+1} in meters: "))
             # Calculate the window area, append it to the window_areas list
            window_areas.append(w_length * w_height)
        
        # Prompt user for the number of doors, convert the input to an int, and store it.
        num_doors = int(input(f"Enter the number of doors in the {room}: "))
        
        # Creates an empty list to store the door areas.
        door_areas = []
         # Iterate through the range of values, prompting the user for the height and length of each door
        for i in range(num_doors):
            d_length = float(input(f"Enter the length of door {i+1} in meters: "))
            d_height = float(input(f"Enter the height of door {i+1} in meters: "))
           # Calculate the door area and append it to the door_areas list
            door_areas.append(d_length * d_height)
        
        # Prompt the user for the paint type for the room
        paint_type = input(f"Enter the type of paint for the {room}: ")
        
        # Calls the calculate_paint_requirement method to get the paint needed for the provided room details
        paint_litres = calculate_paint_requirement(room, perimeter, height, window_areas, door_areas, paint_type)
        
        # Output the total paint required for the room to the console, formatted to two decimal places.
        print(f"Total paint required for {room}: {paint_litres:.2f} liters")

# This ensures that the main function is only called if the script is called as the main script rather than imported.
if __name__ == "__main__":
    main()
