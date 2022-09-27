from Content.Appbar import Style_AppBar
from Content.Styles.Cardapio import filtro
from flet import View, Column

def Cardapio(page, auth):          
    page.title = "Cardapio"
    page.views.append(
        View(
            route="/cardapio", 
            padding=0,
            scroll='always',
            controls=[
                Style_AppBar(page, auth), 
                filtro(page),
                ]
            )
        )