from pydoc import pager
from Content.Appbar import Style_AppBar
from  Content.Styles.Default import TextContainer, Cardapio
from flet import View, Column, Row, Alignment
from Views.RouteConfig import RouteConfig

def Default(page, auth):
    if auth == 1:
        RouteConfig(page=page, route='/home')
    page.title = "Restaurante Lunary"
    page.views.append(
        View(
            route="/",
            padding=0,
            spacing=40,
            scroll="always",
            bgcolor=format("#DB895C"),
            vertical_alignment="center",
            horizontal_alignment="center",
            appbar=Style_AppBar(page, auth),
            controls=html(page, auth).body(),
            )
        )
    
class html:
    def __init__(head, page, auth):
        head.page = page
        head.auth = auth
    def body(head):
        return [
            Row(
                alignment="center",
                controls=[
                    TextContainer(head),
                    Cardapio(head),
                ]
            )
            ]

