import time
from flet.ref import Ref
from flet import (Row, Image, Text, Container, colors, Column, IconButton, 
                  ElevatedButton, Dropdown, dropdown, PopupMenuButton, PopupMenuItem, 
                  Icon, icons, padding, alignment, Alignment, FilePicker, FilePickerResultEvent,
                  FilePickerUploadEvent, FilePickerUploadFile, border_radius, margin,
                  Stack)
from Models.Database import Database as db
import base64
import os

with open(f"Content/Imgs/Add_Img.png", "rb") as AddImg:
    AddImg = base64.b64encode(AddImg.read()).decode()

def filtro(page):
    def file_picker_result(e: FilePickerResultEvent):
        PATH = f"cache"
        if e.files != None:
            uf = []
            for f in file_picker.result.files:
                uf.append(
                    FilePickerUploadFile(
                        f.name,
                        upload_url=page.get_upload_url(f.name, 600),
                    )
                )
            file_picker.upload(uf)
            name = list(map(lambda f: f.name, uf))[0]
            print(f'{name} foi adicionado ao item de Id: {i_d}')
            while os.listdir(PATH) == []:
                time.sleep(0.01)
            with open(f"{PATH}/{name}", "rb") as img:
                db.UPDATE(TABLE='Cardapio',
                          COLUMN='Imagem',
                          VALUES=f"CONVERT(VARBINARY(MAX), '{base64.b64encode(img.read()).decode()}')",
                          COLUMNCond='Id',
                          Operator='=',
                          Condition=i_d)
            while os.listdir(PATH) != []:
                try:
                    os.remove(f"{PATH}/{name}")
                except:
                    print('erro')
            db.SELECT(COLUMN='*', TABLE='Cardapio')
            produtos()
            
                    
    def on_upload_progress(e: FilePickerUploadEvent):
        pass
    produto = Row(controls=[], scroll='always',)
    disableBimg = False
    file_picker = FilePicker(on_result=file_picker_result, on_upload=on_upload_progress)
    page.overlay.append(file_picker)
    page.update()
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
    def addImage(Id):
        global i_d
        i_d = Id
        file_picker.pick_files(
            dialog_title="Insira a imagem ao item do cardápio",
            file_type="image",
            allow_multiple=False,
                               )
    def produtos():
        produto.controls.clear()
        def addcart(Nome, Preco):
            return IconButton(icon=icons.ADD_SHOPPING_CART_SHARP, on_click=lambda _: adicionar(Nome, Preco))
        def imgUpd(Id, Imagem):
            if Imagem != None:
                Imagem = base64.decodebytes(Imagem)
                Imagem = base64.b64encode(Imagem).decode()
                size = 250
                radius = size*0.5
            else:
                Imagem = AddImg
                size = 150
                radius = 0
            return IconButton(
                bgcolor=colors.WHITE,
                bottom=10,
                left=10,
                right=10,
                width=250,
                height=250,
                disabled=disableBimg,
                on_click=lambda _: addImage(Id),
                content=Image(
                    src_base64=Imagem,
                    fit='cover',
                    width=size,
                    height=size,
                    border_radius= radius,
                )
            )
        for row in db.FETCHALL():
            produto.controls.append(
                Container(
                    height=475,
                    width=275, 
                    padding=5,
                    margin=5,
                    bgcolor=colors.DEEP_ORANGE_400,
                    border_radius=border_radius.BorderRadius(10, 10, 275*0.5, 275*0.5),
                    content=Stack(
                        controls=[
                            Column(
                                top=10,
                                left=10,
                                right=10,
                                horizontal_alignment="center",
                                controls=[
                                    Text(
                                        value=row.Nome,
                                        size=18,
                                        text_align="center",
                                        weight="bold",
                                        ),
                                    Text(value=row.Descricao),
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
                            imgUpd(row.Id, row.Imagem),
                        ]
                        ),
                    ),
                )
        page.update()
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
    return Column(
        controls=[
            Container(
                margin=margin.Margin(10,10,0,0),
                content=Row(
                    controls=[
                        dd, 
                        btnTodos,
                        btnMConsumidos,
                        btnPdoDia,
                        ]
                    )
                ),
            Container(
                margin=margin.Margin(10,10,0,0),
                content=Row(
                    controls=[
                        icone,
                        carrinho
                        ]
                    )
                ),
            produto
            ],
        )