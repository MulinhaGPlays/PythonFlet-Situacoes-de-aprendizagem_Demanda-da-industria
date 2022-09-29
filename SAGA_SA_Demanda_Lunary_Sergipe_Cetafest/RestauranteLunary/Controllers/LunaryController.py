from Models.Database import Database as db
from Views.View import View
from flet import Page

db.DELETE(TABLE='SessaoDoDispositivo')

def main(page: Page):
    
    def route(route):
        mobile = True if page.width <= 668.0 else False
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
                View(page, auth, mobile).Default()
            case "/home":
                View(page, auth, mobile).Home()
            case "/cardapio":
                View(page, auth, mobile).Cardapio()
            case "/contato":
                View(page, auth, mobile).Contato()
            case "/sobre":
                View(page, auth, mobile).Sobre()
            case "/login":
                View(page, auth, mobile).Login()
            case "/registrar":
                View(page, auth, mobile).Registrar()
            case _:
                View(page, 0, mobile).Erro404()
        page.update()

    page.on_route_change = route
    db.SELECT_WHERE(TABLE='SessaoDoDispositivo', COLUMN='CodSessao', COLUMNCond='CodSessao', Operator='=', Condition=f'{page.session_id}')
    if db.FETCHALL() == []:
        db.INSERT_INTO(TABLE='SessaoDoDispositivo', COLUMN='CodSessao', VALUES=f"'{page.session_id}'")
    page.go(page.route)
    page.on_resize = route
    