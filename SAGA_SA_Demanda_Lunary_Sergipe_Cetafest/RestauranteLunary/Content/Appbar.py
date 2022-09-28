from flet import (
    AppBar, ElevatedButton, Text, Row, 
    PopupMenuButton, PopupMenuItem, TextField, 
    Column, TextButton, Divider, icons, IconButton,
    Image)
import base64
from Content.Colors import (Background, TextColor)
from Views.RouteConfig import RouteConfig
from Scripts.Autenticacao import Autenticacao, Deslogar

with open(f"Logo.png", "rb") as noB64:         
    Logo = base64.b64encode(noB64.read()).decode()

def Style_AppBar(page, auth):
    AreaUsuario = TextField(
        hint_text="Usuário",
        width=200
        )
    AreaSenha = TextField(
        hint_text="Senha",
        width=200
        )
    if auth == 1:
        login = ElevatedButton(
            text='Fazer Logout',
            on_click= lambda _: Deslogar(page)
            )
    else:
        login = PopupMenuButton(
            icon=icons.SUPERVISED_USER_CIRCLE,
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
    return AppBar(
        bgcolor=format(Background),
        toolbar_height=100,
        leading_width=150,
        leading=IconButton(
            content=Image(
                src_base64=Logo,
                fit="cover"
            )
            ),
        elevation=0,
        center_title=True,
        title=Row(
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
            login,
            ]
        )