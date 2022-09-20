from Content.Appbar import Style_AppBar
from Content.Styles.Cardapio import filtro
from flet import View, Column

def Cardapio(page):
    page.title = "Cardapio"
    page.views.append(
        View(
            route="/cardapio", 
            controls=[
                Style_AppBar(page), 
                filtro(page),
                ]
            )
        )