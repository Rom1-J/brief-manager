from rich.layout import Layout
from rich.panel import Panel

LAYOUT_NAME = "side"


class SidebarLayout(Layout):
    def __init__(self):
        panel = Panel(LAYOUT_NAME, title=LAYOUT_NAME)

        super().__init__(panel, name=LAYOUT_NAME, ratio=1)
