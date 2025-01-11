#  madakixo
## PaintCalculator class with type hinting, static methods, 
## and comprehensive docstrings:

from typing import List, Dict, Union

class PaintCalculator:
    """
    A class to calculate the amount of paint required for painting different rooms in a building.
    This calculator takes into account the dimensions of rooms, windows, doors, and the type of paint used.
    """

    def __init__(self):
        """
        Initialize the PaintCalculator with predefined paint coverage rates for different types of paint.
        """
        # Paint coverage rates per 100 m² for different types of paint for 3 coats
        self.coverage_rates: Dict[str, float] = {
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

    def calculate_paint_requirement(self, room_name: str, perimeter: float, height: float, window_areas: List[float], door_areas: List[float], paint_type: str) -> float:
        """
        Calculate the amount of paint required for a given room.

        Args:
            room_name (str): The name of the room being calculated.
            perimeter (float): The perimeter of the room in meters.
            height (float): The height of the room in meters.
            window_areas (List[float]): A list of areas for each window in the room in square meters.
            door_areas (List[float]): A list of areas for each door in the room in square meters.
            paint_type (str): The type of paint to be used.

        Returns:
            float: The amount of paint required in liters.

        Raises:
            ValueError: If the calculated net wall area is negative or if any dimension is non-positive.
            KeyError: If the specified paint type is not found in the coverage rates dictionary.
            ZeroDivisionError: If division by zero is attempted (e.g., no wall area to paint).
            Exception: For any other unexpected errors during calculation.
        """
        try:
            # Calculate the total wall area
            total_wall_area = perimeter * height
            
            # Subtract the areas of windows and doors
            net_wall_area = total_wall_area - sum(window_areas) - sum(door_areas)
            
            # Check for negative area
            if net_wall_area < 0:
                raise ValueError("Net wall area cannot be negative. Check your dimensions.")
            
            # Get the coverage for the chosen paint type
            coverage_per_100m2: Union[float, None] = self.coverage_rates.get(paint_type, None)
            if coverage_per_100m2 is None:
                raise KeyError(f"Paint type {paint_type} not found in the database.")
            
            # Calculate the paint needed, avoid division by zero
            if net_wall_area == 0:
                return 0
            paint_needed: float = (net_wall_area * coverage_per_100m2) / 100
            
            return paint_needed
        except ZeroDivisionError:
            print("Error: Division by zero occurred. Check your dimensions.")
            return 0
        except ValueError as ve:
            print(f"Error: {ve}")
            return 0
        except KeyError as ke:
            print(f"Error: {ke}")
            return 0
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return 0

    @staticmethod
    def get_float_input(prompt: str, default: Union[float, None] = None) -> float:
        """
        Get a float input from the user with an optional default value.

        Args:
            prompt (str): The prompt to display to the user.
            default (Union[float, None]): The default value to return if no input is provided.

        Returns:
            float: The float value entered by the user or the default value.

        Raises:
            ValueError: If the input cannot be converted to a float.
        """
        while True:
            try:
                user_input = input(prompt)
                if not user_input and default is not None:
                    return default
                return float(user_input)
            except ValueError:
                print("Please enter a valid number.")

    @staticmethod
    def get_int_input(prompt: str, default: Union[int, None] = None) -> int:
        """
        Get an integer input from the user with an optional default value.

        Args:
            prompt (str): The prompt to display to the user.
            default (Union[int, None]): The default value to return if no input is provided.

        Returns:
            int: The integer value entered by the user or the default value.

        Raises:
            ValueError: If the input cannot be converted to an integer or if it's negative.
        """
        while True:
            try:
                user_input = input(prompt)
                if not user_input and default is not None:
                    return default
                result = int(user_input)
                if result < 0:
                    raise ValueError("Number of windows or doors cannot be negative.")
                return result
            except ValueError as ve:
                print(f"Error: {ve}")

    def run_calculator(self) -> None:
        """
        Run the paint requirement calculator for each predefined room.

        This method guides the user through entering details for each room in the building,
        calculates the paint requirement, and displays the result. It uses default values for
        typical room configurations and handles errors for invalid inputs.
        """
        rooms: List[str] = ['Parlour', 'Bedroom', 'Toilet', 'Kitchen']
        for room in rooms:
            print(f"\n--- {room} Details ---")
            try:
                # Default values based on typical room dimensions and features
                perimeter: float = PaintCalculator.get_float_input(f"Enter the perimeter of the {room} in meters (default {('15.3' if room == 'Parlour' else '12.9' if room == 'Bedroom' else '6' if room == 'Toilet' else '6.6')}m): ", 
                                       15.3 if room == 'Parlour' else 12.9 if room == 'Bedroom' else 6 if room == 'Toilet' else 6.6)
                if perimeter <= 0:
                    raise ValueError("Perimeter must be positive.")
                
                height: float = PaintCalculator.get_float_input(f"Enter the height of the {room} in meters (default 3m): ", 3)
                if height <= 0:
                    raise ValueError("Height must be positive.")
                
                num_windows: int = PaintCalculator.get_int_input(f"Enter the number of windows in the {room} (default {('2' if room == 'Parlour' else '1' if room == 'Bedroom' else '1' if room == 'Toilet' else '1')}): ", 
                                       2 if room == 'Parlour' else 1)
                window_areas: List[float] = []
                for i in range(num_windows):
                    w_length: float = PaintCalculator.get_float_input(f"Enter the length of window {i+1} in meters (default {('1' if room == 'Parlour' or room == 'Bedroom' else '0.6')}m): ", 
                                                  1 if room == 'Parlour' or room == 'Bedroom' else 0.6)
                    if w_length <= 0:
                        raise ValueError("Window length must be positive.")
                    w_height: float = PaintCalculator.get_float_input(f"Enter the height of window {i+1} in meters (default {('1.2' if room == 'Parlour' or room == 'Bedroom' else '0.6')}m): ", 
                                                  1.2 if room == 'Parlour' or room == 'Bedroom' else 0.6)
                    if w_height <= 0:
                        raise ValueError("Window height must be positive.")
                    window_areas.append(w_length * w_height)
                
                num_doors: int = PaintCalculator.get_int_input(f"Enter the number of doors in the {room} (default {('2' if room == 'Parlour' or room == 'Bedroom' else '1')}): ", 
                                     2 if room == 'Parlour' or room == 'Bedroom' else 1)
                door_areas: List[float] = []
                for i in range(num_doors):
                    d_length: float = PaintCalculator.get_float_input(f"Enter the length of door {i+1} in meters (default {('0.9' if room == 'Parlour' or room == 'Bedroom' else '0.75')}m): ", 
                                                  0.9 if room == 'Parlour' or room == 'Bedroom' else 0.75)
                    if d_length <= 0:
                        raise ValueError("Door length must be positive.")
                    d_height: float = PaintCalculator.get_float_input(f"Enter the height of door {i+1} in meters (default 2.1m): ", 2.1)
                    if d_height <= 0:
                        raise ValueError("Door height must be positive.")
                    door_areas.append(d_length * d_height)
                
                print("\nAvailable paint types:")
                for paint_type in self.coverage_rates.keys():
                    print(f"- {paint_type}")
                paint_type: str = input(f"Enter the type of paint for the {room} (default 'Emulsion paint'): ") or 'Emulsion paint'
                
                # Calculate paint requirement
                paint_litres: float = self.calculate_paint_requirement(room, perimeter, height, window_areas, door_areas, paint_type)
                print(f"Total paint required for {room}: {paint_litres:.2f} liters")
            except ValueError as ve:
                print(f"Error in {room} details: {ve}")
            except Exception as e:
                print(f"An unexpected error occurred in {room} details: {e}")

if __name__ == "__main__":
    calculator: PaintCalculator = PaintCalculator()
    calculator.run_calculator()
