from flet import (Container, Column, Text, alignment, colors, 
                  UserControl, Image, ElevatedButton, TextField, 
                  Dropdown, dropdown, Row)
from Scripts.Autenticacao import Registro
from Models.Database import Database as db
import base64

class build(UserControl):
    def build(self):
        return self.RegistroArea(self.page)
    
    def RegistroArea(self, page):
        with open(f"Logo.png", "rb") as noB64:         
            Logo = base64.b64encode(noB64.read()).decode()
        AreaUsuario = TextField(hint_text="Usuário",
                                width=200)
        AreaSenha = TextField(hint_text="Senha",
                              width=200)
        AreaRestaurante = Dropdown(
            width=500
        )
        AreaCodFunc = TextField(
            hint_text='Código de Funcionario',
            width=200
        )
        db.SELECT(COLUMN='*', TABLE='RedeRestaurantes')
        for row in db.FETCHALL():
            AreaRestaurante.options.append(
                dropdown.Option(f'{row.Id} - {row.Endereco}, {row.Numero} / {row.Cidade} - {row.Estado}')
            )
        
        def Autenticar(e):
            Registro(
                Usuario=AreaUsuario.value, 
                Senha=AreaSenha.value,
                IdRestaurante=len(AreaRestaurante.options),
                CodFuncionario=AreaCodFunc.value,
                page=page
                )
        return Container(padding=10,
                         alignment=alignment.center,
                         bgcolor=colors.BLUE,
                         border_radius=10,
                         content=Column(horizontal_alignment="center",
                                        controls=[Image(src_base64=Logo,
                                                        width=100,
                                                        height=50),
                                                  Text(value="Usuário:",),
                                                  AreaUsuario,
                                                  Text(value="Senha:",),
                                                  AreaSenha,
                                                  AreaRestaurante,
                                                  AreaCodFunc,
                                                  ElevatedButton(text="Registrar", 
                                                                 on_click=Autenticar)]),
                        )