from flet import (AppBar, ElevatedButton, Text, colors, Row, 
                  PopupMenuButton, PopupMenuItem, TextField, 
                  Column, TextButton, Divider)
from Views.RouteConfig import RouteConfig
from Scripts.Autenticacao import Autenticacao

def Style_AppBar(page):
    AreaUsuario = TextField(hint_text="Usuário",
                            width=200)
    AreaSenha = TextField(hint_text="Senha",
                          width=200)
    def Autenticar(e):
        Autenticacao(Usuario=AreaUsuario.value, Senha=AreaSenha.value, page=page)
    return AppBar(bgcolor=colors.SURFACE_VARIANT,
                  title=Row([TextButton(text="Inicio", 
                                        on_click=lambda _: RouteConfig(page=page, route="/home"),
                                        ),
                             TextButton(text="Cardapio", 
                                        on_click=lambda _: RouteConfig(page=page, route="/cardapio"),
                                        ),
                             TextButton(text="Contato", 
                                        on_click=lambda _: RouteConfig(page=page, route="/contato"),
                                        ),
                             TextButton(text="Sobre",
                                        on_click= lambda _:RouteConfig(page=page, route="/sobre"),
                                        ),]),
                  actions=[PopupMenuButton(items=[PopupMenuItem(on_click=lambda _: RouteConfig(page=page, 
                                                                                     route="/login"),
                                                                content=Column(width=200,
                                                                               alignment="center",
                                                                               controls=[Text(value="Você também pode clicar fora dos campos para acessar a página de login",
                                                                                              size=10),
                                                                                         Divider(height=5),
                                                                                         Text("Usuário:"),
                                                                                         AreaUsuario,
                                                                                         Text("Senha:"),
                                                                                         AreaSenha,
                                                                                         Row(controls=[ElevatedButton(text="Logar", on_click=Autenticar), 
                                                                                                       ElevatedButton(text="Registrar", on_click=lambda _: RouteConfig(page=page, route="/registrar")),])]))])])
           