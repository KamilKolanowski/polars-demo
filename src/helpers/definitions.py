from rich.console import Console
from rich.panel import Panel

def polars_definition():
    console = Console()

    console.print(Panel("""
        
        An [sea_green2]open-source[/] library for data manipulation, 
        known for being one of the fastest data processing solutions on a single machine.

        It features a well-structured, typed API that is both expressive and easy to use.
        
            [yellow]⚡️[/] [dodger_blue2]Fast[/] - Polars is written from the ground up with performance in mind. 
                      Its multi-threaded query engine is written in Rust 
                      and designed for effective parallelism. 
                      Its vectorized and columnar processing enables cache-coherent 
                      algorithms and high performance on modern processors.
                        
            [yellow]⚡️[/] [dodger_blue2]Easy to use[/] - You will feel right at home with Polars if you are familiar with data wrangling. 
                             Its expressions are intuitive and empower you to write code 
                             which is readable and performant at the same time.
                        
            [yellow]⚡️[/] [dodger_blue2]Open source[/] - Polars is and always will be open source. Driven by an active community of developers, 
                             everyone is encouraged to add new features and contribute. 
                             Polars is free to use under the MIT license.
        """, title="[red]Polars"))