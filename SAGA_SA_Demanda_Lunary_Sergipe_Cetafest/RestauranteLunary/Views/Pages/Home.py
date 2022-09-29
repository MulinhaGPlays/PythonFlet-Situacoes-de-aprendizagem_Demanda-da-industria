from Content.View import View_Style
from Views.RouteConfig import RouteConfig

def Home(page, auth, mobile):
    if auth == 0:
        return RouteConfig(page=page, route='/')
    page.title = "Home"
    page.views.append(View_Style("/home", page, auth, html(page, auth).body(), mobile))
    
class html:
    def __init__(head, page, auth):
        head.page = page
        head.auth = auth
    def body(head):
        return []