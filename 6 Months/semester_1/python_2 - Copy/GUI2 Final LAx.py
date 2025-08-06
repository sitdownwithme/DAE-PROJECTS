"""
Enhanced TA Customizer GUI - Lacrosse Shoe Customization System

This program provides a comprehensive GUI for customizing lacrosse shoes with poetic themes,
customer types, seasonal collections, shipping/billing functionality, and field revision capabilities.

Features:
- Poetic customer journey themes and messaging
- Individual field revision without starting over
- Complete shipping and billing address management
- Seasonal color collections with dynamic updates
- Smart discount calculation based on customer type
- Professional GUI with scrollable interface
- Input validation and error handling
- Tax calculation and final pricing

Author: Enhanced from original LAXTA2025DAE system
Date: 2025
"""

import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import font as tkFont
import random
from datetime import datetime
from typing import Dict, List, Tuple


class LacrosseShoeCustomizer:
    """
    Core business logic class that handles all customization inputs, pricing logic, 
    and calculations for lacrosse shoes based on user preferences.
    
    This class maintains the original functionality from LAXTA2025DAE.py while
    being adapted for GUI integration.
    """
    
    def __init__(self):
        """Initialize all customization fields and preset options."""
        # Customer information
        self.name: str = ""
        self.customer_type: str = ""
        self.memory_tag: str = ""
        
        # Shoe customization
        self.color: str = ""
        self.size: float = 0.0
        self.traction: str = ""
        self.support: str = ""
        self.design: str = ""
        self.season: str = ""
        
        # Pricing and discounts
        self.base_cost: float = 150.0  # Updated base price
        self.discount: float = 0.0
        self.final_price: float = 0.0
        self.discount_reason: str = ""
        
        # Address information
        self.shipping_address: Dict[str, str] = {}
        self.billing_address: Dict[str, str] = {}
        
        # Preset selection options (from original LAXTA2025DAE)
        self.TRACTION_TYPES = ["Standard", "All-Terrain", "Speed", "Grip+"]
        self.SUPPORT_LEVELS = ["Light", "Medium", "High", "Maximum"]
        self.MIN_SIZE = 5.0
        self.MAX_SIZE = 15.0
        
        # Enhanced poetic designs
        self.DESIGNS = [
            "The Journey",         # for those who've lived in two worlds
            "Crossroads Classic",  # where North meets South
            "Rooted Rise",         # growth from where it started
            "Horizon Line"         # for what's ahead
        ]
        
        # Poetic customer types
        self.CUSTOMER_TYPES = [
            "The Mentor", 
            "The First-Timer", 
            "The One Who Came Back", 
            "The Quiet Storm"
        ]
        
        # Seasonal color collections (from original system)
        self.SEASONAL_COLLECTIONS = {
            "Spring": ["Spring Green", "Fresh Blue", "Sunrise Yellow", "Lavender Bloom"],
            "Summer": ["Ocean Blue", "Sandy Beige", "Coral Pink", "Sunset Orange"],
            "Fall": ["Autumn Red", "Golden Brown", "Forest Green", "Harvest Gold"],
            "Winter": ["Winter White", "Ice Blue", "Charcoal Gray", "Frost Silver"]
        }

    def calculate_tax(self, price: float, tax_rate: float = 0.08) -> float:
        """
        Calculates tax based on a default or provided tax rate.
        
        Args:
            price (float): Pre-tax price
            tax_rate (float): Tax rate as decimal (default 8%)
            
        Returns:
            float: Tax amount rounded to 2 decimal places
        """
        return round(price * tax_rate, 2)

    def calculate_discount(self, customer_type: str) -> Tuple[float, str]:
        """
        Calculate discount percentage and reason based on customer type.
        Each customer type has a meaningful discount with poetic reasoning.
        
        Args:
            customer_type (str): The type of customer
            
        Returns:
            Tuple[float, str]: Discount percentage and reason
        """
        discount_map = {
            "The Mentor": (15, "Because someone saw your worth."),
            "The First-Timer": (5, "Because every start deserves belief."),
            "The One Who Came Back": (10, "Because you've come far already."),
            "The Quiet Storm": (0, "Because some journeys don't need discounts—they earn every step.")
        }
        return discount_map.get(customer_type, (0, "Standard pricing"))

    def calculate_final_price(self) -> float:
        """
        Calculates final shoe price based on support level, customer discount, and tax.
        Incorporates the original pricing logic with enhancements.
        
        Returns:
            float: Final price including tax
        """
        # Add-on pricing based on support level (from original system)
        support_addon = {
            "Maximum": 30,
            "High": 20, 
            "Medium": 10,
            "Light": 0
        }
        addon = support_addon.get(self.support, 0)
        
        # Calculate base cost with addon
        base_with_addon = self.base_cost + addon
        
        # Apply customer type discount
        self.discount, self.discount_reason = self.calculate_discount(self.customer_type)
        
        # Calculate subtotal after discount
        subtotal = base_with_addon * (1 - self.discount / 100)
        
        # Add tax
        tax = self.calculate_tax(subtotal)
        
        # Final price
        self.final_price = round(subtotal + tax, 2)
        return self.final_price

    def validate_size(self, size_str: str) -> bool:
        """
        Validates shoe size input to ensure it's within acceptable range.
        
        Args:
            size_str (str): Size as string input
            
        Returns:
            bool: True if valid, False otherwise
        """
        try:
            size = float(size_str)
            return self.MIN_SIZE <= size <= self.MAX_SIZE
        except ValueError:
            return False


class TACustomizerGUI:
    """
    Main GUI class for the TA Customizer application.
    
    Provides a complete interface for shoe customization with poetic themes,
    field revision capabilities, and comprehensive address management.
    """
    
    def __init__(self, root):
        """
        Initialize the GUI application with all components and styling.
        
        Args:
            root: Tkinter root window
        """
        self.root = root
        self.root.title("TA Customizer — Where Every Pair Walks a Path Back to Where You Began")
        self.root.geometry("850x950")
        self.root.configure(bg='#f8f9fa')
        
        # Initialize the business logic
        self.customizer = LacrosseShoeCustomizer()
        
        # GUI state variables
        self.current_values = {}
        
        # Build the complete interface
        self.build_gui()

    def build_gui(self):
        """
        Constructs the complete GUI interface with all sections and components.
        Creates a scrollable interface with organized sections for different input types.
        """
        # Create main scrollable frame
        main_frame = tk.Frame(self.root, bg='#f8f9fa')
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Canvas and scrollbar for scrolling
        canvas = tk.Canvas(main_frame, bg='#f8f9fa', highlightthickness=0)
        scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        self.scrollable_frame = tk.Frame(canvas, bg='#f8f9fa')
        
        # Configure scrolling
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Pack canvas and scrollbar
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Main content frame with padding
        self.frame = tk.Frame(self.scrollable_frame, bg='#f8f9fa', padx=40, pady=30)
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        # Build all sections
        self._build_header()
        self._build_personal_section()
        self._build_customization_section()
        self._build_shipping_section()
        self._build_billing_section()
        self._build_submit_section()
        
        # Enable mouse wheel scrolling
        self._bind_mousewheel(canvas)

    def _build_header(self):
        """Creates the application header with title and subtitle."""
        # Main title
        title_font = tkFont.Font(family="Georgia", size=18, weight="bold")
        title_label = tk.Label(
            self.frame, 
            text="🎤 Welcome to the TA Customizer", 
            font=title_font, 
            bg='#f8f9fa', 
            fg='#2c3e50'
        )
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 5))
        
        # Subtitle
        subtitle_font = tkFont.Font(family="Georgia", size=11, slant="italic")
        subtitle_label = tk.Label(
            self.frame, 
            text="Where every pair walks a path back to where you began", 
            font=subtitle_font, 
            bg='#f8f9fa', 
            fg='#7f8c8d'
        )
        subtitle_label.grid(row=1, column=0, columnspan=3, pady=(0, 30))

    def _build_personal_section(self):
        """Creates the personal information input section."""
        current_row = 2
        
        # Section header
        section_font = tkFont.Font(family="Arial", size=13, weight="bold")
        personal_label = tk.Label(
            self.frame, 
            text="✨ Personal Journey", 
            font=section_font, 
            bg='#f8f9fa', 
            fg='#34495e'
        )
        personal_label.grid(row=current_row, column=0, columnspan=3, sticky="w", pady=(10, 15))
        current_row += 1
        
        # Name field
        tk.Label(self.frame, text="Name:", bg='#f8f9fa', font=("Arial", 10)).grid(
            row=current_row, column=0, sticky="w", padx=(0, 15), pady=5
        )
        self.name_entry = tk.Entry(self.frame, width=30, font=("Arial", 10))
        self.name_entry.grid(row=current_row, column=1, sticky="w", pady=5)
        self._create_revise_button(current_row, 'name')
        current_row += 1
        
        # Customer Type field
        tk.Label(self.frame, text="Customer Type:", bg='#f8f9fa', font=("Arial", 10)).grid(
            row=current_row, column=0, sticky="w", padx=(0, 15), pady=5
        )
        self.customer_var = tk.StringVar()
        self.customer_menu = ttk.Combobox(
            self.frame, 
            textvariable=self.customer_var, 
            values=self.customizer.CUSTOMER_TYPES, 
            state="readonly", 
            width=27,
            font=("Arial", 10)
        )
        self.customer_menu.grid(row=current_row, column=1, sticky="w", pady=5)
        self._create_revise_button(current_row, 'customer_type')
        current_row += 1
        
        # Memory Tag field
        tk.Label(self.frame, text="Memory Tag:", bg='#f8f9fa', font=("Arial", 10)).grid(
            row=current_row, column=0, sticky="w", padx=(0, 15), pady=5
        )
        self.memory_entry = tk.Entry(self.frame, width=30, font=("Arial", 10))
        self.memory_entry.grid(row=current_row, column=1, sticky="w", pady=5)
        self._create_revise_button(current_row, 'memory_tag')
        current_row += 1
        
        # Memory tag helper text
        helper_label = tk.Label(
            self.frame, 
            text="(e.g., First Win, Her Smile, My Comeback)", 
            font=("Arial", 8), 
            bg='#f8f9fa', 
            fg='#95a5a6'
        )
        helper_label.grid(row=current_row, column=1, sticky="w", pady=(0, 10))
        
        self.personal_end_row = current_row + 1

    def _build_customization_section(self):
        """Creates the shoe customization input section."""
        current_row = self.personal_end_row
        
        # Section header
        section_font = tkFont.Font(family="Arial", size=13, weight="bold")
        custom_label = tk.Label(
            self.frame, 
            text="👟 Shoe Customization", 
            font=section_font, 
            bg='#f8f9fa', 
            fg='#34495e'
        )
        custom_label.grid(row=current_row, column=0, columnspan=3, sticky="w", pady=(20, 15))
        current_row += 1
        
        # Season selection
        tk.Label(self.frame, text="Season:", bg='#f8f9fa', font=("Arial", 10)).grid(
            row=current_row, column=0, sticky="w", padx=(0, 15), pady=5
        )
        self.season_var = tk.StringVar()
        self.season_menu = ttk.Combobox(
            self.frame, 
            textvariable=self.season_var, 
            values=list(self.customizer.SEASONAL_COLLECTIONS.keys()), 
            state="readonly", 
            width=27,
            font=("Arial", 10)
        )
        self.season_menu.grid(row=current_row, column=1, sticky="w", pady=5)
        self.season_menu.bind("<<ComboboxSelected>>", self._update_colors)
        self._create_revise_button(current_row, 'season')
        current_row += 1
        
        # Color selection (dynamically updated based on season)
        tk.Label(self.frame, text="Color:", bg='#f8f9fa', font=("Arial", 10)).grid(
            row=current_row, column=0, sticky="w", padx=(0, 15), pady=5
        )
        self.color_var = tk.StringVar()
        self.color_menu = ttk.Combobox(
            self.frame, 
            textvariable=self.color_var, 
            state="readonly", 
            width=27,
            font=("Arial", 10)
        )
        self.color_menu.grid(row=current_row, column=1, sticky="w", pady=5)
        self._create_revise_button(current_row, 'color')
        current_row += 1
        
        # Size input with validation
        tk.Label(self.frame, text="Shoe Size (5-15):", bg='#f8f9fa', font=("Arial", 10)).grid(
            row=current_row, column=0, sticky="w", padx=(0, 15), pady=5
        )
        self.size_entry = tk.Entry(self.frame, width=30, font=("Arial", 10))
        self.size_entry.grid(row=current_row, column=1, sticky="w", pady=5)
        self._create_revise_button(current_row, 'size')
        current_row += 1
        
        # Traction type selection
        tk.Label(self.frame, text="Traction Type:", bg='#f8f9fa', font=("Arial", 10)).grid(
            row=current_row, column=0, sticky="w", padx=(0, 15), pady=5
        )
        self.traction_var = tk.StringVar()
        self.traction_menu = ttk.Combobox(
            self.frame, 
            textvariable=self.traction_var, 
            values=self.customizer.TRACTION_TYPES, 
            state="readonly", 
            width=27,
            font=("Arial", 10)
        )
        self.traction_menu.grid(row=current_row, column=1, sticky="w", pady=5)
        self._create_revise_button(current_row, 'traction')
        current_row += 1
        
        # Support level selection
        tk.Label(self.frame, text="Support Level:", bg='#f8f9fa', font=("Arial", 10)).grid(
            row=current_row, column=0, sticky="w", padx=(0, 15), pady=5
        )
        self.support_var = tk.StringVar()
        self.support_menu = ttk.Combobox(
            self.frame, 
            textvariable=self.support_var, 
            values=self.customizer.SUPPORT_LEVELS, 
            state="readonly", 
            width=27,
            font=("Arial", 10)
        )
        self.support_menu.grid(row=current_row, column=1, sticky="w", pady=5)
        self._create_revise_button(current_row, 'support')
        current_row += 1
        
        # Design selection
        tk.Label(self.frame, text="Design:", bg='#f8f9fa', font=("Arial", 10)).grid(
            row=current_row, column=0, sticky="w", padx=(0, 15), pady=5
        )
        self.design_var = tk.StringVar()
        self.design_menu = ttk.Combobox(
            self.frame, 
            textvariable=self.design_var, 
            values=["No design"] + self.customizer.DESIGNS, 
            state="readonly", 
            width=27,
            font=("Arial", 10)
        )
        self.design_menu.grid(row=current_row, column=1, sticky="w", pady=5)
        self._create_revise_button(current_row, 'design')
        
        self.customization_end_row = current_row + 1

    def _build_shipping_section(self):
        """Creates the shipping address input section."""
        current_row = self.customization_end_row
        
        # Section header
        section_font = tkFont.Font(family="Arial", size=13, weight="bold")
        shipping_label = tk.Label(
            self.frame, 
            text="📦 Shipping Information", 
            font=section_font, 
            bg='#f8f9fa', 
            fg='#34495e'
        )
        shipping_label.grid(row=current_row, column=0, columnspan=3, sticky="w", pady=(25, 15))
        current_row += 1
        
        # Shipping address fields
        fields = [
            ("Street Address:", "ship_address_entry"),
            ("City:", "ship_city_entry"),
            ("State:", "ship_state_entry"),
            ("ZIP Code:", "ship_zip_entry")
        ]
        
        for label_text, entry_name in fields:
            tk.Label(self.frame, text=label_text, bg='#f8f9fa', font=("Arial", 10)).grid(
                row=current_row, column=0, sticky="w", padx=(0, 15), pady=5
            )
            entry = tk.Entry(self.frame, width=30, font=("Arial", 10))
            entry.grid(row=current_row, column=1, sticky="w", pady=5)
            setattr(self, entry_name, entry)
            current_row += 1
        
        self.shipping_end_row = current_row

    def _build_billing_section(self):
        """Creates the billing address input section with same-as-shipping option."""
        current_row = self.shipping_end_row
        
        # Section header
        section_font = tkFont.Font(family="Arial", size=13, weight="bold")
        billing_label = tk.Label(
            self.frame, 
            text="💳 Billing Information", 
            font=section_font, 
            bg='#f8f9fa', 
            fg='#34495e'
        )
        billing_label.grid(row=current_row, column=0, columnspan=3, sticky="w", pady=(25, 15))
        current_row += 1
        
        # Same as shipping checkbox
        self.same_address_var = tk.BooleanVar()
        same_address_check = tk.Checkbutton(
            self.frame, 
            text="Billing address same as shipping", 
            variable=self.same_address_var, 
            command=self._toggle_billing_fields,
            bg='#f8f9fa',
            font=("Arial", 10)
        )
        same_address_check.grid(row=current_row, column=0, columnspan=2, sticky="w", pady=(0, 15))
        current_row += 1
        
        # Billing address fields
        fields = [
            ("Street Address:", "bill_address_entry"),
            ("City:", "bill_city_entry"),
            ("State:", "bill_state_entry"),
            ("ZIP Code:", "bill_zip_entry")
        ]
        
        self.billing_fields = []
        for label_text, entry_name in fields:
            tk.Label(self.frame, text=label_text, bg='#f8f9fa', font=("Arial", 10)).grid(
                row=current_row, column=0, sticky="w", padx=(0, 15), pady=5
            )
            entry = tk.Entry(self.frame, width=30, font=("Arial", 10))
            entry.grid(row=current_row, column=1, sticky="w", pady=5)
            setattr(self, entry_name, entry)
            self.billing_fields.append(entry)
            current_row += 1
        
        self.billing_end_row = current_row

    def _build_submit_section(self):
        """Creates the final submit button section."""
        current_row = self.billing_end_row
        
        # Submit button with poetic text
        submit_btn = tk.Button(
            self.frame, 
            text="Complete Your Journey ✨", 
            command=self._submit_form,
            bg='#3498db', 
            fg='white', 
            font=("Arial", 14, "bold"), 
            padx=30, 
            pady=15,
            relief='raised',
            borderwidth=2
        )
        submit_btn.grid(row=current_row, column=0, columnspan=3, pady=40)

    def _create_revise_button(self, row: int, field_name: str):
        """
        Creates a revision button for a specific field.
        
        Args:
            row (int): Grid row for button placement
            field_name (str): Name of field to revise
        """
        revise_btn = tk.Button(
            self.frame, 
            text="📝", 
            command=lambda: self._revise_field(field_name), 
            width=3, 
            bg='#ecf0f1',
            font=("Arial", 8)
        )
        revise_btn.grid(row=row, column=2, padx=(10, 0), pady=5)

    def _bind_mousewheel(self, canvas):
        """
        Binds mouse wheel scrolling to the canvas.
        
        Args:
            canvas: The tkinter Canvas widget to bind scrolling to
        """
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        canvas.bind("<MouseWheel>", _on_mousewheel)

    def _update_colors(self, event=None):
        """
        Updates available color options based on selected season.
        Called when season selection changes.
        
        Args:
            event: Tkinter event (optional)
        """
        selected_season = self.season_var.get()
        if selected_season in self.customizer.SEASONAL_COLLECTIONS:
            colors = self.customizer.SEASONAL_COLLECTIONS[selected_season]
            self.color_menu["values"] = colors
            if colors:
                self.color_menu.current(0)  # Select first color by default

    def _toggle_billing_fields(self):
        """
        Enables or disables billing address fields based on same-as-shipping checkbox.
        """
        if self.same_address_var.get():
            # Disable billing fields when same as shipping
            for field in self.billing_fields:
                field.config(state='disabled')
        else:
            # Enable billing fields for separate address
            for field in self.billing_fields:
                field.config(state='normal')

    def _revise_field(self, field_name: str):
        """
        Opens a revision dialog for a specific field without losing other data.
        
        Args:
            field_name (str): Name of the field to revise
        """
        # Create revision popup window
        revision_window = tk.Toplevel(self.root)
        revision_window.title(f"Revise {field_name.replace('_', ' ').title()}")
        revision_window.geometry("450x250")
        revision_window.configure(bg='#f8f9fa')
        revision_window.grab_set()  # Make modal
        
        # Center the window
        revision_window.transient(self.root)
        
        # Header
        header_font = tkFont.Font(family="Arial", size=12, weight="bold")
        tk.Label(
            revision_window, 
            text=f"Revise your {field_name.replace('_', ' ')}", 
            bg='#f8f9fa', 
            font=header_font,
            fg='#2c3e50'
        ).pack(pady=15)
        
        # Field-specific revision interface
        if field_name == 'name':
            current_value = self.name_entry.get()
            entry_widget = tk.Entry(revision_window, width=35, font=("Arial", 11))
            entry_widget.pack(pady=15)
            entry_widget.insert(0, current_value)
            entry_widget.focus()
            
            def save_revision():
                self.name_entry.delete(0, tk.END)
                self.name_entry.insert(0, entry_widget.get())
                revision_window.destroy()
                
        elif field_name == 'customer_type':
            current_value = self.customer_var.get()
            var = tk.StringVar(value=current_value)
            combo = ttk.Combobox(
                revision_window, 
                textvariable=var, 
                values=self.customizer.CUSTOMER_TYPES, 
                state="readonly",
                font=("Arial", 11)
            )
            combo.pack(pady=15)
            
            def save_revision():
                self.customer_var.set(var.get())
                revision_window.destroy()
                
        elif field_name == 'memory_tag':
            current_value = self.memory_entry.get()
            entry_widget = tk.Entry(revision_window, width=35, font=("Arial", 11))
            entry_widget.pack(pady=15)
            entry_widget.insert(0, current_value)
            entry_widget.focus()
            
            def save_revision():
                self.memory_entry.delete(0, tk.END)
                self.memory_entry.insert(0, entry_widget.get())
                revision_window.destroy()
                
        elif field_name == 'season':
            current_value = self.season_var.get()
            var = tk.StringVar(value=current_value)
            combo = ttk.Combobox(
                revision_window, 
                textvariable=var, 
                values=list(self.customizer.SEASONAL_COLLECTIONS.keys()), 
                state="readonly",
                font=("Arial", 11)
            )
            combo.pack(pady=15)
            
            def save_revision():
                self.season_var.set(var.get())
                self._update_colors()  # Update colors when season changes
                revision_window.destroy()
                
        elif field_name == 'color':
            current_value = self.color_var.get()
            var = tk.StringVar(value=current_value)
            season = self.season_var.get()
            colors = self.customizer.SEASONAL_COLLECTIONS.get(season, [])
            combo = ttk.Combobox(
                revision_window, 
                textvariable=var, 
                values=colors, 
                state="readonly",
                font=("Arial", 11)
            )
            combo.pack(pady=15)
            
            def save_revision():
                self.color_var.set(var.get())
                revision_window.destroy()
                
        elif field_name == 'size':
            current_value = self.size_entry.get()
            entry_widget = tk.Entry(revision_window, width=35, font=("Arial", 11))
            entry_widget.pack(pady=15)
            entry_widget.insert(0, current_value)
            entry_widget.focus()
            
            def save_revision():
                self.size_entry.delete(0, tk.END)
                self.size_entry.insert(0, entry_widget.get())
                revision_window.destroy()
                
        elif field_name == 'traction':
            current_value = self.traction_var.get()
            var = tk.StringVar(value=current_value)
            combo = ttk.Combobox(
                revision_window, 
                textvariable=var, 
                values=self.customizer.TRACTION_TYPES, 
                state="readonly",
                font=("Arial", 11)
            )
            combo.pack(pady=15)
            
            def save_revision():
                self.traction_var.set(var.get())
                revision_window.destroy()
                
        elif field_name == 'support':
            current_value = self.support_var.get()
            var = tk.StringVar(value=current_value)
            combo = ttk.Combobox(
                revision_window, 
                textvariable=var, 
                values=self.customizer.SUPPORT_LEVELS, 
                state="readonly",
                font=("Arial", 11)
            )
            combo.pack(pady=15)
            
            def save_revision():
                self.support_var.set(var.get())
                revision_window.destroy()
                
        elif field_name == 'design':
            current_value = self.design_var.get()
            var = tk.StringVar(value=current_value)
            combo = ttk.Combobox(
                revision_window, 
                textvariable=var, 
                values=["No design"] + self.customizer.DESIGNS, 
                state="readonly",
                font=("Arial", 11)
            )
            combo.pack(pady=15)
            
            def save_revision():
                self.design_var.set(var.get())
                revision_window.destroy()
        
        # Create action buttons
        button_frame = tk.Frame(revision_window, bg='#f8f9fa')
        button_frame.pack(pady=20)
        
        save_btn = tk.Button(
            button_frame, 
            text="Save Changes", 
            command=save_revision,
            bg='#27ae60', 
            fg='white', 
            font=("Arial", 11, "bold"),
            padx=15,
            pady=8
        )
        save_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        cancel_btn = tk.Button(
            button_frame, 
            text="Cancel", 
            command=revision_window.destroy,
            bg='#e74c3c', 
            fg='white', 
            font=("Arial", 11),
            padx=15,
            pady=8
        )
        cancel_btn.pack(side=tk.LEFT)

    def _get_billing_address(self) -> Dict[str, str]:
        """
        Gets billing address information, using shipping address if same-as-shipping is checked.
        
        Returns:
            Dict[str, str]: Billing address information
        """
        if self.same_address_var.get():
            # Use shipping address
            return {
                'address': self.ship_address_entry.get().strip(),
                'city': self.ship_city_entry.get().strip(),
                'state': self.ship_state_entry.get().strip(),
                'zip': self.ship_zip_entry.get().strip()
            }
        else:
            # Use separate billing address
            return {
                'address': self.bill_address_entry.get().strip(),
                'city': self.bill_city_entry.get().strip(),
                'state': self.bill_state_entry.get().strip(),
                'zip': self.bill_zip_entry.get().strip()
            }

    def _validate_form(self) -> Tuple[bool, str]:
        """
        Validates all form inputs and returns validation status.
        
        Returns:
            Tuple[bool, str]: (is_valid, error_message)
        """
        # Validate personal information
        if not self.name_entry.get().strip():
            return False, "Name is required."
        
        if not self.customer_var.get():
            return False, "Customer type is required."
        
        if not self.memory_entry.get().strip():
            return False, "Memory tag is required."
        
        # Validate shoe customization
        if not self.season_var.get():
            return False, "Season selection is required."
        
        if not self.color_var.get():
            return False, "Color selection is required."
        
        # Validate shoe size
        size_str = self.size_entry.get().strip()
        if not size_str:
            return False, "Shoe size is required."
        
        if not self.customizer.validate_size(size_str):
            return False, f"Shoe size must be between {self.customizer.MIN_SIZE} and {self.customizer.MAX_SIZE}."
        
        if not self.traction_var.get():
            return False, "Traction type is required."
        
        if not self.support_var.get():
            return False, "Support level is required."
        
        if not self.design_var.get():
            return False, "Design selection is required."
        
        # Validate shipping address
        shipping_fields = [
            self.ship_address_entry.get().strip(),
            self.ship_city_entry.get().strip(),
            self.ship_state_entry.get().strip(),
            self.ship_zip_entry.get().strip()
        ]
        
        if not all(shipping_fields):
            return False, "All shipping address fields are required."
        
        # Validate billing address
        billing = self._get_billing_address()
        if not all(billing.values()):
            return False, "All billing address fields are required."
        
        return True, ""

    def _populate_customizer(self):
        """
        Populates the customizer object with form data for processing.
        """
        # Personal information
        self.customizer.name = self.name_entry.get().strip()
        self.customizer.customer_type = self.customer_var.get()
        self.customizer.memory_tag = self.memory_entry.get().strip()
        
        # Shoe customization
        self.customizer.season = self.season_var.get()
        self.customizer.color = self.color_var.get()
        self.customizer.size = float(self.size_entry.get())
        self.customizer.traction = self.traction_var.get()
        self.customizer.support = self.support_var.get()
        self.customizer.design = self.design_var.get()
        
        # Address information
        self.customizer.shipping_address = {
            'address': self.ship_address_entry.get().strip(),
            'city': self.ship_city_entry.get().strip(),
            'state': self.ship_state_entry.get().strip(),
            'zip': self.ship_zip_entry.get().strip()
        }
        
        self.customizer.billing_address = self._get_billing_address()

    def _create_order_summary(self) -> str:
        """
        Creates a formatted order summary with all details and pricing.
        
        Returns:
            str: Formatted order summary
        """
        billing_note = " (Same as shipping)" if self.same_address_var.get() else ""
        
        # Get current timestamp
        order_time = datetime.now().strftime("%B %d, %Y at %I:%M %p")
        
        summary = f"""✨ Your Journey Begins ✨

🏷️  PERSONAL DETAILS
Name: {self.customizer.name}
Customer Type: {self.customizer.customer_type}
Memory Tag: "{self.customizer.memory_tag}"

👟 SHOE CUSTOMIZATION
Season Collection: {self.customizer.season}
Color: {self.customizer.color}
Size: {self.customizer.size}
Traction Type: {self.customizer.traction}
Support Level: {self.customizer.support}
Design: {self.customizer.design}

📦 SHIPPING ADDRESS
{self.customizer.shipping_address['address']}
{self.customizer.shipping_address['city']}, {self.customizer.shipping_address['state']} {self.customizer.shipping_address['zip']}

💳 BILLING ADDRESS{billing_note}
{self.customizer.billing_address['address']}
{self.customizer.billing_address['city']}, {self.customizer.billing_address['state']} {self.customizer.billing_address['zip']}

💰 PRICING BREAKDOWN
Base Price: ${self.customizer.base_cost:.2f}
Support Level Add-on: ${self._get_support_addon():.2f}
Subtotal: ${self.customizer.base_cost + self._get_support_addon():.2f}
Discount: {self.customizer.discount}% - {self.customizer.discount_reason}
After Discount: ${(self.customizer.base_cost + self._get_support_addon()) * (1 - self.customizer.discount / 100):.2f}
Tax (8%): ${self.customizer.calculate_tax((self.customizer.base_cost + self._get_support_addon()) * (1 - self.customizer.discount / 100)):.2f}
Final Price: ${self.customizer.final_price:.2f}

📅 Order Date: {order_time}

"Every step forward honors where you've been."
— Your TA Customizer Team
"""
        return summary

    def _get_support_addon(self) -> float:
        """
        Gets the support level add-on cost.
        
        Returns:
            float: Add-on cost for support level
        """
        support_addon = {
            "Maximum": 30,
            "High": 20, 
            "Medium": 10,
            "Light": 0
        }
        return support_addon.get(self.customizer.support, 0)

    def _submit_form(self):
        """
        Handles form submission with validation, processing, and summary display.
        This is the main submission handler that orchestrates the entire process.
        """
        try:
            # Validate all form inputs
            is_valid, error_message = self._validate_form()
            if not is_valid:
                messagebox.showerror("Input Error", error_message)
                return
            
            # Populate customizer object with form data
            self._populate_customizer()
            
            # Calculate final pricing
            self.customizer.calculate_final_price()
            
            # Create and display order summary
            summary = self._create_order_summary()
            
            # Show success dialog with option to save or print
            result = messagebox.askyesno(
                "Order Complete", 
                "Your custom lacrosse shoes have been ordered successfully!\n\n" +
                "Would you like to view the detailed order summary?",
                icon='question'
            )
            
            if result:
                # Display detailed summary in a new window
                self._show_detailed_summary(summary)
            
            # Optional: Ask if user wants to place another order
            another_order = messagebox.askyesno(
                "New Order", 
                "Would you like to create another custom pair?",
                icon='question'
            )
            
            if another_order:
                self._reset_form()
        
        except Exception as e:
            messagebox.showerror("Processing Error", f"An error occurred while processing your order: {str(e)}")

    def _show_detailed_summary(self, summary: str):
        """
        Shows the detailed order summary in a new window.
        
        Args:
            summary (str): The formatted order summary
        """
        summary_window = tk.Toplevel(self.root)
        summary_window.title("Order Summary - TA Customizer")
        summary_window.geometry("600x700")
        summary_window.configure(bg='#f8f9fa')
        
        # Create scrollable text widget
        frame = tk.Frame(summary_window, bg='#f8f9fa')
        frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Text widget with scrollbar
        text_frame = tk.Frame(frame, bg='#f8f9fa')
        text_frame.pack(fill=tk.BOTH, expand=True)
        
        scrollbar = tk.Scrollbar(text_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        text_widget = tk.Text(
            text_frame, 
            wrap=tk.WORD, 
            yscrollcommand=scrollbar.set,
            font=("Consolas", 10),
            bg='white',
            relief='sunken',
            borderwidth=2
        )
        text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=text_widget.yview)
        
        # Insert summary text
        text_widget.insert(tk.END, summary)
        text_widget.config(state=tk.DISABLED)  # Make read-only
        
        # Close button
        close_btn = tk.Button(
            frame, 
            text="Close", 
            command=summary_window.destroy,
            bg='#3498db',
            fg='white',
            font=("Arial", 12, "bold"),
            padx=20,
            pady=10
        )
        close_btn.pack(pady=10)

    def _reset_form(self):
        """
        Resets all form fields to their default state for a new order.
        """
        # Clear personal information
        self.name_entry.delete(0, tk.END)
        self.customer_var.set("")
        self.memory_entry.delete(0, tk.END)
        
        # Clear shoe customization
        self.season_var.set("")
        self.color_var.set("")
        self.color_menu["values"] = []
        self.size_entry.delete(0, tk.END)
        self.traction_var.set("")
        self.support_var.set("")
        self.design_var.set("")
        
        # Clear shipping address
        self.ship_address_entry.delete(0, tk.END)
        self.ship_city_entry.delete(0, tk.END)
        self.ship_state_entry.delete(0, tk.END)
        self.ship_zip_entry.delete(0, tk.END)
        
        # Clear billing address
        self.bill_address_entry.delete(0, tk.END)
        self.bill_city_entry.delete(0, tk.END)
        self.bill_state_entry.delete(0, tk.END)
        self.bill_zip_entry.delete(0, tk.END)
        
        # Reset checkbox
        self.same_address_var.set(False)
        self._toggle_billing_fields()
        
        # Reset customizer object
        self.customizer = LacrosseShoeCustomizer()


def main():
    """
    Main entry point for the TA Customizer GUI application.
    
    Creates the root window and initializes the application.
    Includes error handling for application startup.
    """
    try:
        # Create and configure root window
        root = tk.Tk()
        
        # Set application icon (if available)
        try:
            # You can add an icon file here if desired
            # root.iconbitmap('icon.ico')
            pass
        except:
            pass  # Icon not found, continue without it
        
        # Initialize the application
        app = TACustomizerGUI(root)
        
        # Start the GUI event loop
        root.mainloop()
        
    except Exception as e:
        # Handle any startup errors
        print(f"Error starting TA Customizer: {e}")
        messagebox.showerror("Startup Error", f"Failed to start TA Customizer:\n{e}")


if __name__ == "__main__":
    main()
            