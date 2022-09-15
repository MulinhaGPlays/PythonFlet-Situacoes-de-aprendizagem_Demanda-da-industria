from flet import Container, Column, Text, alignment, colors, UserControl, Image

class build(UserControl):
    def build(self):
        return Column([self.logo(), self.text()])
    
    def logo(self):
        return Image(src=f"RestauranteLunary\Logo.png",)
    def text(self):
        return Container(content=Text("Non clickable"),
                         margin=10,
                         padding=10,
                         alignment=alignment.center,
                         bgcolor=colors.BLUE,
                         width=150,
                         height=150,
                         border_radius=10,
                        )