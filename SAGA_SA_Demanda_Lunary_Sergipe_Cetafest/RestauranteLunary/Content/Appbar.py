from flet import AppBar, ElevatedButton, Text, colors, Row, PopupMenuButton, PopupMenuItem, TextField, Column
from Views.RouteConfig import RouteConfig
from Scripts.Autenticacao import Autenticar

def Style_AppBar(page):
    return [
            AppBar(bgcolor=colors.SURFACE_VARIANT,
                   title=Row([ElevatedButton(text="Inicio", 
                                             on_click=RouteConfig(page=page, route="/home"),
                                            ),
                              ElevatedButton(text="Cardapio", 
                                             on_click=RouteConfig(page=page, route="/cardapio"),
                                            ),
                              ElevatedButton(text="Contato", 
                                             on_click=RouteConfig(page=page, route="/contato"),
                                            ),
                              ElevatedButton(text="Sobre", 
                                             on_click=RouteConfig(page=page, route="/sobre"),
                                            ),
                            ]),
                   actions=[PopupMenuButton(items=[PopupMenuItem(on_click=RouteConfig(page=page, route="/login"),
                                                                 content=Column([Text("Usuário:"),
                                                                                 TextField(hint_text="Usuário"),
                                                                                 Text("Senha:"),
                                                                                 TextField(hint_text="Senha"),
                                                                                 ElevatedButton(text="Logar", 
                                                                                                on_click=Autenticar()),]))])
                           ]
                  ),
           ]

def Style_AppBarD(page):
    return [
            AppBar(bgcolor=colors.SURFACE_VARIANT,
                   title=Row([ElevatedButton(text="Inicio", 
                                             on_click=RouteConfig(page=page, route="/home"),
                                            ),
                              ElevatedButton(text="Contato", 
                                             on_click=RouteConfig(page=page, route="/contato"),
                                            ),
                              ElevatedButton(text="Sobre", 
                                             on_click=RouteConfig(page=page, route="/sobre"),
                                            ),
                            ]),
                   actions=[PopupMenuButton(items=[PopupMenuItem(on_click=RouteConfig(page=page, route="/login"),
                                                                 content=Column([Text("Usuário:"),
                                                                                 TextField(hint_text="Usuário"),
                                                                                 Text("Senha:"),
                                                                                 TextField(hint_text="Senha"),
                                                                                 ElevatedButton(text="Logar", 
                                                                                                on_click=Autenticar()),]))])
                           ]
                  ),
           ]