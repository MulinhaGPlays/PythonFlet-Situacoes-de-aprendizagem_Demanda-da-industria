from flet import View
from Content.Styles.Registrar import build
from Content.Appbar import Style_AppBar

def Registrar(page, auth, mobile):
    page.title = "Registrar"
    page.views.append(View(route="/registrar",
                           horizontal_alignment="center",
                           vertical_alignment="center",
                           appbar=Style_AppBar(page, auth, mobile),
                           controls=[build(page).build(mobile)],))