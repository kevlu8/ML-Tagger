# This is what will draw out the window.

if __name__ == "__main__":
    print("You're running the wrong file. Please run main.py instead.")
    exit()

import sys
import PySimpleGUI as sg

def createWindow():
    if sys.platform.startswith("win"):
        import ctypes
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(u"kevlu8.ML-Tagger.0.1.3.alpha")
        platform = "windows"
    elif sys.platform.startswith("linux"):
        platform = "linux"
    elif sys.platform.startswith("darwin"):
        platform = "mac"
    else:
        print("Unsupported platform: " + sys.platform)
        sys.exit(1)

    sg.theme("Default 1")

    file_list_column = [
        [
            sg.Text("Image Folder"),
            sg.In(size=(25, 1), enable_events=True, key="-IMAGE_FOLDER-"),
            sg.FolderBrowse(),
        ],
        [
            sg.Listbox(
                values=[], enable_events=True, size=(40, 20), key="-FILE_LIST-",
            )
        ],
    ]

    image_viewer_column = [
        [sg.Text("Choose an image from list on left:")],
        [sg.Text(size=(40, 1), key="-TOUT-")],
        [sg.Image("icon.png", size=(300,300), key="-PREVIEW_IMAGE-")],
        [sg.Button(button_text="Get Tags", key="-GET_TAGS-", disabled=True)],
    ]

    layout = [
        [
            sg.Column(file_list_column),
            sg.VSeparator(),
            sg.Column(image_viewer_column),
        ]
    ]

    if platform == "windows":
        window = sg.Window("ML-Tagger AI Window", layout, icon="icon.ico", finalize=True)
    elif platform == "linux":
        window = sg.Window("ML-Tagger AI Window", layout, icon="icon.png", finalize=True)
    elif platform == "mac":
        window = sg.Window("ML-Tagger AI Window", layout, icon="icon.icns", finalize=True)

    return window