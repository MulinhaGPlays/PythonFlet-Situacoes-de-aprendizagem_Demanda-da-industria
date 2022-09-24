from Content.Appbar import Style_AppBar
from flet import View

def Home(page, auth):
    print(auth)
    page.title = "Home"
    page.views.append(View(route="/home", controls=[Style_AppBar(page),]
                          )
                     )