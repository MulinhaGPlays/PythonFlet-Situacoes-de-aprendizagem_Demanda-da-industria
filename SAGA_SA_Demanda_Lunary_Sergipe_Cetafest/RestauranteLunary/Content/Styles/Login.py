from flet import Container, Column, Text, alignment, colors, UserControl, Image, ElevatedButton, TextField
import base64
from Scripts.Autenticacao import Autenticar

class build(UserControl):
    def build(self):
        return self.LoginArea()
    
    def LoginArea(self):
        with open(f"RestauranteLunary\Logo.png", "rb") as noB64:         
            Logo = base64.b64encode(noB64.read()).decode()
        return Container(content=Column(horizontal_alignment="center",
                                        controls=[Image(src_base64=Logo,
                                                        width=100,
                                                        height=50),
                                                  Text(value="Usuário:",),
                                                  TextField(hint_text="Usuário",
                                                            width=200),
                                                  Text(value="Senha:",),
                                                  TextField(hint_text="Senha",
                                                            width=200),
                                                  ElevatedButton(text="Logar", 
                                                                 on_click=Autenticar())]),
                         padding=10,
                         alignment=alignment.center,
                         bgcolor=colors.BLUE,
                         border_radius=10,
                         width=300,
                        )