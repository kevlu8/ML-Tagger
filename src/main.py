# This script combines the many files that are used to make the program work.

if __name__ != "__main__":
    print("This is meant to be run as the main file, not imported as a module.")
    exit()

import window
import detect

from threading import Thread
import PIL.Image
import tempfile
import math
import time
import os

eventQueue = []

def convertAndScale(filename):
    MAX_HEIGHT, MAX_WIDTH = 852, 480
    img = PIL.Image.open(filename[0])
    width, height = img.size
    if width > MAX_WIDTH or height > MAX_HEIGHT:
        scale = max(width, height) / min(MAX_WIDTH, MAX_HEIGHT)
        if width / scale > MAX_WIDTH or height / scale > MAX_HEIGHT:
            scale = max(width, height) / max(MAX_WIDTH, MAX_HEIGHT)
        img = img.resize((math.floor(width / scale), math.floor(height / scale)))
        if filename[0] != filename[1]:
            img.save(filename[0], "png")
        else:
            fd, file = tempfile.mkstemp()
            os.close(fd)
            filename = (file, filename[0])
            img.save(filename[0], "png")
    elif filename[0].lower().endswith((".jpg", ".jpeg")):
        fd, file = tempfile.mkstemp()
        os.close(fd)

        # Save the png to the temp file
        pil_image = PIL.Image.open(filename[0])
        pil_image.save(file, "png")

        filename = (file, filename[0])
    eventQueue.append(("convertAndScale finished", {"filename":filename}))

appWindow = window.createWindow()

while True:
    if eventQueue:
        event, values = eventQueue.pop()
    else:
        event, values = appWindow.read(0)
    if event == "Exit" or event == window.sg.WIN_CLOSED:
        break
    if event == "-IMAGE_FOLDER-":
        folder = values["-IMAGE_FOLDER-"]
        try:
            file_list = os.listdir(folder)
        except FileNotFoundError:
            continue
        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".png", ".jpg", ".jpeg"))
        ]
        appWindow["-FILE_LIST-"].update(fnames)
    elif event == "-FILE_LIST-":
        try:
            filename = os.path.join(
                values["-IMAGE_FOLDER-"], values["-FILE_LIST-"][0]
            )
            filename = (filename, filename)
        except IndexError:
            continue
        appWindow["-GET_TAGS-"].update(disabled=True)
        Thread(target=convertAndScale, args=(filename,), daemon=True).start()
    if event == "convertAndScale finished":
        filename = values["filename"]
        appWindow["-TOUT-"].update(filename[1])
        appWindow["-GET_TAGS-"].update(disabled=False)
        appWindow["-PREVIEW_IMAGE-"].update(filename=filename[0])
        if filename[0] != filename[1]:
            os.remove(filename[0])
    elif event == "-GET_TAGS-":
        print("WIP")
    time.sleep(0.01)

appWindow.close()
