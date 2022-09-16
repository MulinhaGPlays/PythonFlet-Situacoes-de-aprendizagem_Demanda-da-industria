from Views.View import View
from flet import Page


def main(page: Page):

    def route(route):
        page.views.clear()
        match page.route:
            case "/":
                View(page).Default()
            case "/home":
                View(page).Home()
            case "/cardapio":
                View(page).Cardapio()
            case "/contato":
                View(page).Contato()
            case "/sobre":
                View(page).Sobre()
            case "/login":
                View(page).Login()
            case _:
                View(page).Erro404()
        page.update()

    page.on_route_change = route
    page.scroll = "adaptive"
    page.go(page.route)