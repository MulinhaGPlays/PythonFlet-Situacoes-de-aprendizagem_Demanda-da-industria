from Content.View import View_Style

def Sobre(page, auth, mobile):
    page.title = "Sobre"
    page.views.append(View_Style("/sobre", page, auth, html(page, auth).body(), mobile))
    
class html:
    def __init__(head, page, auth):
        head.page = page
        head.auth = auth
    def body(head):
        return []