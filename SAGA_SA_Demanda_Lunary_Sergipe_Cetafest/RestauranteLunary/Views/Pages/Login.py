from flet import View

def Login(page):
    page.title = "Login"
    page.views.append(View(route="/login",))