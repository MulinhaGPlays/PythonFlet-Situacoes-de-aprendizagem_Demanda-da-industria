from CSS import Style_AppBar

class PageView:
    def __init__(self, page):
        self.page = page
        
    def RouteConfig(self, route):
        return lambda _: self.page.go(route)
    
    def Page(self, PageName:str='Home'):
        match PageName:
            case 'Home':
                return Style_AppBar(title='Home', btn1_name="Cardapio", btn1_route=self.RouteConfig('/cardapio'))
            case 'cardapio':
                return Style_AppBar(title="Cardapio", btn1_name="Visit Home", btn1_route=self.RouteConfig('/'))
            case 'contato':
                pass
            case 'sobre':
                pass
            case '404':
                return Style_AppBar(title="Erro404", btn1_name="Visit Home", btn1_route=self.RouteConfig('/'))