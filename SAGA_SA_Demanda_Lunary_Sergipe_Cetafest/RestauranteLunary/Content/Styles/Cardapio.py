from flet import Row, UserControl, Image, border_radius
import base64

class build(UserControl):
    def build(self):
        return self.images()
    
    def images(self):
        with open(f"RestauranteLunary\Logo.png", "rb") as noB64:         
            Logo = base64.b64encode(noB64.read()).decode()
        images = Row(expand=1, wrap=False, scroll="always")
        for i in range(0, 30):
            images.controls.append(
                Image(
                    src=f"https://picsum.photos/200/200?{i}",
                    width=200,
                    height=200,
                    fit="none",
                    repeat="noRepeat",
                    border_radius=border_radius.all(10),
                )
            )
        return images