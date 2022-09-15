from typing import Dict

import flet
import os
import base64
import time
import threading
from flet import (
    ElevatedButton,
    FilePicker,
    FilePickerResultEvent,
    FilePickerUploadEvent,
    FilePickerUploadFile,
    Page,
    ProgressRing,
    Ref,
    Row,
    Text,
    icons,
    Image,
)
from flet.column import Column


def main(page: Page):
    prog_bars: Dict[str, ProgressRing] = {}
    files = Ref[Column]()
    upload_button = Ref[ElevatedButton]()
    selected_image = Image()
    
    PATH = "temp/Temp/"

    def file_picker_result(e: FilePickerResultEvent):
        upload_button.current.disabled = True if e.files == None else False
        prog_bars.clear()
        files.current.controls.clear()
        if e.files != None:
            for f in e.files:
                prog = ProgressRing(value=0, bgcolor="#eeeeee", width=20, height=20)
                prog_bars[f.name] = prog
                files.current.controls.append(Row([prog, Text(f.name)]))
        page.update()
        

    def on_upload_progress(e: FilePickerUploadEvent):
        prog_bars[e.file_name].value = e.progress
        prog_bars[e.file_name].update()

    file_picker = FilePicker(on_result=file_picker_result, on_upload=on_upload_progress)

    def upload_files(e):
        upload_button.current.disabled = True
        upload_button.current.update()
        uf = []
        if file_picker.result != None and file_picker.result.files != None:
            for f in file_picker.result.files:
                uf.append(
                    FilePickerUploadFile(
                        f.name,
                        upload_url=page.get_upload_url(f.name, 600),
                    )
                )
            file_picker.upload(uf)
            global name
            name = list(map(lambda f: f.name, uf))[0]
            
    def load_image():
        while True:
            time.sleep(0.01)
            try:
                if name in os.listdir(PATH):
                    with open(f"{PATH}{name}", "rb") as noB64:         
                        selected_image.src_base64 = base64.b64encode(noB64.read()).decode()    
                        selected_image.update()
                    os.remove(f"{PATH}{name}")
            except:
                pass
            
    threading.Thread(target=load_image).start()
    # hide dialog in a overlay
    page.overlay.append(file_picker)

    page.add(
        ElevatedButton(
            "Select image",
            icon=icons.FOLDER_OPEN,
            on_click=lambda _: file_picker.pick_files(file_type="image", allow_multiple=False),
        ),
        Column(ref=files),
        ElevatedButton(
            "Upload",
            ref=upload_button,
            icon=icons.UPLOAD,
            on_click=upload_files,
            disabled=True,
        ),
        selected_image,
    )


flet.app(target=main, view=flet.WEB_BROWSER, upload_dir="Temp")

#falta colocar pra imagem aparecer no loadfile como previsualização e o upload ser pra exportar pro banco de dados