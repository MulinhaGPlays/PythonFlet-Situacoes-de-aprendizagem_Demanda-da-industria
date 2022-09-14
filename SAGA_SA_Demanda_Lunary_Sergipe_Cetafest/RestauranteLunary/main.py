import flet
from flet import (Checkbox, Column, FloatingActionButton, IconButton, OutlinedButton, Page, Row, Tab, Tabs, Text, TextField, 
UserControl, colors, icons,)

class TodoApp(UserControl):
    def build(self):
        return Column()


def main(page: Page):
    page.title = "Restaurante Lunary"
    page.horizontal_alignment = "center"
    page.scroll = "adaptive"
    page.update()

    app = TodoApp()

    page.add(app)


flet.app(target=main)