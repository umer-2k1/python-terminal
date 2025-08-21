from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.rule import Rule
from rich.text import Text
import pyfiglet

console = Console()

PRIMARY = "#b26349"

def display_intro(): 

    console.print()
    console.print(
        Panel.fit(
            f"[bold white]* Welcome to [{PRIMARY}]MEDIA AGENT[/{PRIMARY}] *[/bold white]",
            border_style=PRIMARY,
            padding=(0, 2),
        )
    )

    # Banner
    banner = pyfiglet.figlet_format("MEDIA AGENT", font="ansi_shadow", width=200) 
    console.print()
    console.print(banner, style=f"{PRIMARY} bold")
    # console.print(Rule(style="#b26349"))

    welcome_text = """[bold cyan]Welcome to MEDIA AGENT[/bold cyan]

This tool helps you:
🔎 Search Twitter & Reddit  
💬 Chat with extracted content  
📝 Summarize & get insights  
💡 Generate conversation ideas  
"""
    title_text = Text("About", style=f"bold {PRIMARY}")
    console.print(
        Panel(
            welcome_text,
            # border_style="#FF5733",
            title=title_text,
            padding=(1, 2),
            expand=False,
            # style="on #1e1e1e",   
        )
    )

def display_menu():
    # Create menu table
    console.print()
    table = Table(title="✨ Main Menu ✨", header_style="bold magenta", show_lines=True)
    table.add_column("Option", style="cyan", justify="center")
    table.add_column("Description", style=PRIMARY)

    table.add_row("1", "🔎 Search Twitter")
    table.add_row("2", "📢 Search Reddit")
    table.add_row("3", "📝 Summarize Content")
    table.add_row("4", "🤖 Chat with Media Agent")
    table.add_row("5", "❌ Exit")

    console.print(table)

if __name__ == "__main__":
    display_intro()
    display_menu()
    # console.print(Rule(style="#FF5733"))
    choice = console.input("[bold green]Enter your choice ➜ [/bold green]")
    console.print(f"You selected: [bold {PRIMARY}]{choice}[/bold {PRIMARY}]")
