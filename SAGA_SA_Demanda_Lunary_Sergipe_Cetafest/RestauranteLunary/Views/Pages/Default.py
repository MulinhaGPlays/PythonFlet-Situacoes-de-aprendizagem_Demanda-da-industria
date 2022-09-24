from Content.Appbar import Style_AppBar
from flet import View

def Default(page, auth):
    print(auth)
    page.title = "Restaurante Lunary"
    page.views.append(View(route="/",
                           controls=[Style_AppBar(page),],
                          )
                     )