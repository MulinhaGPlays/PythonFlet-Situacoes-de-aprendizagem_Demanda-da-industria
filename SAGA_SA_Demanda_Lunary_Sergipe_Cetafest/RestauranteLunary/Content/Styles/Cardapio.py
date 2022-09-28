import time
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
produto = Row(controls=[], scroll='always',)
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