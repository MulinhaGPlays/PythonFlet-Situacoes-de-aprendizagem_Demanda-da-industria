from flet import View
from Content.Styles.Login import build
from Content.Appbar import Style_AppBar

def Login(page, auth, mobile):
    page.title = "Login"
    page.views.append(View(route="/login",
                           horizontal_alignment="center",
                           vertical_alignment="center",
                           appbar=Style_AppBar(page, auth, mobile),
                           controls=[build(page).build(page, mobile)],))