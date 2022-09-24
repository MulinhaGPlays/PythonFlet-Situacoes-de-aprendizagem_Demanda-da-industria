import flet
from Controllers.LunaryController import main

if __name__ == "__main__":
    flet.app(
        target=main,
        upload_dir="cache",
        view=flet.WEB_BROWSER,
        port= 5000,
        )
