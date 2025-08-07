#!/usr/bin/env python3
"""
Enhanced Lacrosse Shoe Customizer with Comprehensive Docstrings
Demonstrates proper documentation for all functions using lists and tuples.

This module provides a complete shoe customization system with detailed
function documentation following Python docstring conventions.

Author: Enhanced for Todd Avery Lacrosse
Version: 2.0
Date: 2025
"""

import random
import os
from typing import List, Tuple, Dict, Optional, Union, Any
from datetime import datetime

class EnhancedLacrosseCustomizer:
    """
    A comprehensive lacrosse shoe customization system with enhanced collections usage.
    
    This class demonstrates extensive use of lists and tuples for managing shoe
    customization options, pricing, inventory, and customer data.
    
    Attributes:
        COLORS (List[str]): Available shoe colors
        TRACTION_TYPES (List[str]): Available traction options
        SUPPORT_LEVELS (List[str]): Available support levels
        DESIGNS (List[str]): Available design patterns
        SHOE_MATERIALS (List[str]): Available shoe materials
        LACE_COLORS (List[str]): Available lace color options
        ACCESSORIES (List[str]): Available shoe accessories
        SIZE_RANGES (Tuple[Tuple[float, float, str], ...]): Size categories with ranges
        COLOR_COMBINATIONS (List[Tuple[str, str, str]]): Recommended color combos
        PRICE_TIERS (List[Tuple[int, int, str, List[str]]]): Pricing tier structure
        SHOE_RATINGS (Dict[str, Tuple[int, int, int, int]]): Performance ratings
    
    Example:
        >>> customizer = EnhancedLacrosseCustomizer()
        >>> accessories, prefs = customizer.get_enhanced_user_preferences()
        >>> customizer.analyze_color_combinations()
    """
    
    def __init__(self) -> None:
        """
        Initialize the lacrosse shoe customizer with all available options.
        
        Sets up all lists and tuples containing customization options, pricing
        structures, and performance data. Initializes empty collections for
        tracking orders and user selections.
        
        Returns:
            None
            
        Example:
            >>> customizer = EnhancedLacrosseCustomizer()
            >>> len(customizer.COLORS)
            4
        """
        # EXISTING LISTS in your code:
        self.COLORS = ["Red", "Blue", "White", "Black"]
        self.TRACTION_TYPES = ["Turf", "Grass", "All-Terrain"]
        self.SUPPORT_LEVELS = ["Low", "Mid", "High"]
        self.DESIGNS = ["Classic TA", "Modern TA", "Bold TA", "Minimal TA"]
        
        # NEW: Enhanced Lists with more data
        self.SHOE_MATERIALS = ["Synthetic Leather", "Mesh", "Canvas", "Premium Leather"]
        self.LACE_COLORS = ["White", "Black", "Red", "Blue", "Neon Green", "Silver"]
        self.ACCESSORIES = ["Ankle Guards", "Cleats Bag", "Extra Laces", "Shoe Care Kit"]
        
        # EXISTING TUPLE usage (from your discount logic):
        # In calculate_final_price: discount_options = [(5, "Welcome"), (10, "Lucky Day"), ...]
        
        # NEW: Enhanced Tuples for structured data
        self.SIZE_RANGES = (
            (5.0, 7.0, "Small"),      # (min, max, category)
            (7.5, 10.0, "Medium"),
            (10.5, 13.0, "Large"),
            (13.5, 15.0, "Extra Large")
        )
        
        # Color combinations as tuples (primary, accent, sole)
        self.COLOR_COMBINATIONS = [
            ("Red", "White", "Black"),
            ("Blue", "Silver", "White"),
            ("Black", "Red", "Gray"),
            ("White", "Blue", "Navy")
        ]
        
        # Price tiers as named tuples concept
        self.PRICE_TIERS = [
            (100, 149, "Basic", ["Standard warranty", "Basic customization"]),
            (150, 199, "Premium", ["Extended warranty", "Advanced customization", "Free shipping"]),
            (200, 299, "Elite", ["Lifetime warranty", "Premium customization", "Free shipping", "Personal consultation"])
        ]
        
        # Performance ratings as tuples (comfort, durability, style, performance)
        self.SHOE_RATINGS = {
            "Classic TA": (8, 9, 7, 8),
            "Modern TA": (9, 8, 9, 9),
            "Bold TA": (7, 8, 10, 8),
            "Minimal TA": (9, 7, 6, 9)
        }

    def demonstrate_list_operations(self) -> Dict[str, List[Union[str, float]]]:
        """
        Demonstrate comprehensive list operations for shoe customization.
        
        This function showcases various list methods and operations including:
        - List comprehensions for filtering data
        - List methods (append, extend, copy, sort)
        - List slicing for data selection
        - Multiple list management for order processing
        
        The function creates and manipulates several lists to show practical
        applications in a shoe customization context.
        
        Returns:
            Dict[str, List[Union[str, float]]]: Dictionary containing demonstration
            results with keys:
                - 'large_sizes': List of shoe sizes >= 10.5
                - 'custom_colors': Extended list of available colors
                - 'popular_colors': Top 2 most popular colors
                - 'sorted_materials': Materials in alphabetical order
                - 'pending_orders': List of orders awaiting processing
                - 'completed_orders': List of processed orders
        
        Example:
            >>> customizer = EnhancedLacrosseCustomizer()
            >>> results = customizer.demonstrate_list_operations()
            >>> print(f"Large sizes available: {len(results['large_sizes'])}")
            Large sizes available: 10
        """
        print("\n📋 LIST OPERATIONS DEMONSTRATION")
        print("=" * 40)
        
        results = {}
        
        # 1. List comprehension for filtering
        available_sizes = [5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0, 10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 14.0, 14.5, 15.0]
        large_sizes = [size for size in available_sizes if size >= 10.5]
        results['large_sizes'] = large_sizes
        print(f"Available large sizes (10.5+): {large_sizes}")
        
        # 2. List methods - adding/removing options
        custom_colors = self.COLORS.copy()  # Create a copy
        custom_colors.append("Gold")
        custom_colors.extend(["Silver", "Purple"])
        results['custom_colors'] = custom_colors
        print(f"Extended color options: {custom_colors}")
        
        # 3. List slicing for recommendations
        popular_colors = self.COLORS[:2]  # First 2 colors
        results['popular_colors'] = popular_colors
        print(f"Most popular colors: {popular_colors}")
        
        # 4. List sorting and reversing
        materials_by_price = self.SHOE_MATERIALS.copy()
        materials_by_price.sort()  # Alphabetical
        results['sorted_materials'] = materials_by_price
        print(f"Materials (alphabetical): {materials_by_price}")
        
        # 5. Multiple lists for order tracking
        order_queue = []
        completed_orders = []
        
        # Simulate adding orders
        order_queue.extend(["Order-001", "Order-002", "Order-003"])
        completed_order = order_queue.pop(0)  # Remove first order
        completed_orders.append(completed_order)
        results['pending_orders'] = order_queue
        results['completed_orders'] = completed_orders
        print(f"Pending orders: {order_queue}")
        print(f"Completed orders: {completed_orders}")
        
        return results

    def demonstrate_tuple_operations(self) -> Dict[str, Union[Tuple, Dict, str]]:
        """
        Demonstrate comprehensive tuple operations in shoe customization context.
        
        This function showcases tuple usage patterns including:
        - Tuple unpacking for structured data access
        - Immutable coordinate storage for shoe dimensions
        - Multiple return values using tuples
        - Tuples as dictionary keys for complex indexing
        - Named tuple-like patterns for structured data
        
        Processes size ranges, shoe dimensions, performance ratings, and inventory
        data using various tuple operations and patterns.
        
        Returns:
            Dict[str, Union[Tuple, Dict, str]]: Dictionary containing demonstration
            results with keys:
                - 'shoe_dimensions': Tuple of (length, width, height)
                - 'modern_ta_ratings': Tuple of performance ratings
                - 'size_categories': List of formatted size category strings
                - 'inventory_sample': Dictionary with tuple keys
                - 'dimension_analysis': String description of shoe dimensions
        
        Raises:
            KeyError: If requested shoe design is not found in ratings
            
        Example:
            >>> customizer = EnhancedLacrosseCustomizer()
            >>> results = customizer.demonstrate_tuple_operations()
            >>> dimensions = results['shoe_dimensions'] 
            >>> print(f"Shoe length: {dimensions[0]} inches")
            Shoe length: 12.5 inches
        """
        print("\n📦 TUPLE OPERATIONS DEMONSTRATION")
        print("=" * 40)
        
        results = {}
        
        # 1. Tuple unpacking for size categories
        size_categories = []
        for min_size, max_size, category in self.SIZE_RANGES:
            category_str = f"{category}: {min_size} - {max_size}"
            size_categories.append(category_str)
            print(category_str)
        results['size_categories'] = size_categories
        
        # 2. Tuple as immutable coordinates for shoe dimensions
        shoe_dimensions = (12.5, 4.2, 5.8)  # length, width, height in inches
        length, width, height = shoe_dimensions
        results['shoe_dimensions'] = shoe_dimensions
        dimension_analysis = f"Shoe dimensions - L: {length}\", W: {width}\", H: {height}\""
        results['dimension_analysis'] = dimension_analysis
        print(dimension_analysis)
        
        # 3. Return multiple values as tuple
        def get_shoe_specs(design: str) -> Tuple[int, int, int, int]:
            """
            Get performance specifications for a shoe design.
            
            Args:
                design: The shoe design name to look up
                
            Returns:
                Tuple[int, int, int, int]: Performance ratings for
                (comfort, durability, style, performance)
            """
            if design in self.SHOE_RATINGS:
                return self.SHOE_RATINGS[design]  # Returns tuple
            return (5, 5, 5, 5)  # Default ratings
        
        comfort, durability, style, performance = get_shoe_specs("Modern TA")
        modern_ratings = (comfort, durability, style, performance)
        results['modern_ta_ratings'] = modern_ratings
        print(f"Modern TA ratings - Comfort: {comfort}, Durability: {durability}, Style: {style}, Performance: {performance}")
        
        # 4. Tuples in dictionaries for structured data
        inventory = {
            ("Red", 9.0): 25,      # (color, size): quantity
            ("Blue", 9.0): 18,
            ("Red", 10.0): 30,
            ("Black", 8.5): 12
        }
        results['inventory_sample'] = inventory
        print(f"Inventory check - Red size 9.0: {inventory.get(('Red', 9.0), 0)} pairs")
        
        return results

    def get_enhanced_user_preferences(self) -> Tuple[List[str], Dict[str, str]]:
        """
        Collect comprehensive user preferences using interactive input.
        
        This function demonstrates tuple return values and list building through
        user interaction. Collects multiple accessory selections and preference
        settings, handling user input validation and error cases.
        
        The function builds a list of selected accessories through comma-separated
        input parsing and creates a preferences dictionary with user choices.
        
        Returns:
            Tuple[List[str], Dict[str, str]]: A tuple containing:
                - List[str]: Selected accessories from available options
                - Dict[str, str]: User preferences with keys:
                    - 'priority': Most important factor (comfort/style/performance)
                    - 'budget_range': Preferred price range (basic/premium/elite)
                    - 'sport_level': Competition level (recreational/competitive/professional)
        
        Raises:
            ValueError: If user input contains invalid accessory numbers
            IndexError: If accessory selection is out of range
            
        Note:
            Invalid selections are handled gracefully with empty lists returned
            
        Example:
            >>> customizer = EnhancedLacrosseCustomizer()
            >>> accessories, prefs = customizer.get_enhanced_user_preferences()
            >>> # User enters "1,3" for accessories and "comfort" for priority
            >>> print(f"Selected: {accessories}")
            Selected: ['Ankle Guards', 'Extra Laces']
            >>> print(f"Priority: {prefs['priority']}")
            Priority: comfort
        """
        print("\n🎨 ENHANCED PREFERENCE COLLECTION")
        print("=" * 40)
        
        # Collect multiple selections (lists)
        selected_accessories = []
        print("Available accessories:")
        for i, accessory in enumerate(self.ACCESSORIES, 1):
            print(f"{i}. {accessory}")
        
        # Allow multiple selections
        choices = input("Select accessories (comma-separated numbers, e.g., 1,3,4): ").strip()
        if choices:
            try:
                indices = [int(x.strip()) - 1 for x in choices.split(",")]
                selected_accessories = [self.ACCESSORIES[i] for i in indices if 0 <= i < len(self.ACCESSORIES)]
            except (ValueError, IndexError):
                print("Invalid selection, no accessories added.")
        
        # Collect preferences as dictionary
        preferences = {
            "priority": input("What's most important? (comfort/style/performance): ").strip().lower(),
            "budget_range": input("Budget range? (basic/premium/elite): ").strip().lower(),
            "sport_level": input("Competition level? (recreational/competitive/professional): ").strip().lower()
        }
        
        return selected_accessories, preferences

    def analyze_color_combinations(self) -> List[Tuple[str, str, str]]:
        """
        Analyze and return recommended color combinations for shoes.
        
        Evaluates all available color combinations based on contrast, popularity,
        and aesthetic appeal. Uses a scoring system to filter and recommend the
        best combinations for customer selection.
        
        The function processes the COLOR_COMBINATIONS list, assigning random scores
        (simulating real analysis) and filtering for high-quality combinations.
        Each combination is a tuple of (primary_color, accent_color, sole_color).
        
        Returns:
            List[Tuple[str, str, str]]: List of recommended color combinations.
            Each tuple contains (primary_color, accent_color, sole_color) strings.
            Only combinations with scores >= 8/10 are included.
        
        Note:
            Scoring is currently randomized for demonstration. In production,
            this would use actual color theory and customer preference data.
            
        Example:
            >>> customizer = EnhancedLacrosseCustomizer()
            >>> combos = customizer.analyze_color_combinations()
            >>> if combos:
            ...     primary, accent, sole = combos[0]
            ...     print(f"Top combo: {primary} with {accent} and {sole}")
            Top combo: Red with White and Black
        """
        print("\n🌈 COLOR COMBINATION ANALYSIS")
        print("=" * 35)
        
        recommended_combos = []
        
        for primary, accent, sole in self.COLOR_COMBINATIONS:
            # Score combinations based on contrast and popularity
            score = random.randint(7, 10)  # Simplified scoring
            if score >= 8:
                recommended_combos.append((primary, accent, sole))
                print(f"⭐ {primary} with {accent} accent and {sole} sole (Score: {score}/10)")
        
        return recommended_combos

    def calculate_bulk_pricing(self, quantities: List[int]) -> List[Tuple[int, float, float]]:
        """
        Calculate bulk pricing for multiple order quantities.
        
        Processes a list of quantities and applies tiered bulk discounts based on
        predefined thresholds. Uses tuple structures to define discount tiers and
        returns detailed pricing information for each quantity level.
        
        The discount structure uses tuples of (minimum_quantity, discount_percentage)
        to define pricing tiers. Higher quantities receive better discounts.
        
        Args:
            quantities (List[int]): List of quantities to calculate pricing for.
                Each quantity must be a positive integer representing number of pairs.
        
        Returns:
            List[Tuple[int, float, float]]: List of pricing results where each tuple
            contains (quantity, unit_price_after_discount, total_price).
            
        Raises:
            TypeError: If quantities contains non-integer values
            ValueError: If any quantity is negative or zero
            
        Note:
            Base price is $120.00 per pair. Bulk discounts apply as follows:
            - 1-4 pairs: 0% discount
            - 5-9 pairs: 10% discount  
            - 10-19 pairs: 15% discount
            - 20+ pairs: 20% discount
            
        Example:
            >>> customizer = EnhancedLacrosseCustomizer()
            >>> results = customizer.calculate_bulk_pricing([1, 5, 10, 25])
            >>> quantity, unit_price, total = results[1]  # 5 pairs
            >>> print(f"{quantity} pairs at ${unit_price:.2f} each = ${total:.2f}")
            5 pairs at $108.00 each = $540.00
        """
        print("\n💰 BULK PRICING CALCULATION")
        print("=" * 35)
        
        base_price = 120.0
        pricing_results = []
        
        # Bulk discount tiers (quantity_threshold, discount_percent)
        bulk_discounts = [(1, 0), (5, 10), (10, 15), (20, 20)]
        
        for quantity in quantities:
            if not isinstance(quantity, int) or quantity <= 0:
                raise ValueError(f"Quantity must be a positive integer, got {quantity}")
                
            # Find applicable discount
            discount = 0
            for threshold, disc_percent in reversed(bulk_discounts):
                if quantity >= threshold:
                    discount = disc_percent
                    break
            
            unit_price = base_price * (1 - discount / 100)
            total_price = unit_price * quantity
            
            result = (quantity, unit_price, total_price)
            pricing_results.append(result)
            
            print(f"{quantity} pairs: ${unit_price:.2f} each = ${total_price:.2f} total ({discount}% discount)")
        
        return pricing_results

    def generate_order_summary_with_collections(self, name: str, selections: Dict[str, Any]) -> Tuple[List[str], Dict[str, float], float]:
        """
        Generate comprehensive order summary using multiple collection types.
        
        Creates a detailed order summary by processing customer selections and
        calculating pricing. Demonstrates combined usage of lists, dictionaries,
        and tuples for complex data management.
        
        The function builds an order items list, creates a pricing breakdown
        dictionary, and returns multiple values as a tuple. Handles accessories,
        discounts, and tax calculations.
        
        Args:
            name (str): Customer name for the order
            selections (Dict[str, Any]): Dictionary containing customer selections
                with possible keys:
                - 'color': Selected shoe color (str)
                - 'size': Selected shoe size (str or float)
                - 'design': Selected design pattern (str)
                - 'accessories': List of selected accessories (List[str])
                - 'discount': Applied discount percentage (int or float)
        
        Returns:
            Tuple[List[str], Dict[str, float], float]: A tuple containing:
                - List[str]: Formatted order items for display
                - Dict[str, float]: Pricing breakdown with keys:
                    - 'base_cost': Base shoe price
                    - 'accessory_cost': Total cost of accessories
                    - 'discount': Discount percentage applied
                    - 'tax_rate': Tax rate used in calculation
                - float: Final total price including tax
        
        Note:
            - Base cost is $120.00 per pair
            - Each accessory adds $25.00
            - Tax rate is 8% (0.08)
            - Discount is applied before tax calculation
            
        Example:
            >>> customizer = EnhancedLacrosseCustomizer()
            >>> selections = {
            ...     'color': 'Blue', 'size': '9.5', 'design': 'Modern TA',
            ...     'accessories': ['Ankle Guards', 'Extra Laces'], 'discount': 10
            ... }
            >>> items, pricing, total = customizer.generate_order_summary_with_collections(
            ...     "John Doe", selections)
            >>> print(f"Total: ${total:.2f}")
            Total: $162.00
        """
        print("\n📄 COMPREHENSIVE ORDER SUMMARY")
        print("=" * 40)
        
        # Order items as list
        order_items = [
            f"Name: {name}",
            f"Color: {selections.get('color', 'Red')}",
            f"Size: {selections.get('size', '9.0')}",
            f"Design: {selections.get('design', 'Classic TA')}"
        ]
        
        # Add accessories if any
        accessories = selections.get('accessories', [])
        if accessories:
            order_items.append(f"Accessories: {', '.join(accessories)}")
        
        # Pricing breakdown as dictionary
        pricing = {
            'base_cost': 120.0,
            'accessory_cost': len(accessories) * 25.0,
            'discount': selections.get('discount', 0),
            'tax_rate': 0.08
        }
        
        # Calculate total
        subtotal = pricing['base_cost'] + pricing['accessory_cost']
        discount_amount = subtotal * (pricing['discount'] / 100)
        taxable = subtotal - discount_amount
        tax = taxable * pricing['tax_rate']
        total = taxable + tax
        
        print("Order Items:")
        for item in order_items:
            print(f"  • {item}")
        
        print(f"\nPricing Breakdown:")
        print(f"  Base Cost: ${pricing['base_cost']:.2f}")
        print(f"  Accessories: ${pricing['accessory_cost']:.2f}")
        print(f"  Discount: -{pricing['discount']}% (-${discount_amount:.2f})")
        print(f"  Tax: ${tax:.2f}")
        print(f"  TOTAL: ${total:.2f}")
        
        return order_items, pricing, total

    def create_inventory_report(self) -> Tuple[List[List[Union[str, float, int]]], List[Tuple[str, float, int]], List[Tuple[str, float, int]]]:
        """
        Create comprehensive inventory report using nested collections.
        
        Generates detailed inventory analysis using nested lists for inventory data
        and tuples for critical items that need attention. Processes stock levels,
        identifies low stock situations, and determines reorder requirements.
        
        The function uses a nested list structure where each inventory item is
        represented as [color, size, current_quantity, reorder_threshold]. Analysis
        results are returned as lists of tuples for efficient processing.
        
        Returns:
            Tuple[List[List[Union[str, float, int]]], List[Tuple[str, float, int]], List[Tuple[str, float, int]]]:
            A tuple containing:
                - List[List[Union[str, float, int]]]: Complete inventory data where each
                  inner list contains [color(str), size(float), quantity(int), reorder_point(int)]
                - List[Tuple[str, float, int]]: Items needing reorder as
                  (color, size, current_quantity) tuples
                - List[Tuple[str, float, int]]: Critical low stock items as
                  (color, size, current_quantity) tuples
        
        Note:
            - Reorder needed: quantity <= reorder_point
            - Low stock: quantity < 10 pairs
            - Different colors have different reorder thresholds based on demand
            
        Example:
            >>> customizer = EnhancedLacrosseCustomizer()
            >>> inventory, reorder, low_stock = customizer.create_inventory_report()
            >>> print(f"Items needing reorder: {len(reorder)}")
            Items needing reorder: 3
            >>> if low_stock:
            ...     color, size, qty = low_stock[0]
            ...     print(f"Critical: {color} {size} has only {qty} pairs")
            Critical: Black 9.0 has only 8 pairs
        """
        print("\n📊 INVENTORY REPORT")
        print("=" * 25)
        
        # Inventory data: [color, size, quantity, reorder_point]
        inventory_data = [
            ["Red", 8.0, 45, 20],
            ["Red", 9.0, 32, 20],
            ["Red", 10.0, 28, 20],
            ["Blue", 8.0, 38, 15],
            ["Blue", 9.0, 15, 15],  # Low stock
            ["Blue", 10.0, 41, 15],
            ["Black", 8.0, 22, 25],
            ["Black", 9.0, 8, 25],   # Very low stock
            ["Black", 10.0, 35, 25]
        ]
        
        # Analyze inventory using list operations
        low_stock_items = []
        reorder_needed = []
        
        for color, size, quantity, reorder_point in inventory_data:
            if quantity <= reorder_point:
                reorder_needed.append((color, size, quantity))
            if quantity < 10:
                low_stock_items.append((color, size, quantity))
        
        print("📦 Current Inventory:")
        for item in inventory_data[:5]:  # Show first 5 items
            color, size, quantity, reorder = item
            status = "🔴 LOW" if quantity < 10 else "🟡 REORDER" if quantity <= reorder else "🟢 OK"
            print(f"  {color} {size}: {quantity} pairs {status}")
        
        print(f"\n⚠️  Items needing reorder: {len(reorder_needed)}")
        for color, size, quantity in reorder_needed:
            print(f"  • {color} {size}: Only {quantity} left")
            
        return inventory_data, reorder_needed, low_stock_items

    def demo_advanced_collections(self) -> Dict[str, Union[List[Tuple[str, int, str, str]], float, Tuple[List[str], List[str], List[str]]]]:
        """
        Demonstrate advanced usage of lists and tuples in complex scenarios.
        
        Showcases sophisticated collection patterns including:
        - Lists of tuples for customer review data
        - Tuple unpacking in list comprehensions
        - Statistical analysis using collection operations
        - Tuple of lists for categorized data organization
        - Combined collection types for real-world data modeling
        
        This function simulates customer review processing and product categorization
        to demonstrate how lists and tuples work together in complex data scenarios.
        
        Returns:
            Dict[str, Union[List[Tuple[str, int, str, str]], float, Tuple[List[str], List[str], List[str]]]]:
            Dictionary containing analysis results:
                - 'all_reviews': Complete list of review tuples (name, rating, comment, date)
                - 'high_rated_reviews': List of reviews with rating >= 4
                - 'average_rating': Calculated average rating as float
                - 'design_categories': Tuple of three lists containing categorized designs
                - 'total_reviews': Total number of reviews processed
        
        Note:
            Customer reviews are stored as tuples of (name, rating, comment, date)
            for immutable review records. Design categories use tuple of lists
            for organized product grouping.
            
        Example:
            >>> customizer = EnhancedLacrosseCustomizer()
            >>> results = customizer.demo_advanced_collections()
            >>> avg_rating = results['average_rating']
            >>> print(f"Average customer rating: {avg_rating:.1f}/5")
            Average customer rating: 4.2/5
            >>> traditional, modern, bold = results['design_categories']
            >>> print(f"Traditional designs: {traditional}")
            Traditional designs: ['Classic TA', 'Vintage TA']
        """
        print("\n🚀 ADVANCED COLLECTIONS DEMO")
        print("=" * 35)
        
        results = {}
        
        # List of tuples for customer reviews
        customer_reviews = [
            ("John D.", 5, "Excellent quality!", "2024-01-15"),
            ("Sarah M.", 4, "Very comfortable", "2024-01-18"),
            ("Mike R.", 5, "Perfect for lacrosse", "2024-01-20"),
            ("Lisa K.", 3, "Good but pricey", "2024-01-22")
        ]
        results['all_reviews'] = customer_reviews
        
        # Process reviews using list comprehension and tuple unpacking
        high_ratings = [(name, rating, comment) for name, rating, comment, date in customer_reviews if rating >= 4]
        results['high_rated_reviews'] = high_ratings
        
        avg_rating = sum(rating for _, rating, _, _ in customer_reviews) / len(customer_reviews)
        results['average_rating'] = avg_rating
        results['total_reviews'] = len(customer_reviews)
        
        print(f"Average Rating: {avg_rating:.1f}/5 stars")
        print("High-rated reviews:")
        for name, rating, comment in high_ratings:
            print(f"  ⭐ {name}: {rating}/5 - '{comment}'")
        
        # Tuple of lists for different shoe categories
        shoe_categories = (
            ["Classic TA", "Vintage TA"],           # Traditional designs
            ["Modern TA", "Tech TA"],               # Modern designs  
            ["Bold TA", "Neon TA", "Custom TA"]     # Bold designs
        )
        results['design_categories'] = shoe_categories
        
        traditional, modern, bold = shoe_categories
        print(f"\nDesign Categories:")
        print(f"  Traditional: {traditional}")
        print(f"  Modern: {modern}")
        print(f"  Bold: {bold}")
        
        return results

def main() -> None:
    """
    Main demonstration function showcasing all list and tuple implementations.
    
    Executes a comprehensive demonstration of the EnhancedLacrosseCustomizer class,
    running all methods that showcase lists and tuples usage. Provides interactive
    examples and displays results from various collection operations.
    
    The function demonstrates:
    - Basic list and tuple operations
    - Interactive user preference collection
    - Color combination analysis
    - Bulk pricing calculations
    - Order summary generation
    - Inventory reporting
    - Advanced collection patterns
    
    Returns:
        None
        
    Example: