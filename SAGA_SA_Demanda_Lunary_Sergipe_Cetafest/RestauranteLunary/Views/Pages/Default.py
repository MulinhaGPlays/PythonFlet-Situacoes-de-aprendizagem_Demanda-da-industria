from Content.View import View_Style
from  Content.Styles.Default import TextContainer, Cardapio
from flet import Column, Row, Alignment
from Views.RouteConfig import RouteConfig

def Default(page, auth, mobile):
    if auth == 1:
        return RouteConfig(page=page, route='/home')
    page.title = "Restaurante Lunary"
    page.views.append(View_Style("/", page, auth, html(page, auth, mobile).body(), mobile))
    
class html:
    def __init__(head, page, auth, mobile):
        head.page = page
        head.auth = auth
        head.mobile = mobile
    def body(head):
        dados = [
            TextContainer(head),
            Cardapio(head),
            ]
        if head.mobile:
            site = Column(
                horizontal_alignment="center",
                controls=dados
                    )
        else: 
            site = Row(
                alignment="center",
                controls=dados
            )
        return [
            Column(
                controls=[
                    site
                ]
            )
            ]