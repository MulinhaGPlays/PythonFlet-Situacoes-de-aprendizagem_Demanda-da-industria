import qrcode
def QrCodeGen(page, selectPage):
    selectPage == "Default" if selectPage == None else selectPage
    qrcode.make(f'{page.url}/#/{selectPage}').save(f'QrCode_{selectPage}.png')