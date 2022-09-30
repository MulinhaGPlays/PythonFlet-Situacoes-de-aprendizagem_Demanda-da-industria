import qrcode
def QrCodeGen(page, selectPage):
    selectPage = "Default" if selectPage == None or '' else selectPage
    imgName = f'QrCode_{selectPage}.png'
    qrcode.make(f'{page.url}/#/{selectPage}').save(imgName)
    return imgName