from flet import View
from Content.Styles.Login import build

def Login(page, auth, mobile):
    print(auth)
    page.title = "Login"
    page.views.append(View(route="/login",
                           horizontal_alignment="center",
                           vertical_alignment="center",
                           controls=[build(page).build(page)],))