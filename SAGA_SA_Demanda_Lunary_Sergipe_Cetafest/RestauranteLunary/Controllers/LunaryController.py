from Models.Database import Database as db
from Views.View import View
from flet import Page

db.DELETE(TABLE='SessaoDoDispositivo')

def main(page: Page):
    
    def route(route):
        db.SELECT_WHERE(TABLE='SessaoDoDispositivo', 
                        COLUMN='Autenticado', 
                        COLUMNCond='CodSessao', Operator='=', Condition=page.session_id)
        auth = 0
        for row in db.FETCHALL():
            if row.Autenticado == 1:
                auth = 1
        page.views.clear()
        match page.route:
            case "/":
                View(page, auth).Default()
            case "/home":
                View(page, auth).Home()
            case "/cardapio":
                View(page, auth).Cardapio()
            case "/contato":
                View(page, auth).Contato()
            case "/sobre":
                View(page, auth).Sobre()
            case "/login":
                View(page, auth).Login()
            case "/registrar":
                View(page, auth).Registrar()
            case _:
                View(page, 0).Erro404()
        page.update()

    page.on_route_change = route
    db.SELECT_WHERE(TABLE='SessaoDoDispositivo', COLUMN='CodSessao', COLUMNCond='CodSessao', Operator='=', Condition=f'{page.session_id}')
    if db.FETCHALL() == []:
        db.INSERT_INTO(TABLE='SessaoDoDispositivo', COLUMN='CodSessao', VALUES=f"'{page.session_id}'")
    page.go(page.route)
    page.on_resize = page.update()
    