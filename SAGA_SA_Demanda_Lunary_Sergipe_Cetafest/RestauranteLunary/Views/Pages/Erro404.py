from Content.View import View_Style

def Erro404(page, mobile):
    page.title = "404"
    page.views.append(View_Style("/erro404", page, 0, html(page).body(), mobile))
    
class html:
    def __init__(head, page):
        head.page = page
    def body(head):
        return []