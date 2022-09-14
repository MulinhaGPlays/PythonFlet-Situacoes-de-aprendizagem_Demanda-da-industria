import flet
from HTML import PageView
from flet import Page, View


def main(page: Page):


    def route(route):
        page.views.clear()
        match page.route:
            case "/":
                page.title = "Resturante Lunary"
                page.views.append(View(route="/", 
                                       controls=PageView(page=page).Page()
                                      ))
            case "/cardapio":
                page.title = "Cardápio"
                page.views.append(View(route="/cardapio", 
                                       controls=PageView(page=page).Page('cardapio')
                                       ))
            case "/contato":
                page.title = "Contato"
                page.views.append(View(route="/contato", 
                                       controls=PageView(page=page).Page('contato')
                                       ))
            case "/sobre":
                page.title = "Sobre"
                page.views.append(View(route="/sobre", 
                                       controls=PageView(page=page).Page('sobre')
                                       ))
            case _:
                page.title = "404"
                page.views.append(View(route="/Erro404", 
                                       controls=PageView(page=page).Page('404')
                                      ))
        page.update()

    page.on_route_change = route
    page.go(page.route)

flet.app(target=main, view=flet.WEB_BROWSER)