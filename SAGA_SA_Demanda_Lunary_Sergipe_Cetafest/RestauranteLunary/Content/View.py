from flet import View
from Content.Appbar import Style_AppBar

def View_Style(route, page, auth, html):
    return View(
        route=route,
        padding=0,
        spacing=40,
        scroll="always",
        bgcolor=format("#E67716"),
        vertical_alignment="center",
        horizontal_alignment="center",
        appbar=Style_AppBar(page, auth),
        controls=html,
        )