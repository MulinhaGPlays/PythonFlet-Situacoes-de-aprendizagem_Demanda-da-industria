from Content.Appbar import Style_AppBar
from Content.Styles.Cardapio import build
from flet import View

def Cardapio(page):
    page.title = "Cardapio"
    page.views.append(View(route="/cardapio", 
                           controls=[Style_AppBar(page), 
                                     build(page)]
                          )
                     )