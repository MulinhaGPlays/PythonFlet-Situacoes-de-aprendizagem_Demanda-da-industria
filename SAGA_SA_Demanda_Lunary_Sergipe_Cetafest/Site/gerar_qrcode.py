import qrcode

img = qrcode.make("opa bom dia")
img.save("Cardapio.jpeg")
