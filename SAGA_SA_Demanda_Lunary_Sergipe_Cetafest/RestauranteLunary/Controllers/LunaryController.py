from Models.Database import Database as db
from Views.View import View
from flet import Page

db.DELETE(TABLE='SessaoDoDispositivo')

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
            case "/registrar":
                View(page).Registrar()
            case _:
                View(page).Erro404()
        page.update()

    page.on_route_change = route
    db.SELECT_WHERE(TABLE='SessaoDoDispositivo', COLUMN='CodSessao', COLUMNCond='CodSessao', Operator='=', Condition=f'{page.session_id}')
    if db.FETCHALL() == []:
        db.INSERT_INTO(TABLE='SessaoDoDispositivo', COLUMN='CodSessao', VALUES=f"'{page.session_id}'")
    page.go(page.route)
    