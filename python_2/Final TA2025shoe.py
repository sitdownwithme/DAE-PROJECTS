import random
import os
import sys
from typing import Dict, List

class LacrosseShoeCustomizer:
    def __init__(self):
        """Initialize all customization options and settings."""
        self.name: str = ""
        self.color: str = ""
        self.size: float = 0.0
        self.traction: str = ""
        self.support: str = ""
        self.design: str = ""
        self.base_cost: float = 100.0
        self.discount: float = 0.0
        self.final_price: float = 0.0
        self.discount_reason: str = ""

        self.COLORS = ["Red", "Blue", "White", "Black"]
        self.TRACTION_TYPES = ["Turf", "Grass", "All-Terrain"]
        self.SUPPORT_LEVELS = ["Low", "Mid", "High"]
        self.DESIGNS = ["Classic TA", "Modern TA", "Bold TA", "Minimal TA"]
        self.MIN_SIZE = 5.0
        self.MAX_SIZE = 15.0

        self.settings = self.read_settings_file()

    def read_settings_file(self) -> Dict[str, any]:
        """Reads customization settings from a file."""
        settings = {"theme": "default", "save_auto": False}
        try:
            with open("settings.txt", "r") as file:
                for line in file:
                    if "=" in line:
                        key, value = line.strip().split("=", 1)
                        if value.lower() == "true":
                            value = True
                        elif value.lower() == "false":
                            value = False
                        settings[key.strip()] = value
        except Exception:
            print("Settings file not loaded. Defaults used.")
        return settings

    def clear_screen(self):
        """Clears the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_menu_items(self, items: List[str], title: str):
        """Displays numbered options for a selection menu."""
        print(f"\n{title}")
        print("=" * 30)
        for i, item in enumerate(items, 1):
            print(f"{i}. {item}")

    def calculate_tax(self, price: float, tax_rate: float = 0.08) -> float:
        """Returns tax based on price."""
        return round(price * tax_rate, 2)

    def get_user_input(self):
        """Collects all user input for customizing the shoe."""
        self.name = input("Enter your name: ").strip()
        
        # Color
        self.display_menu_items(self.COLORS, "Choose a Color")
        self.color = self.COLORS[int(input("Choose a number: ")) - 1]

        # Size
        self.size = float(input(f"Enter your shoe size ({self.MIN_SIZE}-{self.MAX_SIZE}): "))
        if not (self.MIN_SIZE <= self.size <= self.MAX_SIZE):
            print("Size out of range. Setting to default size 10.")
            self.size = 10.0

        # Traction
        self.display_menu_items(self.TRACTION_TYPES, "Choose Traction Type")
        self.traction = self.TRACTION_TYPES[int(input("Choose a number: ")) - 1]

        # Support
        self.display_menu_items(self.SUPPORT_LEVELS, "Choose Support Level")
        self.support = self.SUPPORT_LEVELS[int(input("Choose a number: ")) - 1]

        # Design
        choice = input("Add TA design? (yes/no): ").lower()
        if choice in ["yes", "y"]:
            self.display_menu_items(self.DESIGNS, "Choose a Design")
            self.design = self.DESIGNS[int(input("Choose a number: ")) - 1]
        else:
            self.design = "No design"

    def calculate_final_price(self):
        """Calculates final price after support addons, discount, and tax."""
        addon = 20 if self.support == "High" else 10 if self.support == "Mid" else 0
        self.base_cost = 100 + addon
        discount_options = [(5, "Welcome"), (10, "Lucky Day"), (0, "No Discount")]
        self.discount, self.discount_reason = random.choice(discount_options)
        subtotal = self.base_cost * (1 - self.discount / 100)
        tax = self.calculate_tax(subtotal)
        self.final_price = round(subtotal + tax, 2)

    def recommend_shoe(self):
        """Recommends a shoe type based on support and traction."""
        if self.support == "High" and self.traction == "All-Terrain":
            print("🏆 Recommended: ELITE PRO Model")
        elif self.support == "Mid":
            print("🏃 Recommended: MID RUNNER Model")
        else:
            print("⚡ Recommended: LIGHT SPEED Model")

    def display_summary(self):
        """Displays final shoe order summary."""
        print("\n✅ Order Summary ✅")
        print(f"Name: {self.name}")
        print(f"Color: {self.color}")
        print(f"Size: {self.size}")
        print(f"Traction: {self.traction}")
        print(f"Support: {self.support}")
        print(f"Design: {self.design}")
        print(f"Discount Applied: {self.discount}% ({self.discount_reason})")
        print(f"Final Price: ${self.final_price:.2f}")

    def write_order_to_file(self):
        """Saves the order summary to a text file."""
        try:
            with open("order_summary.txt", "w") as f:
                f.write("ORDER SUMMARY\n")
                f.write(f"Name: {self.name}\n")
                f.write(f"Color: {self.color}\n")
                f.write(f"Size: {self.size}\n")
                f.write(f"Traction: {self.traction}\n")
                f.write(f"Support: {self.support}\n")
                f.write(f"Design: {self.design}\n")
                f.write(f"Discount: {self.discount}% - {self.discount_reason}\n")
                f.write(f"Final Price: ${self.final_price:.2f}\n")
            print("📝 Order saved to file.")
        except Exception as e:
            print("❌ Error writing file:", e)

def main():
    customizer = LacrosseShoeCustomizer()
    customizer.clear_screen()
    print("🏁 Welcome to the Toddavery Lacrosse Shoe Customizer!")
    customizer.get_user_input()
    customizer.calculate_final_price()
    customizer.recommend_shoe()
    customizer.display_summary()
    customizer.write_order_to_file()

if __name__ == "__main__":
    main()
