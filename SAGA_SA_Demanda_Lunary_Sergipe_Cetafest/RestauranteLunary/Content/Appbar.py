from turtle import width
from flet import (
    AppBar, ElevatedButton, Text, Row, 
    PopupMenuButton, PopupMenuItem, TextField, 
    Column, TextButton, Divider, icons, IconButton,
    Image, NavigationRailDestination, NavigationRail, Icon, FloatingActionButton, 
    colors, Container)
import base64
from Content.Colors import (Background, TextColor)
from Views.RouteConfig import RouteConfig
from Scripts.Autenticacao import Autenticacao, Deslogar

with open(f"Logo.png", "rb") as noB64:         
    Logo = base64.b64encode(noB64.read()).decode()

def Style_AppBar(page, auth, mobile):
    largura = page.width*0.6
    autenticado1 = PopupMenuItem(
            
                content=Text(
                    width=largura,
                    value="Login",
                    color=TextColor,
                    size=16
                    ),
                on_click=lambda _: RouteConfig(
                    page=page, 
                    route="/login"
                    )
                )
    autenticado2 = PopupMenuItem(
                
                    content=Text(
                        width=largura,
                        value="Registrar", 
                        color=TextColor, 
                        size=16
                        ),
                    on_click=lambda _: RouteConfig(
                        page=page, 
                        route="/registrar"
                        )
                    )
    AreaUsuario = TextField(
        hint_text="Usuário",
        width=200
        )
    AreaSenha = TextField(
        hint_text="Senha",
        width=200
        )
    if auth == 1:
        login = IconButton(
            icon=icons.LOGOUT,
            icon_size=40,
            icon_color=TextColor,
            on_click= lambda _: Deslogar(page)
            )
    else:
        login = PopupMenuButton(
            content=IconButton(
                icon=icons.SUPERVISED_USER_CIRCLE_ROUNDED,
                icon_size=40,
                icon_color=TextColor,
                disabled=True
            ),
            icon=None,
            items=[
                PopupMenuItem(
                    on_click=lambda _: RouteConfig(page=page, route="/login"),
                    content=Column(
                        width=200,
                        alignment="center",
                        controls=[
                            Text(
                                value="Você também pode clicar fora dos campos para acessar a página de login",
                                size=10
                                ),
                            Divider(height=5),
                            Text("Usuário:"),
                            AreaUsuario,
                            Text("Senha:"),
                            AreaSenha,
                            Row(
                                controls=[
                                    ElevatedButton(
                                        text="Logar",
                                        on_click=lambda _: Autenticacao(
                                            Usuario=AreaUsuario.value,
                                            Senha=AreaSenha.value, 
                                            page=page
                                            )
                                        ), 
                                    ElevatedButton(
                                        text="Registrar",
                                        on_click=lambda _: RouteConfig(
                                            page=page, 
                                            route="/registrar"
                                            )
                                        ),
                                    ]
                                )
                            ]
                        )
                    )
                ]
            )
    if mobile:
        if auth == 1:
            autenticado1 = PopupMenuItem(
            
                content=Text("Sair", width=largura,),
                on_click= lambda _: Deslogar(page))
            autenticado2 = PopupMenuItem(
            
                content=Text("Registrar", width=largura,),
                on_click=lambda _: RouteConfig(
                    page=page, 
                    route="/registrar"
                    )
                )
        bar_phone_or_desktop = AppBar(
            bgcolor=format(Background),
            toolbar_height=100,
            leading_width=150,
            leading=IconButton(
                on_click=lambda _: RouteConfig(
                page=page, 
                route="/home"
                ),
                content=Image(
                src_base64=Logo,
                fit="cover"
                )
                ),
            elevation=0,
            actions=[
                PopupMenuButton(
                
                    content=Icon(
                        name=icons.MENU_OPEN,
                        size=40,
                        color=TextColor
                        ),
                    items=[
                        autenticado1,
                        autenticado2,
                        PopupMenuItem(),
                        PopupMenuItem(
                        
                            content=Text(value="Inicio", color=TextColor, size=16),
                            on_click=lambda _: RouteConfig(
                                page=page, 
                                route="/home"
                                ),
                            ),
                        PopupMenuItem(
                        
                            content=Text(value="Cardápio", color=TextColor, size=16),
                            on_click=lambda _: RouteConfig(
                                page=page, 
                                route="/cardapio"
                                ),
                            ),
                        PopupMenuItem(
                        
                            content=Text(value="Contato", color=TextColor, size=16),
                            on_click=lambda _: RouteConfig(
                                page=page, 
                                route="/contato"
                                ),
                            ),
                        PopupMenuItem(
                        
                            content=Text(value="Sobre", color=TextColor, size=16),
                            on_click=lambda _: RouteConfig(
                                page=page, 
                                route="/sobre"
                                ),
                            ),
                        ]
                    ),
                ]
            )
    else:
        bar_phone_or_desktop = AppBar(
            bgcolor=format(Background),
            toolbar_height=100,
            leading_width=150,
            leading=IconButton(
                on_click=lambda _: RouteConfig(
                    page=page, 
                    route="/home"
                    ),
                content=Image(
                    src_base64=Logo,
                    fit="cover"
                )
                ),
            elevation=0,
            center_title=True,
            title=Row(
                width=400,
                spacing=20,
                controls=[
                    TextButton(
                        content=Text(value="Inicio", color=TextColor, size=16),
                        on_click=lambda _: RouteConfig(
                            page=page, 
                            route="/home"
                            ),
                        ),
                    TextButton(
                        content=Text(value="Cardápio", color=TextColor, size=16),
                        on_click=lambda _: RouteConfig(
                            page=page, 
                            route="/cardapio"
                            ),
                        ),
                    TextButton
                    (
                        content=Text(value="Contato", color=TextColor, size=16),
                        on_click=lambda _: RouteConfig(
                            page=page, 
                            route="/contato"
                            ),
                        ),
                    TextButton(
                        content=Text(value="Sobre", color=TextColor, size=16),
                        on_click= lambda _:RouteConfig(
                            page=page, 
                            route="/sobre"
                            ),
                        ),
                    ]
                ),
            actions=[
                Row(alignment="center", controls=[login]),
                ]
            )
    return bar_phone_or_desktop