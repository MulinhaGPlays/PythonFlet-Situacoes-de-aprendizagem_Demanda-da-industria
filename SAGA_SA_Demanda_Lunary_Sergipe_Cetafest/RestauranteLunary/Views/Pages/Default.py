from Content.Appbar import Style_AppBar
from flet import View
from Views.RouteConfig import RouteConfig

def Default(page, auth):
    if auth == 1:
        RouteConfig(page=page, route='/home')
    page.title = "Restaurante Lunary"
    page.views.append(View(route="/",
                           controls=[Style_AppBar(page, auth),],
                          )
                     )