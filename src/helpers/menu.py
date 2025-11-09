from InquirerPy import inquirer
from rich.console import Console
from helpers import definitions as d
import os

class Menu:
    def __init__(self):
        self.console = Console()

    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def menu_return_message(self):
        input("\nPress Enter to return to the menu...")

    def main_menu(self):
        choices = [
            "Polars Definitions",
            "Examples",
            "Spark Comparison",
            "Exit",
        ]

        while True:
            self.clear_screen()
            self.console.print("[red3]Welcome in Polars Demo[/]")

            result = inquirer.select(
                message="To learn something about this library, select an option below:",
                choices=choices,
                pointer=">",
                instruction="use arrow keys and Enter\n",
                qmark=""
            ).execute()

            self.clear_screen()

            if result == "Polars Definitions":
                self.polars_menu()
            elif result == "Examples":
                print("Examples here")
                self.menu_return_message()
            elif result == "Spark Comparison":
                print("Check the comparison here")
                self.menu_return_message()
            elif result == "Exit":
                break
            

    def polars_menu(self):
        choices = [
            "Base Definition",
            "Key Features",
            "Philosophy",
            "Example",
            "Back",
        ]

        hd = d.DefinitionHelper()

        while True:
            self.clear_screen()
            self.console.print("[red3]Check out the key informations below[/]")
            result = inquirer.select(
                message="Select an option below:",
                choices=choices,
                pointer=">",
                instruction="use arrow keys and Enter",
                qmark=""
            ).execute()

            self.clear_screen()

            if result == "Base Definition":
                hd.base_definition()
                self.menu_return_message()
            elif result == "Key Features":
                hd.key_features()
                self.menu_return_message()
            elif result == "Philosophy":
                hd.philosophy()
                self.menu_return_message()
            elif result == "Example":
                hd.example()
                self.menu_return_message()
            elif result == "Back":
                break
