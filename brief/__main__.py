from brief.core.utils.console import console


def main() -> None:
    print("Hello World!")


if __name__ == "__main__":
    try:
        main()
    except Exception:
        console.print_exception(
            show_locals=True, word_wrap=True, extra_lines=5
        )
