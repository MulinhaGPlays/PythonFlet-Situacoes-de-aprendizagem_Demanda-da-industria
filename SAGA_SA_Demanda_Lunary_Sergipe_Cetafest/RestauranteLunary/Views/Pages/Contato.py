from Content.View import View_Style

def Contato(page, auth):
    page.title = "Contato"
    page.views.append(View_Style("/contato", page, auth, html(page, auth).body()))
    
class html:
    def __init__(head, page, auth):
        head.page = page
        head.auth = auth
    def body(head):
        return []
