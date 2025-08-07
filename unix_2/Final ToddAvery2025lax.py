#!/usr/bin/env python3
"""
Enhanced Toddavery Lacrosse Shoe Customizer
Cross-platform compatible with Linux/Unix command demonstrations
"""

import random
import os
import sys
import subprocess
import shutil
import platform
from typing import Dict, List
from datetime import datetime

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

        # Detect operating system
        self.is_windows = platform.system().lower() == 'windows'
        self.is_unix = not self.is_windows

        # Initialize system environment
        self.setup_environment()
        self.settings = self.read_settings_file()

    def run_command(self, cmd_list, description="command"):
        """Cross-platform command runner with error handling."""
        try:
            if self.is_windows and cmd_list[0] in ['ls', 'cat', 'rm', 'mv', 'cp']:
                # Skip Unix commands on Windows, use Python alternatives
                return self.handle_windows_alternative(cmd_list, description)
            
            result = subprocess.run(cmd_list, check=True, capture_output=True, text=True)
            print(f"   ✅ {description}: {' '.join(cmd_list)}")
            if result.stdout.strip():
                print(f"      Output: {result.stdout.strip()}")
            return result
        except subprocess.CalledProcessError as e:
            print(f"   ❌ {description} failed: {e}")
            return None
        except FileNotFoundError:
            print(f"   ⚠️  Command not found: {cmd_list[0]} (using Python alternative)")
            return self.handle_windows_alternative(cmd_list, description)

    def handle_windows_alternative(self, cmd_list, description):
        """Handle Windows alternatives for Unix commands."""
        cmd = cmd_list[0]
        
        if cmd == 'mkdir':
            # Use Python's os.makedirs instead
            for directory in cmd_list[2:]:  # Skip 'mkdir' and '-p'
                try:
                    os.makedirs(directory, exist_ok=True)
                    print(f"   ✅ {description}: Created directory {directory}")
                except Exception as e:
                    print(f"   ❌ Failed to create {directory}: {e}")
        
        elif cmd == 'cp':
            # Use Python's shutil.copy
            try:
                files_to_copy = cmd_list[1:-1]  # All except last (destination)
                destination = cmd_list[-1]
                for file in files_to_copy:
                    if os.path.exists(file):
                        shutil.copy2(file, destination)
                print(f"   ✅ {description}: Copied files to {destination}")
            except Exception as e:
                print(f"   ❌ Copy failed: {e}")
        
        elif cmd == 'mv':
            # Use Python's shutil.move
            try:
                shutil.move(cmd_list[1], cmd_list[2])
                print(f"   ✅ {description}: Moved {cmd_list[1]} to {cmd_list[2]}")
            except Exception as e:
                print(f"   ❌ Move failed: {e}")
        
        elif cmd == 'rm':
            # Use Python's os.remove
            try:
                files_to_remove = [f for f in cmd_list[1:] if f != '-v']
                for file in files_to_remove:
                    if os.path.exists(file):
                        os.remove(file)
                        print(f"   ✅ {description}: Removed {file}")
            except Exception as e:
                print(f"   ❌ Remove failed: {e}")
        
        elif cmd == 'cat':
            # Use Python file reading
            try:
                if len(cmd_list) > 1 and os.path.exists(cmd_list[1]):
                    with open(cmd_list[1], 'r') as f:
                        content = f.read()
                        print(f"   ✅ {description}: File content preview:")
                        print(f"   {content.strip()}")
            except Exception as e:
                print(f"   ❌ File reading failed: {e}")

    def setup_environment(self):
        """Setup working directories and demonstrate mkdir command."""
        print("🔧 Setting up environment...")
        
        # Demonstrate mkdir command with multiple arguments
        directories = ["orders", "backups", "temp", "logs"]
        
        if self.is_windows:
            # Windows approach
            print("   (Windows environment detected - using Python alternatives)")
            for directory in directories:
                try:
                    os.makedirs(directory, exist_ok=True)
                    print(f"   ✅ Created directory: {directory}")
                except Exception as e:
                    print(f"   ❌ Failed to create {directory}: {e}")
        else:
            # Unix/Linux approach
            for directory in directories:
                self.run_command(["mkdir", "-p", directory], f"Create directory {directory}")
        
        # Create sample files to demonstrate other commands later
        sample_files = ["sample_order.txt", "config.txt", "readme.txt"]
        for file in sample_files:
            if not os.path.exists(file):
                try:
                    with open(file, "w") as f:
                        f.write(f"Sample content for {file}\nCreated: {datetime.now()}\nPlatform: {platform.system()}\n")
                    print(f"   ✅ Created sample file: {file}")
                except Exception as e:
                    print(f"   ❌ Failed to create {file}: {e}")

    def demonstrate_shell_commands(self):
        """Demonstrate various shell commands with multiple arguments."""
        print(f"\n🖥️  Demonstrating Shell Commands ({platform.system()}):")
        print("=" * 50)
        
        # 1. System and Shell Information
        print("1. System and Shell Information:")
        try:
            print(f"   Operating System: {platform.system()} {platform.release()}")
            print(f"   Python Version: {platform.python_version()}")
            
            if self.is_windows:
                # Windows shell information
                shell = os.environ.get('COMSPEC', 'cmd.exe')
                print(f"   Default Shell: {shell}")
                # Get current process info
                result = subprocess.run(['echo', '%PROCESSOR_ARCHITECTURE%'], shell=True, capture_output=True, text=True)
                if result.returncode == 0:
                    print(f"   Architecture: {result.stdout.strip()}")
            else:
                # Unix/Linux shell information
                shell = os.environ.get('SHELL', '/bin/sh')
                print(f"   Default Shell: {shell}")
                self.run_command(['echo', '$SHELL'], "Show shell variable")
                
        except Exception as e:
            print(f"   ❌ System info failed: {e}")

        # 2. Demonstrate directory listing (cross-platform)
        print("\n2. Directory Listing:")
        if self.is_windows:
            self.run_command(['dir'], "List directory contents")
        else:
            self.run_command(['ls', '-la'], "List directory contents with details")

        # 3. Demonstrate cp/copy command with multiple arguments
        print("\n3. Copy Command with multiple arguments:")
        source_files = ["sample_order.txt", "config.txt"]
        
        # Ensure backup directory exists
        if not os.path.exists("backups"):
            os.makedirs("backups", exist_ok=True)
        
        if self.is_windows:
            # Windows copy command
            for file in source_files:
                if os.path.exists(file):
                    self.run_command(['copy', file, 'backups\\'], f"Copy {file}")
        else:
            # Unix copy command
            existing_files = [f for f in source_files if os.path.exists(f)]
            if existing_files:
                cmd = ['cp'] + existing_files + ['backups/']
                self.run_command(cmd, "Copy multiple files")

        # 4. Demonstrate mv/move command
        print("\n4. Move Command:")
        try:
            # Create a temp file and move it
            temp_file = "temp_move_test.txt"
            with open(temp_file, "w") as f:
                f.write("Test file for move command demonstration")
            
            if not os.path.exists("temp"):
                os.makedirs("temp", exist_ok=True)
            
            if self.is_windows:
                self.run_command(['move', temp_file, 'temp\\'], f"Move {temp_file}")
            else:
                self.run_command(['mv', temp_file, 'temp/'], f"Move {temp_file}")
                
        except Exception as e:
            print(f"   ❌ Move demonstration failed: {e}")

        # 5. Demonstrate file viewing
        print("\n5. File Viewing Command:")
        if os.path.exists("readme.txt"):
            if self.is_windows:
                self.run_command(['type', 'readme.txt'], "Display file content")
            else:
                self.run_command(['cat', 'readme.txt'], "Display file content")

        # 6. Demonstrate rm/del command with options
        print("\n6. Remove Command with arguments:")
        try:
            # Create test files to remove
            test_files = ["test1.txt", "test2.txt"]
            for file in test_files:
                with open(file, "w") as f:
                    f.write("Test file for deletion demonstration")
            
            if self.is_windows:
                for file in test_files:
                    self.run_command(['del', file], f"Remove {file}")
            else:
                self.run_command(['rm', '-v'] + test_files, "Remove multiple files")
                
        except Exception as e:
            print(f"   ❌ Remove demonstration failed: {e}")

    def create_custom_aliases(self):
        """Create and demonstrate custom aliases."""
        print("\n🔧 Creating Custom Aliases:")
        print("=" * 30)
        
        if self.is_windows:
            # Windows batch file with aliases
            alias_script = """@echo off
REM Custom aliases for Lacrosse Shoe Customizer (Windows)
doskey ll=dir /A
doskey shoe_orders=cd orders ^& dir
doskey backup_orders=xcopy orders\\* backups\\ /Y 2^>nul ^|^| echo No orders to backup
doskey clean_temp=del temp\\* /Q 2^>nul ^& echo Temp directory cleaned
doskey shoe_status=echo Shoe Customizer Status: Active

echo Custom aliases loaded for Windows!
echo Available commands:
echo   ll - detailed file listing
echo   shoe_orders - navigate to orders directory  
echo   backup_orders - backup all orders
echo   clean_temp - clean temporary files
echo   shoe_status - show application status
"""
            filename = "shoe_aliases.bat"
        else:
            # Unix/Linux shell script with aliases
            alias_script = """#!/bin/bash
# Custom aliases for Lacrosse Shoe Customizer (Unix/Linux)
alias ll='ls -la'
alias shoe_orders='cd orders && ls -la'
alias backup_orders='cp orders/* backups/ 2>/dev/null || echo "No orders to backup"'
alias clean_temp='rm -rf temp/* && echo "Temp directory cleaned"'
alias shoe_status='echo "Shoe Customizer Status: Active"'

echo "Custom aliases loaded for Unix/Linux!"
echo "Available commands:"
echo "  ll - detailed file listing"
echo "  shoe_orders - navigate to orders directory"
echo "  backup_orders - backup all orders" 
echo "  clean_temp - clean temporary files"
echo "  shoe_status - show application status"
"""
            filename = "shoe_aliases.sh"
        
        try:
            with open(filename, "w") as f:
                f.write(alias_script)
            
            if not self.is_windows:
                os.chmod(filename, 0o755)
            
            print(f"✅ Created {filename} with custom aliases")
            print("   Available aliases:")
            print("   - ll: detailed file listing")
            print("   - shoe_orders: navigate to orders directory")
            print("   - backup_orders: backup all orders")
            print("   - clean_temp: clean temporary files")
            print("   - shoe_status: show application status")
            
            if self.is_windows:
                print(f"\n💡 To use: {filename}")
            else:
                print(f"\n💡 To use: source {filename}")
                
        except Exception as e:
            print(f"❌ Failed to create aliases: {e}")

    def customize_terminal_prompt(self):
        """Create custom terminal prompt configuration."""
        print("\n🎨 Customizing Terminal Prompt:")
        print("=" * 35)
        
        if self.is_windows:
            # Windows prompt customization
            prompt_script = """@echo off
REM Custom terminal prompt for Lacrosse Shoe Customizer (Windows)

REM Set colorful prompt with shoe emoji and current directory
prompt $E[35m👟 SHOE-CUSTOMIZER$E[0m $E[32m%USERNAME%@%COMPUTERNAME%$E[0m:$E[34m%CD%$E[0m$E[33m ⚡ $E[0m

echo Custom Windows prompt activated!
echo Prompt includes: 👟 emoji, username@computer, current directory, and ⚡ symbol
echo Colors: Purple brand, Green user info, Blue directory, Yellow prompt
"""
            filename = "custom_prompt.bat"
        else:
            # Unix/Linux prompt customization
            prompt_script = """#!/bin/bash
# Custom terminal prompt for Lacrosse Shoe Customizer (Unix/Linux)

# Colors
RED='\\[\\033[0;31m\\]'
GREEN='\\[\\033[0;32m\\]'
BLUE='\\[\\033[0;34m\\]'
YELLOW='\\[\\033[1;33m\\]'
PURPLE='\\[\\033[0;35m\\]'
NC='\\[\\033[0m\\]' # No Color

# Custom prompt with shoe emoji and current directory
export PS1="${PURPLE}👟 SHOE-CUSTOMIZER${NC} ${GREEN}\\u@\\h${NC}:${BLUE}\\w${NC}${YELLOW} ⚡ ${NC}"

# Alternative colorful prompt for continuation
export PS2="${RED}🏃 Enter more: ${NC}"

echo "Custom Unix/Linux prompt activated!"
echo "Prompt includes: 👟 emoji, username@hostname, current directory, and ⚡ symbol"
echo "Colors: Purple brand, Green user info, Blue directory, Yellow prompt"
"""
            filename = "custom_prompt.sh"
        
        try:
            with open(filename, "w") as f:
                f.write(prompt_script)
            
            if not self.is_windows:
                os.chmod(filename, 0o755)
            
            print(f"✅ Created {filename}")
            print("   Features:")
            print("   - 👟 Shoe emoji indicator")
            print("   - Color-coded username@hostname")
            print("   - Current directory display")
            print("   - ⚡ Lightning bolt prompt symbol")
            
            if self.is_windows:
                print(f"\n💡 To activate: {filename}")
            else:
                print(f"\n💡 To activate: source {filename}")
                
        except Exception as e:
            print(f"❌ Failed to create prompt customization: {e}")

    def demonstrate_shell_switching(self):
        """Demonstrate shell information and switching capabilities."""
        print("\n🔄 Shell Access and Switching:")
        print("=" * 35)
        
        try:
            if self.is_windows:
                print("📋 Windows Command Interpreters:")
                interpreters = ["cmd.exe", "powershell.exe", "pwsh.exe (PowerShell Core)"]
                for interpreter in interpreters:
                    print(f"   - {interpreter}")
                
                current_shell = os.environ.get('COMSPEC', 'cmd.exe')
                print(f"\n🐚 Current command interpreter: {current_shell}")
                
                # Create Windows shell switching demonstration
                switch_script = """@echo off
echo === Windows Shell Switching Demonstration ===
echo Current Command Interpreter: %COMSPEC%
echo Process ID: %RANDOM%

echo.
echo To switch command interpreters, you can use:
echo cmd         - Command Prompt (DOS-style)
echo powershell  - Windows PowerShell
echo pwsh        - PowerShell Core (if installed)
echo exit        - Return to previous interpreter

echo.
echo Example session:
echo ^> powershell
echo PS^> Write-Host "Now in PowerShell"
echo PS^> cmd  
echo ^> echo Now back in Command Prompt
echo ^> exit
echo PS^> exit
echo Back to original interpreter
"""
                filename = "shell_demo.bat"
            else:
                # Unix/Linux shells
                if os.path.exists("/etc/shells"):
                    with open("/etc/shells", "r") as f:
                        shells = f.readlines()
                    print("📋 Available shells on system:")
                    for shell in shells:
                        if shell.strip() and not shell.startswith("#"):
                            print(f"   - {shell.strip()}")
                
                current_shell = os.environ.get('SHELL', 'Unknown')
                print(f"\n🐚 Current default shell: {current_shell}")
                
                # Create Unix shell switching demonstration
                switch_script = """#!/bin/bash
echo "=== Unix/Linux Shell Switching Demonstration ==="
echo "Current shell: $SHELL"
echo "Process ID: $$"
echo "Parent Process ID: $PPID"

echo ""
echo "To switch shells, you can use:"
echo "bash    - Switch to Bash shell"
echo "zsh     - Switch to Zsh shell (if installed)"
echo "fish    - Switch to Fish shell (if installed)"
echo "tcsh    - Switch to TCSH shell (if installed)"
echo "exit    - Return to previous shell"

echo ""
echo "Example session:"
echo "$ bash"
echo "$ echo 'Now in Bash shell'"
echo "$ zsh"
echo "$ echo 'Now in Zsh shell'"
echo "$ exit"
echo "$ exit"
echo "Back to original shell"
"""
                filename = "shell_demo.sh"
            
            with open(filename, "w") as f:
                f.write(switch_script)
            
            if not self.is_windows:
                os.chmod(filename, 0o755)
            
            print(f"\n✅ Created {filename}")
            print(f"💡 Run with: {filename}")
            
        except Exception as e:
            print(f"❌ Shell demonstration failed: {e}")

    def read_settings_file(self) -> Dict[str, any]:
        """Reads customization settings from a file."""
        settings = {"theme": "default", "save_auto": False, "commands_demo": True}
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
            print("Settings file not loaded. Creating defaults...")
            # Create default settings file
            try:
                with open("settings.txt", "w") as f:
                    f.write("theme=default\n")
                    f.write("save_auto=false\n")
                    f.write("commands_demo=true\n")
            except Exception as e:
                print(f"Failed to create settings file: {e}")
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
        try:
            choice = int(input("Choose a number: ")) - 1
            if 0 <= choice < len(self.COLORS):
                self.color = self.COLORS[choice]
            else:
                print("Invalid choice. Setting to Red.")
                self.color = "Red"
        except ValueError:
            print("Invalid input. Setting to Red.")
            self.color = "Red"

        # Size
        try:
            self.size = float(input(f"Enter your shoe size ({self.MIN_SIZE}-{self.MAX_SIZE}): "))
            if not (self.MIN_SIZE <= self.size <= self.MAX_SIZE):
                print("Size out of range. Setting to default size 10.")
                self.size = 10.0
        except ValueError:
            print("Invalid size. Setting to default size 10.")
            self.size = 10.0

        # Traction
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

        # Support
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

        # Design
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
        """Calculates final price after support addons, discount, and tax."""
        addon = 20 if self.support == "High" else 10 if self.support == "Mid" else 0
        self.base_cost = 100 + addon
        discount_options = [(5, "Welcome"), (10, "Lucky Day"), (15, "Cross-Platform"), (0, "No Discount")]
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
        """Saves the order summary to a text file with timestamp."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join("orders", f"order_{timestamp}.txt")
        
        try:
            # Ensure orders directory exists
            os.makedirs("orders", exist_ok=True)
            
            with open(filename, "w") as f:
                f.write("TODDAVERY LACROSSE SHOE ORDER\n")
                f.write("=" * 35 + "\n")
                f.write(f"Order Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"Platform: {platform.system()} {platform.release()}\n")
                f.write(f"Name: {self.name}\n")
                f.write(f"Color: {self.color}\n")
                f.write(f"Size: {self.size}\n")
                f.write(f"Traction: {self.traction}\n")
                f.write(f"Support: {self.support}\n")
                f.write(f"Design: {self.design}\n")
                f.write(f"Discount: {self.discount}% - {self.discount_reason}\n")
                f.write(f"Final Price: ${self.final_price:.2f}\n")
                f.write("\nThank you for choosing Toddavery Lacrosse Shoes!\n")
            
            print(f"📝 Order saved to {filename}")
            print(f"📋 Order file created with {os.path.getsize(filename)} bytes")
            
        except Exception as e:
            print("❌ Error writing file:", e)

    def cleanup_demo_files(self):
        """Clean up demonstration files (optional)."""
        demo_files = ["sample_order.txt", "config.txt", "readme.txt"]
        choice = input("\n🧹 Clean up demo files? (yes/no): ").lower()
        
        if choice in ["yes", "y"]:
            try:
                for file in demo_files:
                    if os.path.exists(file):
                        os.remove(file)
                        print(f"   ✅ Removed {file}")
                print("✅ Demo files cleaned up")
            except Exception as e:
                print(f"❌ Cleanup failed: {e}")

def main():
    """Main application function."""
    try:
        customizer = LacrosseShoeCustomizer()
        customizer.clear_screen()
        
        print("🏁 Welcome to the Enhanced Toddavery Lacrosse Shoe Customizer!")
        print("   Cross-Platform with Command Demonstrations")
        print(f"   Running on: {platform.system()} {platform.release()}")
        print("=" * 65)
        
        # Demonstrate all required shell commands and features
        if customizer.settings.get("commands_demo", True):
            customizer.demonstrate_shell_commands()
            customizer.create_custom_aliases() 
            customizer.customize_terminal_prompt()
            customizer.demonstrate_shell_switching()
            
            input("\n📝 Press Enter to continue to shoe customization...")
            customizer.clear_screen()
        
        # Original shoe customization flow
        print("👟 Now let's customize your lacrosse shoes!")
        customizer.get_user_input()
        customizer.calculate_final_price()
        customizer.recommend_shoe()
        customizer.display_summary()
        customizer.write_order_to_file()
        customizer.cleanup_demo_files()
        
        print("\n🎉 Thank you for using the Toddavery Lacrosse Shoe Customizer!")
        print("📁 Check the generated files:")
        
        if customizer.is_windows:
            print("   - shoe_aliases.bat (custom aliases)")
            print("   - custom_prompt.bat (terminal customization)")
            print("   - shell_demo.bat (shell switching demo)")
        else:
            print("   - shoe_aliases.sh (custom aliases)")
            print("   - custom_prompt.sh (terminal customization)")
            print("   - shell_demo.sh (shell switching demo)")
        
        print("   - orders/ directory (your order)")
        print("   - settings.txt (application settings)")
        
    except KeyboardInterrupt:
        print("\n\n👋 Program interrupted by user. Goodbye!")
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")
        print("Please check your Python installation and try again.")

if __name__ == "__main__":
    main()