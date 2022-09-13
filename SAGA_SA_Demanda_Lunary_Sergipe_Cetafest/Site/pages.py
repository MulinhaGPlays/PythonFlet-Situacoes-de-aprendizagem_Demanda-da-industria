from styles import Style_AppBar

def Home(route):
    return Style_AppBar(title="Home", btn_name="Visit Store", route=route)
def Store(route):
    return Style_AppBar(title="Store", btn_name="Visit Home", route=route)
def Erro(route):
    return Style_AppBar(title="Erro404", btn_name="Visit Home", route=route)