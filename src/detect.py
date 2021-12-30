# This file is where the detection of objects inside of an image occurs.

if __name__ == "__main__":
    print("You're running the wrong file. Please run main.py instead.")
    exit()

import train

import torch
from torch import nn
from torchvision.transforms import transforms
import PIL.Image


def detect(imagePath):
    tags = [
        "placeholder"
    ]
    model = train.Net()
    model.load_state_dict(torch.load("weights.pth"))
    model.eval()
    return tags[model(PIL.Image.open(imagePath).convert())]
