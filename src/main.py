# This script combines the many files that are used to make the program work.

if __name__ != '__main__':
    print("This is meant to be run as the main file, not imported as a module.")
    exit()

import window
import detect
import PySimpleGUI as sg
import os
import tempfile
import PIL
import math

def jpgToPng(imagePath):
    # Take jpg and create a temporary png file in %TEMP%/ML-Tagger
    tempdir = tempfile.gettempdir() + '\\ML-Tagger\\'
    if (not os.path.exists(tempdir)):
        os.mkdir(tempdir)

    # Save the png to the temp directory
    pil_image = PIL.Image.open(imagePath)
    pil_image.save(tempdir + 'img.png')
    return tempdir + 'img.png'

appWindow = window.createWindow()

while True:
        event, values = appWindow.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "-IMAGE_FOLDER-":
            folder = values["-IMAGE_FOLDER-"]
            try:
                file_list = os.listdir(folder)
            except FileNotFoundError:
                file_list = []
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
            except IndexError:
                continue
            if filename.lower().endswith((".jpg", ".jpeg")):
                filename = jpgToPng(filename)
            # marker
            MAX_HEIGHT, MAX_WIDTH = 852, 480
            img = PIL.Image.open(filename)
            if img.size[0] > MAX_WIDTH or img.size[1] > MAX_HEIGHT:
                swidth = img.size[0] / min(MAX_WIDTH, MAX_HEIGHT)
                sheight = img.size[1] / min(MAX_WIDTH, MAX_HEIGHT)
                if img.size[0] / swidth > MAX_WIDTH or img.size[1] / sheight > MAX_HEIGHT:
                    swidth = img.size[0] / max(MAX_WIDTH, MAX_HEIGHT)
                    sheight = img.size[1] / max(MAX_WIDTH, MAX_HEIGHT)
                img = img.resize((math.floor(img.size[0] / swidth), math.floor(img.size[1] / sheight)))
                tempdir = tempfile.gettempdir()
                img.save(tempdir + '\\ML-Tagger\\img.png')
                filename = tempdir + '\\ML-Tagger\\img.png'

            appWindow["-TOUT-"].update(filename)
            appWindow["-GET_TAGS-"].update(disabled=False)
            appWindow["-PREVIEW_IMAGE-"].update(filename=filename)
        elif event == "-GET_TAGS-":
            print("WIP")

appWindow.close()