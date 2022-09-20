from flet import Container, Column, Text, alignment, colors, UserControl, Image, ElevatedButton, TextField
from Scripts.Autenticacao import Autenticacao
import base64

class build(UserControl):
    def build(self):
        return self.LoginArea()
    
    def LoginArea(self):
        with open(f"RestauranteLunary\Logo.png", "rb") as noB64:         
            Logo = base64.b64encode(noB64.read()).decode()
        AreaUsuario = TextField(hint_text="Usuário",
                                width=200)
        AreaSenha = TextField(hint_text="Senha",
                              width=200)
        def Autenticar(e):
            Autenticacao(Usuario=AreaUsuario.value, 
                         Senha=AreaSenha.value)
        return Container(padding=10,
                         alignment=alignment.center,
                         bgcolor=colors.BLUE,
                         border_radius=10,
                         width=300,
                         content=Column(horizontal_alignment="center",
                                        controls=[Image(src_base64=Logo,
                                                        width=100,
                                                        height=50),
                                                  Text(value="Usuário:",),
                                                  AreaUsuario,
                                                  Text(value="Senha:",),
                                                  AreaSenha,
                                                  ElevatedButton(text="Logar", 
                                                                 on_click=Autenticar)]),
                        )