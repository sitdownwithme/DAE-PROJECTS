import random
import os

class LacrosseShoeCustomizer:
    def __init__(self):
        """Initialize customization settings."""
        self.name = ""
        self.color = ""
        self.size = 0.0
        self.traction = ""
        self.support = ""
        self.design = ""
        self.model_name = ""
        self.base_cost = 100
        self.discount = 0
        self.final_price = 0

        self.COLORS = ["Red", "Blue", "White", "Black"]
        self.TRACTIONS = ["Turf", "Grass", "All-Terrain"]
        self.SUPPORTS = ["Low", "Mid", "High"]
        self.DESIGNS = ["Classic TA", "Modern TA", "Bold TA", "Minimal TA"]

    def clear_screen(self):
        """Clear terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_menu(self, options, title):
        """Display options as numbered menu."""
        print(f"\n{title}")
        for idx, option in enumerate(options, 1):
            print(f"{idx}. {option}")

    def get_user_input(self):
        """Collect user customization input."""
        self.name = input("Enter your name: ")
        
        self.display_menu(self.COLORS, "Choose a Color")
        self.color = self.COLORS[int(input("Select a number: ")) - 1]

        self.size = float(input("Enter shoe size (5-15): "))
        if not 5 <= self.size <= 15:
            print("Invalid size. Defaulting to 10.")
            self.size = 10.0

        self.display_menu(self.TRACTIONS, "Choose Traction Type")
        self.traction = self.TRACTIONS[int(input("Select a number: ")) - 1]

        self.display_menu(self.SUPPORTS, "Choose Support Level")
        self.support = self.SUPPORTS[int(input("Select a number: ")) - 1]

        design_choice = input("Add TA Design? (yes/no): ").lower()
        if design_choice in ["yes", "y"]:
            self.display_menu(self.DESIGNS, "Choose a Design")
            self.design = self.DESIGNS[int(input("Select a number: ")) - 1]
        else:
            self.design = "No design"

    def calculate_final_price(self):
        """Calculate cost including support and discount."""
        support_addon = 0
        if self.support == "Mid":
            support_addon = 10
        elif self.support == "High":
            support_addon = 20

        self.base_cost += support_addon
        self.discount = random.choice([0, 5, 10])
        subtotal = self.base_cost * (1 - self.discount / 100)
        tax = round(subtotal * 0.08, 2)
        self.final_price = round(subtotal + tax, 2)

    def generate_model_name(self):
        """Create a speed-themed shoe model name based on choices."""
        # Traction prefix
        prefix = {
            "Turf": "Blaze",
            "Grass": "Rocket",
            "All-Terrain": "Phantom"
        }.get(self.traction, "Speed")

        # Support core
        core = {
            "Low": "Lite",
            "Mid": "Run",
            "High": "Elite"
        }.get(self.support, "Core")

        # Design suffix
        suffix = {
            "Classic TA": "Storm",
            "Modern TA": "Flash",
            "Bold TA": "Pulse",
            "Minimal TA": "Glide",
            "No design": "Core"
        }.get(self.design, "Core")

        self.model_name = f"{prefix} {suffix} {core}"

    def display_summary(self):
        """Show final shoe order and model name."""
        print("\n🔧 Customization Summary")
        print(f"Name: {self.name}")
        print(f"Color: {self.color}")
        print(f"Size: {self.size}")
        print(f"Traction: {self.traction}")
        print(f"Support: {self.support}")
        print(f"Design: {self.design}")
        print(f"🚀 Model Name: {self.model_name}")
        print(f"💵 Final Price: ${self.final_price:.2f} (Discount: {self.discount}%)")

    def write_to_file(self):
        """Save order details to a text file."""
        with open("speed_shoe_order.txt", "w") as f:
            f.write("CUSTOM LACROSSE SHOE ORDER\n")
            f.write(f"Name: {self.name}\n")
            f.write(f"Color: {self.color}\n")
            f.write(f"Size: {self.size}\n")
            f.write(f"Traction: {self.traction}\n")
            f.write(f"Support: {self.support}\n")
            f.write(f"Design: {self.design}\n")
            f.write(f"Model: {self.model_name}\n")
            f.write(f"Price: ${self.final_price:.2f}\n")
        print("📝 Order saved to 'speed_shoe_order.txt'.")

def main():
    customizer = LacrosseShoeCustomizer()
    customizer.clear_screen()
    print("⚡ Welcome to the Speed Shoe Customizer ⚡")
    customizer.get_user_input()
    customizer.calculate_final_price()
    customizer.generate_model_name()
    customizer.display_summary()
    customizer.write_to_file()

if __name__ == "__main__":
    main()
