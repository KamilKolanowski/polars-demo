from rich.console import Console
from rich.panel import Panel
from rich.align import Align
import textwrap

class DefinitionHelper:
    BULLET = "[yellow]⚡️[/]"
    BASE_INDENT = "    "
    SECTION_INDENT = "        "
    PANEL_PADDING = (1, 4)
    PANEL_MARGIN = 4

    def __init__(self):
        self.console = Console()

    def hanging_bullet(self, text, bullet=None, indent=None, width=None):
        bullet = bullet if bullet is not None else self.BULLET
        indent = indent if indent is not None else self.BASE_INDENT
        panel_width = width if width is not None else self.console.width - self.PANEL_MARGIN * 2
        wrap_width = panel_width - len(bullet)

        wrapped = textwrap.wrap(text, width=wrap_width)
        if not wrapped:
            return bullet
        lines = [bullet + wrapped[0]]
        lines += [indent + line for line in wrapped[1:]]
        return "\n".join(lines)

    def format_bullet_section(self, bullets, indent=None, width=None):
        indent = indent if indent is not None else self.BASE_INDENT
        panel_width = width if width is not None else self.console.width - self.PANEL_MARGIN * 2
        bullet_texts = [
            self.hanging_bullet(b, bullet=self.BULLET, indent=indent, width=panel_width - self.PANEL_MARGIN * 2)
            for b in bullets
        ]
        return "\n\n".join(bullet_texts)

    def print_bullet_panel(self, title, bullets, prolog=None, indent=None):
        panel_width = self.console.width - self.PANEL_MARGIN
        body = ""
        if prolog:
            body += prolog.strip() + "\n\n"
        body += self.format_bullet_section(bullets, indent=indent, width=panel_width)
        panel = Panel(
            Align.left(body),
            title=title,
            width=panel_width,
            padding=self.PANEL_PADDING
        )
        self.console.print(panel)

    def base_definition(self):
        prolog = """
An [sea_green2]open-source[/] library for data manipulation,
known for being one of the fastest data processing solutions on a single machine.

It features a well-structured, typed API that is both expressive and easy to use.
""".strip()
        bullets = [
            ("[dodger_blue2]Fast[/] - Polars is written from the ground up with performance in mind. "
             "Its multi-threaded query engine is written in Rust and designed for effective parallelism. "
             "Its vectorized and columnar processing enables cache-coherent algorithms and high performance on modern processors."),
            ("[dodger_blue2]Easy to use[/] - You will feel right at home with Polars if you are familiar with data wrangling. "
             "Its expressions are intuitive and empower you to write code which is readable and performant at the same time."),
            ("[dodger_blue2]Open source[/] - Polars is and always will be open source. Driven by an active community of developers, "
             "everyone is encouraged to add new features and contribute. Polars is free to use under the MIT license.")
        ]
        title = "[red][link=https://pola.rs]Polars[/link]"
        self.print_bullet_panel(title, bullets, prolog=prolog, indent=self.BASE_INDENT)

    def key_features(self):
        bullets = [
            "[dodger_blue2]Fast[/] - Written from scratch in Rust, designed close to the machine and without external dependencies.",
            "[dodger_blue2]I/O[/] - First class support for all common data storage layers: local, cloud storage & databases.",
            "[dodger_blue2]Intuitive API[/] - Write your queries the way they were intended. Polars, internally, will determine the most efficient way to execute using its query optimizer.",
            "[dodger_blue2]Out of Core[/] - The streaming API allows you to process your results without requiring all your data to be in memory at the same time.",
            "[dodger_blue2]Parallel[/] - Utilises the power of your machine by dividing the workload among the available CPU cores without any additional configuration.",
            "[dodger_blue2]Vectorized Query Engine[/]",
            "[dodger_blue2]GPU Support[/] - Optionally run queries on NVIDIA GPUs for maximum performance for in-memory workloads.",
            "[dodger_blue2]Apache Arrow support[/] - Polars can consume and produce Arrow data often with zero-copy operations. Note that Polars is not built on a Pyarrow/Arrow implementation. Instead, Polars has its own compute and buffer implementations.",
        ]
        title = "[red]Key Features"
        self.print_bullet_panel(title, bullets, indent=self.SECTION_INDENT)

    def philosophy(self):
        bullets = [
            "Utilizes all available cores on your machine.",
            "Optimizes queries to reduce unneeded work/memory allocations.",
            "Handles datasets much larger than your available RAM.",
            "A consistent and predictable API.",
            "Adheres to a strict schema (data-types should be known before running the query).",
        ]
        title = "[red]Philosophy"
        self.print_bullet_panel(title, bullets, indent=self.SECTION_INDENT)
