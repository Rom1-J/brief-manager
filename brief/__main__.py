from rich.live import Live

from brief.core.layouts.base import BaseLayout
from brief.core.utils.console import console


def main() -> None:
    layout = BaseLayout()
    alive = True

    with Live(console=console) as live_table:
        while alive:
            live_table.update(layout)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        console.print_exception(
            show_locals=True, word_wrap=True, extra_lines=5
        )
