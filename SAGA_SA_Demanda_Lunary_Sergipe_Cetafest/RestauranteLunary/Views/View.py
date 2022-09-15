from Views.Pages import Default, Home, Cardapio, Contato, Sobre, Erro404, Login
class View:
    def __init__(self, page):
        self.page = page
    def Default(self):
        Default.Default(self.page)
    def Home(self):
        Home.Home(self.page)
    def Cardapio(self):
        Cardapio.Cardapio(self.page)
    def Contato(self):
        Contato.Contato(self.page)
    def Sobre(self):
        Sobre.Sobre(self.page)
    def Login(self):
        Login.Login(self.page)
    def Erro404(self):
        Erro404.Erro404(self.page)