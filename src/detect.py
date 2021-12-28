# This file is where the detection of objects inside of an image occurs.

if __name__ == '__main__':
    print("You're running the wrong file. Please run main.py instead.")
    exit()

import torch, torchvision
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

def detect(imagePath):
    tags = [
        "placeholder"
    ]
    return tags