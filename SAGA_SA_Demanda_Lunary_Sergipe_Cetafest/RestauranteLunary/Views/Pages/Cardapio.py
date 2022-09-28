import time
from flet import (Row, Image, Text, Container, colors, Column, IconButton, 
                  ElevatedButton, Dropdown, dropdown, PopupMenuButton, PopupMenuItem, 
                  Icon, icons, padding, alignment, Alignment, FilePicker, FilePickerResultEvent,
                  FilePickerUploadEvent, FilePickerUploadFile, border_radius, margin,
                  Stack, border)
from Models.Database import Database as db
import base64
import os
from Content.View import View_Style

def Cardapio(page, auth):          
    page.title = "Cardapio"
    page.views.append(View_Style("/cardapio", page, auth, html(page, auth).body()))
    
    
from Content.Styles.Cardapio import AddImg, produto, vazio, carrinho, icone
class html:
    def __init__(head, page, auth):
        head.page = page
        head.auth = auth
    def body(head):
        disableBimg = True
        if head.auth == 1:
            disableBimg = False
        def file_picker_result(e: FilePickerResultEvent):
            PATH = f"cache"
            if e.files != None:
                uf = []
                for f in file_picker.result.files:
                    uf.append(
                        FilePickerUploadFile(
                            f.name,
                            upload_url=head.page.get_upload_url(f.name, 600),
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
            print('progresso')
        file_picker = FilePicker(on_result=file_picker_result, on_upload=on_upload_progress)
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
            head.page.update()
        head.page.overlay.append(file_picker)
        head.page.update()
        db.SELECT(COLUMN='*', TABLE='Cardapio')
        def limpardd():
            produtos()
            dd.value = ''
            dd.update()
        def btnTodos(e):
            db.SELECT(COLUMN='*', TABLE='Cardapio')
            limpardd()
        def btnMConsumidos(e):
            db.SELECT_ORDERby(COLUMN='*', TABLE='Cardapio', COLUMNCond='VezesConsumo', ORDER='DESC')
            limpardd()
        def btnPdoDia(e):
            db.SELECT_WHERE(COLUMN='*', TABLE='Cardapio', COLUMNCond='Promocional', Operator='=', Condition=1)
            limpardd()
        def adicionar(Nome, Preco):
            if vazio in carrinho.controls:
                carrinho.controls.clear()
            def remover(e):
                carrinho.controls.remove(e.control)
                if carrinho.controls == []:
                    carrinho.controls.append(vazio)
                head.page.update()
            carrinho.controls.append(
                Container(
                    height=40,
                    bgcolor=colors.DEEP_PURPLE_900,
                    border_radius= 10,
                    padding=padding.Padding(12,0,5,0),
                    alignment=alignment.center,
                    on_click=remover,
                    content=Row(
                        controls=[
                            Text(Nome),
                            Text(f'R${Preco}'),
                        ]
                    )
                )
            )
            head.page.update()
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
                        bgcolor=format("#ff006a"),
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
                head.page.update()
        produtos()
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
        dd = Dropdown(
            filled=True,
            hint_text='Filtrar Categoria',
            width=200,
            border="underline",
            border_radius=10,
            on_change=filtrar,
            options=[
                dropdown.Option('Aperitivos'),
                dropdown.Option('Entradas'),
                dropdown.Option('Pratos Principais'),
                dropdown.Option('Sobremesas'),
                dropdown.Option('Bebidas'),
            ],
        )
        if carrinho.controls == []:
            carrinho.controls.append(vazio)
        return [Column(
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
            )]