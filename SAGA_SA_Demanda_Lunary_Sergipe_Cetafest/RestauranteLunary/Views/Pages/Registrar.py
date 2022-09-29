from flet import View
from Content.Styles.Registrar import build

def Registrar(page, auth, mobile):
    print(auth)
    page.title = "Registrar"
    page.views.append(View(route="/registrar",
                           horizontal_alignment="center",
                           vertical_alignment="center",
                           controls=[build(page)],))