from Content.Appbar import Style_AppBar
from flet import View

def Sobre(page, auth):
    print(auth)
    page.title = "Sobre"
    page.views.append(View(route="/sobre", controls=[Style_AppBar(page),]
                          )
                     )