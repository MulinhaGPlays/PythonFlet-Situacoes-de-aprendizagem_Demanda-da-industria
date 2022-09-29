from Views.Pages import Default, Home, Cardapio, Contato, Sobre, Erro404, Login, Registrar
class View:
    def __init__(self, page, auth, mobile):
        self.page = page
        self.auth = auth
        self.mobile = mobile
    def Default(self):
        Default.Default(self.page, self.auth, self.mobile)
    def Home(self):
        Home.Home(self.page, self.auth, self.mobile)
    def Cardapio(self):
        Cardapio.Cardapio(self.page, self.auth, self.mobile)
    def Contato(self):
        Contato.Contato(self.page, self.auth, self.mobile)
    def Sobre(self):
        Sobre.Sobre(self.page, self.auth, self.mobile)
    def Login(self):
        Login.Login(self.page, self.auth, self.mobile)
    def Registrar(self):
        Registrar.Registrar(self.page, self.auth, self.mobile)
    def Erro404(self):
        Erro404.Erro404(self.page, self.mobile)