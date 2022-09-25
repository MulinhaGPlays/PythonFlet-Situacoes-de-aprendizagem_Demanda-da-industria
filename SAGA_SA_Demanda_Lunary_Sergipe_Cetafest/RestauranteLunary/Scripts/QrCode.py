import qrcode
def QrCodeGen(page, selectPage):
    qrcode.make(f'{page.url}/#/{selectPage}').save(f'QrCode_{selectPage}')
    
#dropdown, aparecer o código no onchange e ter a opção de salvar