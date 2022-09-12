import base64
import flet
from CSS import appBar, Images
from flet import (Image, Page, Row, border_radius, Container, colors, alignment, padding, Text, LinearGradient,
                  ShaderMask, Column, AppBar, Icon, IconButton, Page, PopupMenuButton, PopupMenuItem, icons,)

def main(page: Page):
    
    with open('Site/Logo.png', 'rb') as noB64:
        img_ = base64.b64encode(noB64.read()).decode()
    
    def check_item_clicked(e):
        e.control.checked = not e.control.checked
        page.update()
    def toggle_theme(e):
        page.theme_mode = "dark" if page.theme_mode == "light" else "light"
        page.update()
    
    page.title = "Images Example"
    page.theme_mode = "light"
    page.padding = 0
    page.appbar = appBar(img_, toggle_theme, check_item_clicked)
    page.update()


    images = Row(expand=1, wrap=False, scroll="always")

    page.add(images)

    for i in range(0, 30):
        images.controls.append(Images(i))
    page.update()

flet.app(target=main)

