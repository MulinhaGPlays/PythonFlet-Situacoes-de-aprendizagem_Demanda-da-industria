from Content.View import View_Style
from  Content.Styles.Default import TextContainer, Cardapio
from flet import Column, Row, Alignment
from Views.RouteConfig import RouteConfig

def Default(page, auth, mobile):
    if auth == 1:
        return RouteConfig(page=page, route='/home')
    page.title = "Restaurante Lunary"
    page.views.append(View_Style("/", page, auth, html(page, auth).body(), mobile))
    
class html:
    def __init__(head, page, auth):
        head.page = page
        head.auth = auth
    def body(head):
        return [
            Column(
                controls=[
                    Row(
                        alignment="center",
                        controls=[
                            TextContainer(head),
                            Cardapio(head),
                        ]
                    )
                ]
            )
            ]

