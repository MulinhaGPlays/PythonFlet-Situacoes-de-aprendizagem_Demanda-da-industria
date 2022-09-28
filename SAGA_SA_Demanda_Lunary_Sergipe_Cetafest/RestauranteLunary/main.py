import flet
from Controllers.LunaryController import main

if __name__ == "__main__":
    flet.app(
        target=main,
        upload_dir="cache",
        
        port= 5000,
        )
