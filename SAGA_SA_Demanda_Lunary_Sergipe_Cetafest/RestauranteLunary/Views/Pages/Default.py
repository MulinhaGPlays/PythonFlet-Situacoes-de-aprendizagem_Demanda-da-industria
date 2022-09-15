from Content.Appbar import Style_AppBarD
from flet import View

def Default(page):
    page.title = "Resturante Lunary"
    page.views.append(View(route="/", controls=Style_AppBarD(page),
                          )
                     )