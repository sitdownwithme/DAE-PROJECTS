import random
import os
import sys
from datetime import datetime
from typing import Dict, List

class LacrosseShoeCustomizer:
    def __init__(self):
        self.name: str = ""
        self.customer_type: str = ""
        self.color: str = ""
        self.size: float = 0.0
        self.traction: str = ""
        self.support: str = ""
        self.design: str = ""
        self.base_cost: float = 100.0
        self.discount: float = 0.0
        self.final_price: float = 0.0
        self.discount_reason: str = ""

        self.TRACTION_TYPES = ["Turf", "Grass", "All-Terrain"]
        self.SUPPORT_LEVELS = ["Low", "Mid", "High"]
        self.DESIGNS = ["Classic TA", "Modern TA", "Bold TA", "Minimal TA"]
        self.MIN_SIZE = 5.0
        self.MAX_SIZE = 15.0

    def display_menu_items(self, items: List[str], title: str):
        print(f"\n{title}")
        print("=" * 30)
        for i, item in enumerate(items, 1):
            print(f"{i}. {item}")

    def calculate_tax(self, price: float, tax_rate: float = 0.08) -> float:
        return round(price * tax_rate, 2)

    def get_user_input(self):
        self.name = input("Enter your name: ").strip()

        customer_types = ["High School", "College", "Youth Club"]
        self.display_menu_items(customer_types, "Choose Customer Type")
        try:
            choice = int(input("Choose a number: ")) - 1
            if 0 <= choice < len(customer_types):
                self.customer_type = customer_types[choice]
            else:
                print("Invalid choice. Defaulting to High School.")
                self.customer_type = "High School"
        except ValueError:
            print("Invalid input. Defaulting to High School.")
            self.customer_type = "High School"

        seasons = ["Spring", "Summer", "Fall", "Winter"]
        seasonal_collections = (
            ["Spring Green", "Fresh Blue", "Sunrise Yellow", "Lavender Bloom"],
            ["Ocean Blue", "Sandy Beige", "Coral Pink", "Sunset Orange"],
            ["Autumn Red", "Golden Brown", "Forest Green", "Harvest Gold"],
            ["Winter White", "Ice Blue", "Charcoal Gray", "Frost Silver"]
        )

        self.display_menu_items(seasons, "Choose a Season for Your Shoe Colors")
        try:
            season_choice = int(input("Choose a number: ")) - 1
            if 0 <= season_choice < len(seasons):
                season_colors = seasonal_collections[season_choice]
            else:
                print("Invalid choice. Using Spring colors.")
                season_colors = seasonal_collections[0]
        except ValueError:
            print("Invalid input. Using Spring colors.")
            season_colors = seasonal_collections[0]

        self.display_menu_items(season_colors, "Choose a Color from the Seasonal Collection")
        try:
            color_choice = int(input("Choose a number: ")) - 1
            if 0 <= color_choice < len(season_colors):
                self.color = season_colors[color_choice]
            else:
                print("Invalid choice. Setting to first seasonal color.")
                self.color = season_colors[0]
        except ValueError:
            print("Invalid input. Setting to first seasonal color.")
            self.color = season_colors[0]

        try:
            self.size = float(input(f"Enter your shoe size ({self.MIN_SIZE}-{self.MAX_SIZE}): "))
            if not (self.MIN_SIZE <= self.size <= self.MAX_SIZE):
                print("Size out of range. Setting to default size 10.")
                self.size = 10.0
        except ValueError:
            print("Invalid size. Setting to default size 10.")
            self.size = 10.0

        self.display_menu_items(self.TRACTION_TYPES, "Choose Traction Type")
        try:
            choice = int(input("Choose a number: ")) - 1
            if 0 <= choice < len(self.TRACTION_TYPES):
                self.traction = self.TRACTION_TYPES[choice]
            else:
                print("Invalid choice. Setting to Turf.")
                self.traction = "Turf"
        except ValueError:
            print("Invalid input. Setting to Turf.")
            self.traction = "Turf"

        self.display_menu_items(self.SUPPORT_LEVELS, "Choose Support Level")
        try:
            choice = int(input("Choose a number: ")) - 1
            if 0 <= choice < len(self.SUPPORT_LEVELS):
                self.support = self.SUPPORT_LEVELS[choice]
            else:
                print("Invalid choice. Setting to Mid.")
                self.support = "Mid"
        except ValueError:
            print("Invalid input. Setting to Mid.")
            self.support = "Mid"

        choice = input("Add TA design? (yes/no): ").lower()
        if choice in ["yes", "y"]:
            self.display_menu_items(self.DESIGNS, "Choose a Design")
            try:
                design_choice = int(input("Choose a number: ")) - 1
                if 0 <= design_choice < len(self.DESIGNS):
                    self.design = self.DESIGNS[design_choice]
                else:
                    print("Invalid choice. Setting to Classic TA.")
                    self.design = "Classic TA"
            except ValueError:
                print("Invalid input. Setting to Classic TA.")
                self.design = "Classic TA"
        else:
            self.design = "No design"

    def calculate_final_price(self):
        addon = 20 if self.support == "High" else 10 if self.support == "Mid" else 0
        self.base_cost = 100 + addon
        discount_options = [(5, "Welcome"), (10, "Lucky Day"), (15, "Cross-Platform"), (0, "No Discount")]
        self.discount, self.discount_reason = random.choice(discount_options)
        subtotal = self.base_cost * (1 - self.discount / 100)
        tax = self.calculate_tax(subtotal)
        self.final_price = round(subtotal + tax, 2)

    def display_summary(self):
        print("\n✅ Order Summary ✅")
        print(f"Name: {self.name}")
        print(f"Customer Type: {self.customer_type}")
        print(f"Color: {self.color}")
        print(f"Size: {self.size}")
        print(f"Traction: {self.traction}")
        print(f"Support: {self.support}")
        print(f"Design: {self.design}")
        print(f"Discount Applied: {self.discount}% ({self.discount_reason})")
        print(f"Final Price: ${self.final_price:.2f}")


def main():
    app = LacrosseShoeCustomizer()
    app.get_user_input()
    app.calculate_final_price()
    app.display_summary()

if __name__ == "__main__":
    main()
