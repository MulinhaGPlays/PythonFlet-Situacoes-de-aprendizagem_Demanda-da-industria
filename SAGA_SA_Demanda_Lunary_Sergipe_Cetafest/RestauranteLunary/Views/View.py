from Views.Pages import Default, Home, Cardapio, Contato, Sobre, Erro404, Login, Registrar
class View:
    def __init__(self, page, auth):
        self.page = page
        self.auth = auth
    def Default(self):
        Default.Default(self.page, self.auth)
    def Home(self):
        Home.Home(self.page, self.auth)
    def Cardapio(self):
        Cardapio.Cardapio(self.page, self.auth)
    def Contato(self):
        Contato.Contato(self.page, self.auth)
    def Sobre(self):
        Sobre.Sobre(self.page, self.auth)
    def Login(self):
        Login.Login(self.page, self.auth)
    def Registrar(self):
        Registrar.Registrar(self.page, self.auth)
    def Erro404(self):
        Erro404.Erro404(self.page, self.auth)