from calendar import c
from flet.ref import Ref
from flet import (Row, Image, Text, Container, colors, Column, IconButton, 
                  ElevatedButton, Dropdown, dropdown, PopupMenuButton, PopupMenuItem, 
                  Icon, icons, padding, alignment, Alignment, FilePicker, FilePickerResultEvent)
from Models.Database import Database as db
import base64

def filtro(page):
    produto = Row(controls=[], scroll='always',)
    disableBimg = True
    db.SELECT(COLUMN='*', TABLE='Cardapio')
    def filtrar(e):
        match dd.value:
            case 'Aperitivos':
                categoria = 'Aperitivo'
            case 'Entradas':
                categoria = 'Entrada'
            case 'Pratos Principais':
                categoria = 'Prato Principal'
            case 'Sobremesas':
                categoria = 'Sobremesa'
            case 'Bebidas':
                categoria = 'Bebida'
        db.SELECT_WHERE(
            COLUMN='*',
            TABLE='Cardapio',
            COLUMNCond='Categoria',
            Operator='=',
            Condition=categoria)
        produtos()
        page.update()
    def btnTodos(e):
        db.SELECT(COLUMN='*', TABLE='Cardapio')
        produtos()
        dd.value = ''
        page.update()
    def btnMConsumidos(e):
        db.SELECT_ORDERby(COLUMN='*', TABLE='Cardapio', COLUMNCond='VezesConsumo', ORDER='DESC')
        produtos()
        dd.value = ''
        page.update()
    def btnPdoDia(e):
        db.SELECT_WHERE(COLUMN='*', TABLE='Cardapio', COLUMNCond='Promocional', Operator='=', Condition=1)
        produtos()
        dd.value = ''
        page.update()
    def adicionar(Nome, Preco):
        if vazio in carrinho.controls:
            carrinho.controls.clear()
        indice = Text(f'{len(carrinho.controls)+1} -') #atualizar com a alteração da quantidade
        def RemoveProd(Id):
            return IconButton(icon=icons.REMOVE_CIRCLE_OUTLINE, 
                              icon_color=colors.RED, 
                              on_click=lambda _: remover(Id),)
        def remover(Id):
            carrinho.controls.pop(0)
            if carrinho.controls == []:
                carrinho.controls.append(vazio)
            page.update()
        carrinho.controls.append(
            Container(
                height=40,
                bgcolor=colors.DEEP_PURPLE_900,
                border_radius= 10,
                padding=padding.Padding(12,0,5,0),
                alignment=alignment.center,
                content=Row(
                    controls=[
                        indice,
                        Text(Nome),
                        Text(f'R${Preco}'),
                        RemoveProd(len(carrinho.controls))
                    ]
                )
            )
        )
        page.update()
    def produtos():
        produto.controls.clear()
        def addcart(Nome, Preco):
            return IconButton(icon=icons.ADD_SHOPPING_CART_SHARP, on_click=lambda _: adicionar(Nome, Preco))
        for row in db.FETCHALL():
            produto.controls.append(
                Container(
                    height=475,
                    width=275, 
                    padding=5,
                    margin=5,
                    bgcolor=colors.DEEP_ORANGE_400,
                    border_radius= 10,
                    content=Column(
                        horizontal_alignment="center",
                        controls=[
                            IconButton(
                                disabled=disableBimg,
                                on_click=lambda _: print(1),
                                content=Image(
                                    src_base64=row.Imagem,
                                    fit='cover',
                                    width=255,
                                    border_radius= 10,
                                ),
                            ),
                            Text(
                                value=row.Nome
                                ),
                            Text(
                                value=row.Descricao
                                ),
                            Row(
                                controls=[
                                    Text(
                                        value=f'R${row.Preco}'
                                        ),
                                    addcart(row.Nome, row.Preco),
                                ]
                            ),
                        ]
                        ),
                    ),
                )
    produtos()
    dd = Dropdown(
        hint_text='Filtrar Categoria',
        width=200,
        on_change=filtrar,
        options=[
            dropdown.Option('Aperitivos'),
            dropdown.Option('Entradas'),
            dropdown.Option('Pratos Principais'),
            dropdown.Option('Sobremesas'),
            dropdown.Option('Bebidas'),
        ],
    )
    icone = Icon(icons.SHOPPING_CART)
    carrinho = Row(controls=[])
    vazio = Container(
        bgcolor=colors.DEEP_PURPLE_900,
        border_radius=10,
        height=40,
        padding=padding.Padding(10,0,10,0),
        alignment=alignment.center,
        content=Text(value='O carrinho está vazio, adicione algo!')
        )
    btnTodos = ElevatedButton(
        text='Todos',
        on_click=btnTodos
    )
    btnMConsumidos =  ElevatedButton(
        text='Produtos mais Consumidos',
        on_click=btnMConsumidos
    )
    btnPdoDia = ElevatedButton(
        text='Produtos do Dia',
        on_click=btnPdoDia
    )
    carrinho.controls.append(vazio)
    return Column(controls=[Row(controls=[dd, btnTodos, btnMConsumidos, btnPdoDia]), Row(controls=[icone, carrinho]), produto])