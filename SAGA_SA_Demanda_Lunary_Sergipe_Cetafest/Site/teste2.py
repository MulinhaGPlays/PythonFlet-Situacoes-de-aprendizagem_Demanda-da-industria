import flet
import pages
from flet import Page, View


def main(page: Page):
    page.title = "Routes Example"

    def route(route):
        page.views.clear()
        match page.route:
            case "/":
                page.views.append(View(route="/", controls=pages.Home(route=lambda _: page.go("/store"))))
            case "/store":
                page.views.append(View(route="/store", controls=pages.Store(route=lambda _: page.go("/"))))
            case _:
                page.views.append(View(route="/Erro404", controls=pages.Erro(route=lambda _: page.go("/"))))
        page.update()

    page.on_route_change = route
    page.go(page.route)


flet.app(target=main, view=flet.WEB_BROWSER)