from Content.Appbar import Style_AppBar
from flet import View

def Contato(page):
    page.title = "Contato"
    page.views.append(View(route="/contato", controls=Style_AppBar(page),
                          )
                     )