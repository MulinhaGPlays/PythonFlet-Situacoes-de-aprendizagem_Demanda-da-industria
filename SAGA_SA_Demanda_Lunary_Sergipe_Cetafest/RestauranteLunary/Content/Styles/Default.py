from flet import Column, Row, Container, margin, Text, ElevatedButton, colors
from Views.RouteConfig import RouteConfig

def TextContainer(head):
    return Container(
        width=600 if head.mobile == False else 400,
        content=(
            Column(
                horizontal_alignment="center",
                controls=[
                    Text(
                        value="BEM VINDO(A)",
                        size=40 if head.mobile == False else 35 ,
                        weight="bold",
                        font_family="Consolas"
                    ),
                    Text(
                        width=250 if head.mobile == False else 225,
                        value='Este é um projeto teste utilizando a biblioteca do python "Flet", um compilador da linguagem Dart do fluetter'
                        ),
                ]
            )
        )
    )
    
def Cardapio(head):
    return Container(
        margin=margin.Margin(0,10,0,0),
        width=450 if head.mobile == False else 250,
        height=550 if head.mobile == False else 350,
        border_radius = 5,
        bgcolor=format("#861E1E"),
        content=Column(
            alignment="center",
            horizontal_alignment="center",
            controls=[
                Text(
                    value="Veja nosso cardápio!",
                    size=20 if head.mobile == False else 16,
                    weight="bold",
                    ),
                Container(height=300 if head.mobile == False else 160),
                ElevatedButton(
                    text="Cardápio",
                    width=200 if head.mobile == False else 100,
                    height=50 if head.mobile == False else 35,
                    on_click=lambda _: RouteConfig(page=head.page, route="/cardapio")
                    )
                ]
            )
        )