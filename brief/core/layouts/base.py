from rich.layout import Layout

from .sections import BodyLayout, FooterLayout, HeaderLayout, SidebarLayout


class BaseLayout(Layout):
    def __init__(self):
        super().__init__()

        self.split_column(
            self.header(),
            self.main(),
            self.footer(),
        )

    @staticmethod
    def header() -> HeaderLayout:
        return HeaderLayout()

    @staticmethod
    def main() -> Layout:
        main = Layout()
        main.split_row(SidebarLayout(), BodyLayout())

        return main

    @staticmethod
    def footer() -> FooterLayout:
        return FooterLayout()
