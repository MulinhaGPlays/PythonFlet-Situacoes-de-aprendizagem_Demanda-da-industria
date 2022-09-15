import flet
import base64
from flet import (
    ElevatedButton,
    FilePicker,
    FilePickerResultEvent,
    Page,
    Row,
    Text,
    icons,
    Image,
)


def main(page: Page):
    # Pick files dialog
    def pick_files_result(e: FilePickerResultEvent):
        selected_files.value = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
        )
        selected_files.update()
        if selected_files.value != 'Cancelado!':
            with open(f'{selected_files.value}', 'rb') as noB64:
                img = base64.b64encode(noB64.read()).decode()
                selected_image.src_base64 = img
                selected_image.update()

    pick_files_dialog = FilePicker(on_result=pick_files_result)
    selected_files = Text()
    selected_image = Image()

    # Save file dialog
    def save_file_result(e: FilePickerResultEvent):
        save_file_path.value = e.path if e.path else "Cancelled!"
        save_file_path.update()

    save_file_dialog = FilePicker(on_result=save_file_result)
    save_file_path = Text()

    # Open directory dialog
    def get_directory_result(e: FilePickerResultEvent):
        directory_path.value = e.path if e.path else "Cancelled!"
        directory_path.update()

    get_directory_dialog = FilePicker(on_result=get_directory_result)
    directory_path = Text()

    # hide all dialogs in overlay
    page.overlay.extend([pick_files_dialog, save_file_dialog, get_directory_dialog])

    page.add(
        Row(
            [
                ElevatedButton(
                    "Pick files",
                    icon=icons.UPLOAD_FILE,
                    on_click=lambda _: pick_files_dialog.pick_files(
                        allow_multiple=True
                    ),
                ),
                selected_files,
                selected_image,
            ]
        ),
        Row(
            [
                ElevatedButton(
                    "Save file",
                    icon=icons.SAVE,
                    on_click=lambda _: save_file_dialog.save_file(),
                    disabled=page.web,
                ),
                save_file_path,
            ]
        ),
        Row(
            [
                ElevatedButton(
                    "Open directory",
                    icon=icons.FOLDER_OPEN,
                    on_click=lambda _: get_directory_dialog.get_directory_path(),
                    disabled=page.web,
                ),
                directory_path,
            ]
        ),
    )


flet.app(target=main)