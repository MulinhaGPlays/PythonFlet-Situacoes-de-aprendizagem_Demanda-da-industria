from Models.Database import Database as db
from Views.RouteConfig import RouteConfig

def Autenticacao(Usuario, Senha, page):
    db.SELECT(COLUMN=['Usuario', 'Senha'], TABLE='UsuarioLunary')
    rows = db.FETCHALL()
    for row in rows:
        if row.Usuario == Usuario:
            if row.Senha == Senha:
                db.UPDATE(TABLE='SessaoDoDispositivo', 
                          COLUMN='Autenticado', VALUES='1', 
                          COLUMNCond='CodSessao', Operator='=', Condition=page.session_id)
                RouteConfig(page=page, route="/home")
                
def Registro(Usuario, Senha, IdRestaurante, CodFuncionario, page):
    db.SELECT(COLUMN=['Id', 'CodFuncionario'], TABLE=['RedeRestaurantes', 'Funcionario'])
    rows = db.FETCHALL()
    for row in rows:
        if row.Id == IdRestaurante:
            if row.CodFuncionario == CodFuncionario:
                db.INSERT_INTO(COLUMN=['Usuario', 'Senha', 'IdRestaurante', 'CodFuncionario'], TABLE='UsuarioLunary', VALUES=[f"'{Usuario}'", f"'{Senha}'", f"'{IdRestaurante}'", f"'{CodFuncionario}'"])
                db.UPDATE(TABLE='SessaoDoDispositivo', 
                          COLUMN='Autenticado', VALUES='1', 
                          COLUMNCond='CodSessao', Operator='=', Condition=page.session_id)
                RouteConfig(page=page, route="/home")
                
def Deslogar(page):
    db.UPDATE(TABLE='SessaoDoDispositivo', 
              COLUMN='Autenticado', VALUES='0', 
              COLUMNCond='CodSessao', Operator='=', Condition=page.session_id)
    RouteConfig(page=page, route="/")
