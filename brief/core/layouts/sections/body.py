from rich.layout import Layout
from rich.panel import Panel
from rich.syntax import Syntax

LAYOUT_NAME = "body"
FILE = "venv/lib/python3.9/site-packages/isort/profiles.py"


class BodyLayout(Layout):
    def __init__(self):
        syntax = Syntax.from_path(
            FILE,
            line_numbers=True,
        )
        panel = Panel(syntax, title=FILE)

        super().__init__(panel, name=LAYOUT_NAME, ratio=5)
