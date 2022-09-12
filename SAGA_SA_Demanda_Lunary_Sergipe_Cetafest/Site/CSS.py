from flet import (Image, Page, Row, border_radius, Container, colors, alignment, padding, Text, LinearGradient,
                  ShaderMask, Column, AppBar, Icon, IconButton, Page, PopupMenuButton, PopupMenuItem, icons,
                  border_radius, Stack)

def appBar(img_,func1, func2):
    return AppBar(
        leading=Image(
            src_base64=img_,
            height=100,
            fit="contain",
        ),
        leading_width=100,
        toolbar_height=65,
        title=Text("Cardápio"),
        center_title=True,
        bgcolor=colors.SURFACE_VARIANT,
        actions=[
            IconButton(icons.WB_SUNNY_OUTLINED, on_click=func1, width=65),
            IconButton(icons.FILTER_3, width=65),
            PopupMenuButton(
                width=65,
                items=[
                    PopupMenuItem(text="Item 1"),
                    PopupMenuItem(),  # divider
                    PopupMenuItem(
                        text="Checked item", checked=False, on_click=func2
                    ),
                ]
            ),
        ],
    )
    
def Images(i):
    return Container(
                width=220,
                height=440,
                bgcolor=colors.DEEP_ORANGE_700,
                border_radius=border_radius.all(10),
                margin=5,
                padding=padding.Padding(left=0,top=0,right=0,bottom=0),
                content=Stack([
                    IconButton(icons.FAVORITE_BORDER),
                    Text("descrição", style="titleMedium"),
                    Image(
                        src=f"https://picsum.photos/200/200?{i}",
                        width=200,
                        height=200,
                        fit="none",
                        repeat="noRepeat",
                        top=45,
                        left=0,
                        right=0,
                        border_radius=border_radius.all(10),
                        ),
                    Text("descrição: "),
                    Text("igredientes principais: ")
                ])
            )