from Content.Appbar import Style_AppBar
from flet import View

def Erro404(page, auth):
    page.title = "404"
    page.views.append(View(route="/erro404", controls=[Style_AppBar(page, auth),]
                          )
                     )