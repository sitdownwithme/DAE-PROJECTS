"""
Lacrosse Shoe Customizer with Customer Type and Seasonal Collection

This program allows customers to customize lacrosse shoes based on their organizational type (High School,
College, Youth Club) and seasonal color preferences (Spring, Summer, Fall, Winter).

It demonstrates the use of:
- Lists for storing selectable attributes like traction types, support levels, seasonal color options
- Tuples to store fixed groupings of seasonal color lists
- User input and selection menus
- Conditional logic and random discount application
- Class organization with clear method responsibilities
- Revision loop for confirming user choices before order is finalized
"""

import random
import os
import sys
from datetime import datetime
from typing import Dict, List

class LacrosseShoeCustomizer:
    """
    Handles all customization inputs, pricing logic, and output summary
    for lacrosse shoes based on user preferences.
    """
    def __init__(self):
        """Initialize all customization fields and preset options."""
        self.name: str = ""  # Customer name
        self.customer_type: str = ""  # Type of customer (school/club/etc.)
        self.color: str = ""  # Shoe color
        self.size: float = 0.0  # Shoe size
        self.traction: str = ""  # Traction type
        self.support: str = ""  # Support level
        self.design: str = ""  # Optional design label
        self.base_cost: float = 100.0  # Base cost of the shoe
        self.discount: float = 0.0  # Discount percentage
        self.final_price: float = 0.0  # Final price after discount and tax
        self.discount_reason: str = ""  # Reason for discount

        # Preset selection options
        self.TRACTION_TYPES = ["Turf", "Grass", "All-Terrain"]
        self.SUPPORT_LEVELS = ["Low", "Mid", "High"]
        self.DESIGNS = ["Classic TA", "Modern TA", "Bold TA", "Minimal TA"]
        self.MIN_SIZE = 5.0  # Minimum valid shoe size
        self.MAX_SIZE = 15.0  # Maximum valid shoe size

    def display_menu_items(self, items: List[str], title: str):
        """Displays a numbered list of options for a given title."""
        print(f"\n{title}")
        print("=" * 30)
        for i, item in enumerate(items, 1):
            print(f"{i}. {item}")

    def calculate_tax(self, price: float, tax_rate: float = 0.08) -> float:
        """Calculates tax based on a default or provided tax rate."""
        return round(price * tax_rate, 2)

    def get_user_input(self):
        """
        Collects all required user input and confirms correctness before proceeding.
        Allows user to revise their selections before finalizing the order.
        """
        while True:
            # Ask for user name
            self.name = input("Enter your name: ").strip()

            # Choose customer type
            customer_types = ["High School", "College", "Youth Club"]
            self.display_menu_items(customer_types, "Choose Customer Type")
            try:
                choice = int(input("Choose a number: ")) - 1
                self.customer_type = customer_types[choice] if 0 <= choice < len(customer_types) else "High School"
            except ValueError:
                self.customer_type = "High School"

            # Choose season and corresponding color collection
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
                season_colors = seasonal_collections[season_choice] if 0 <= season_choice < len(seasons) else seasonal_collections[0]
            except ValueError:
                season_colors = seasonal_collections[0]

            # Choose color from selected season
            self.display_menu_items(season_colors, "Choose a Color from the Seasonal Collection")
            try:
                color_choice = int(input("Choose a number: ")) - 1
                self.color = season_colors[color_choice] if 0 <= color_choice < len(season_colors) else season_colors[0]
            except ValueError:
                self.color = season_colors[0]

            # Choose shoe size and validate
            try:
                self.size = float(input(f"Enter your shoe size ({self.MIN_SIZE}-{self.MAX_SIZE}): "))
                if not (self.MIN_SIZE <= self.size <= self.MAX_SIZE):
                    print("Size out of range. Setting to default size 10.")
                    self.size = 10.0
            except ValueError:
                print("Invalid size. Setting to default size 10.")
                self.size = 10.0

            # Choose traction type
            self.display_menu_items(self.TRACTION_TYPES, "Choose Traction Type")
            try:
                choice = int(input("Choose a number: ")) - 1
                self.traction = self.TRACTION_TYPES[choice] if 0 <= choice < len(self.TRACTION_TYPES) else "Turf"
            except ValueError:
                self.traction = "Turf"

            # Choose support level
            self.display_menu_items(self.SUPPORT_LEVELS, "Choose Support Level")
            try:
                choice = int(input("Choose a number: ")) - 1
                self.support = self.SUPPORT_LEVELS[choice] if 0 <= choice < len(self.SUPPORT_LEVELS) else "Mid"
            except ValueError:
                self.support = "Mid"

            # Choose optional design
            choice = input("Add TA design? (yes/no): ").lower()
            if choice in ["yes", "y"]:
                self.display_menu_items(self.DESIGNS, "Choose a Design")
                try:
                    design_choice = int(input("Choose a number: ")) - 1
                    self.design = self.DESIGNS[design_choice] if 0 <= design_choice < len(self.DESIGNS) else "Classic TA"
                except ValueError:
                    self.design = "Classic TA"
            else:
                self.design = "No design"

            # Display all current selections
            print("\n📋 Review Your Selections:")
            print(f"Name: {self.name}")
            print(f"Customer Type: {self.customer_type}")
            print(f"Color: {self.color}")
            print(f"Size: {self.size}")
            print(f"Traction: {self.traction}")
            print(f"Support: {self.support}")
            print(f"Design: {self.design}")

            # Ask if everything is correct
            confirm = input("\nAre all selections correct? (yes to continue / no to revise): ").strip().lower()
            if confirm in ["yes", "y"]:
                break
            else:
                print("\n🔁 Let's revise your selections.")

    def calculate_final_price(self):
        """
        Calculates shoe price based on support level and random discount.
        Applies fixed tax rate and updates final total.
        """
        # Add-on pricing based on support level
        addon = 20 if self.support == "High" else 10 if self.support == "Mid" else 0
        self.base_cost = 100 + addon

        # Random discount and reason
        discount_options = [(5, "Welcome"), (10, "Lucky Day"), (15, "Cross-Platform"), (0, "No Discount")]
        self.discount, self.discount_reason = random.choice(discount_options)

        # Price calculation
        subtotal = self.base_cost * (1 - self.discount / 100)
        tax = self.calculate_tax(subtotal)
        self.final_price = round(subtotal + tax, 2)

    def display_summary(self):
        """Displays a clean summary of all shoe customization details."""
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
    """Main entry point for the Lacrosse Customizer."""
    app = LacrosseShoeCustomizer()  # Create the app
    app.get_user_input()            # Collect input
    app.calculate_final_price()     # Calculate pricing
    app.display_summary()           # Display results

if __name__ == "__main__":
    main()
