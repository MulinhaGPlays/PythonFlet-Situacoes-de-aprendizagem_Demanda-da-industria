from flet import Column, Row, Container, margin, Text, ElevatedButton, colors
from Views.RouteConfig import RouteConfig

def TextContainer(head):
    return Container(
        width=600,
        content=(
            Column(
                horizontal_alignment="center",
                controls=[
                    Text(
                        value="BEM VINDO(A)",
                        size=40,
                        weight="bold",
                    ),
                    Text("akjhndbaujdbadhuwbjdawkjdbwadujawdnawujdh"),
                    Text("akjhndbaujdbadhuwbjdawkjdbwadujawdnawujdh"),
                    Text("akjhndbaujdbadhuwbjdawkjdbwadujawdnawujdh"),
                    Text("akjhndbaujdbadhuwbjdawkjdbwadujawdnawujdh"),
                ]
            )
        )
    )
    
def Cardapio(head):
    return Container(
        margin=margin.Margin(0,10,0,0),
        width=450,
        height=550,
        border_radius = 5,
        bgcolor=format("#861E1E"),
        content=Column(
            alignment="center",
            horizontal_alignment="center",
            controls=[
                Text(
                    value="Veja nosso cardápio!",
                    size=20,
                    weight="bold",
                    ),
                Container(height=300),
                ElevatedButton(
                    text="Cardápio",
                    width=200,
                    height=50,
                    on_click=lambda _: RouteConfig(page=head.page, route="/cardapio")
                    )
                ]
            )
        )