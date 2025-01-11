#  madakixo
## get_float_input and get_int_input: Created a single get_input static method that 
## uses a type function to determine the input type.
from typing import List, Dict, Union

class PaintCalculator:
    """Calculates paint requirements for different rooms."""

    def __init__(self):
        """Initialize with predefined paint coverage rates."""
        self.coverage_rates: Dict[str, float] = {
            'Alkaline resisting primer to lime plaster': 27,
            'Alkaline resisting primer to brick/block work': 39,
            'Wood primer': 27,
            'Metal primer': 18.75,
            'Undercoat': 21,
            'Gloss paint': 24,
            'Eggshell paint': 21,
            'Emulsion paint': 20.95,
            'Bituminous paint': 30,
            'Sandtex-Matt': 63,
            'Staining': 21,
            'Synthetic Varnish': 16.5,
            'Aluminum': 18
        }

    def calculate_paint_requirement(self, room_name: str, perimeter: float, height: float, window_areas: List[float], door_areas: List[float], paint_type: str) -> float:
        """
        Calculate paint requirement for a room.

        Args:
            room_name: Room name.
            perimeter: Room perimeter in meters.
            height: Room height in meters.
            window_areas: List of window areas in sq.m.
            door_areas: List of door areas in sq.m.
            paint_type: Type of paint.

        Returns:
            float: Paint required in liters.

        Raises:
            ValueError, KeyError
        """
        try:
            net_wall_area = perimeter * height - sum(window_areas) - sum(door_areas)
            if net_wall_area < 0:
                raise ValueError("Net wall area cannot be negative.")
            coverage_per_100m2 = self.coverage_rates.get(paint_type)
            if coverage_per_100m2 is None:
                raise KeyError(f"Paint type {paint_type} not found.")
            return (net_wall_area * coverage_per_100m2) / 100 if net_wall_area > 0 else 0
        except (ValueError, KeyError) as e:
            print(f"Error: {e}")
            return 0

    @staticmethod
    def get_input(prompt: str, default: Union[float, int, None], type_func: type) -> Union[float, int]:
        """Get user input with default value, converting to specified type."""
        user_input = input(prompt)
        try:
            return default if not user_input else type_func(user_input)
        except ValueError:
            print(f"Please enter a valid {type_func.__name__}.")
            return PaintCalculator.get_input(prompt, default, type_func)

    def run_calculator(self) -> None:
        """Run paint requirement calculation for predefined rooms."""
        rooms = ['Parlour', 'Bedroom', 'Toilet', 'Kitchen']
        defaults = {
            'Parlour': (15.3, 12.9, 6, 6.6),
            'Bedroom': (12.9, 12.9, 6, 6.6),
            'Toilet': (6, 6, 6, 6.6),
            'Kitchen': (6.6, 6.6, 6, 6.6)
        }
        
        for room in rooms:
            print(f"\n--- {room} Details ---")
            try:
                perimeter = PaintCalculator.get_input(f"Enter the perimeter of the {room} in meters (default {defaults[room][0]}m): ", defaults[room][0], float)
                if perimeter <= 0:
                    raise ValueError("Perimeter must be positive.")
                height = PaintCalculator.get_input(f"Enter the height of the {room} in meters (default 3m): ", 3, float)
                if height <= 0:
                    raise ValueError("Height must be positive.")
                
                num_windows = PaintCalculator.get_input(f"Enter the number of windows in the {room} (default {('2' if room == 'Parlour' else '1')}): ", 2 if room == 'Parlour' else 1, int)
                window_areas = [PaintCalculator.get_input(f"Enter the length of window {i+1} in meters (default {('1' if room in ['Parlour', 'Bedroom'] else '0.6')}m): ", 1 if room in ['Parlour', 'Bedroom'] else 0.6, float) * 
                                PaintCalculator.get_input(f"Enter the height of window {i+1} in meters (default {('1.2' if room in ['Parlour', 'Bedroom'] else '0.6')}m): ", 1.2 if room in ['Parlour', 'Bedroom'] else 0.6, float) 
                                for i in range(num_windows)]
                
                num_doors = PaintCalculator.get_input(f"Enter the number of doors in the {room} (default {('2' if room in ['Parlour', 'Bedroom'] else '1')}): ", 2 if room in ['Parlour', 'Bedroom'] else 1, int)
                door_areas = [PaintCalculator.get_input(f"Enter the length of door {i+1} in meters (default {('0.9' if room in ['Parlour', 'Bedroom'] else '0.75')}m): ", 0.9 if room in ['Parlour', 'Bedroom'] else 0.75, float) * 
                              PaintCalculator.get_input(f"Enter the height of door {i+1} in meters (default 2.1m): ", 2.1, float) 
                              for i in range(num_doors)]
                
                print("\nAvailable paint types:")
                for paint_type in self.coverage_rates.keys():
                    print(f"- {paint_type}")
                paint_type = input(f"Enter the type of paint for the {room} (default 'Emulsion paint'): ") or 'Emulsion paint'
                
                paint_litres = self.calculate_paint_requirement(room, perimeter, height, window_areas, door_areas, paint_type)
                print(f"Total paint required for {room}: {paint_litres:.2f} liters")
            except ValueError as ve:
                print(f"Error in {room} details: {ve}")

if __name__ == "__main__":
    calculator = PaintCalculator()
    calculator.run_calculator()
