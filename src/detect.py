# This file is where the detection of objects inside of an image occurs.

if __name__ == "__main__":
    print("You're running the wrong file. Please run main.py instead.")
    exit()

import torch
from torch import nn
from torchvision.transforms import transforms
import PIL.Image

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.main = nn.Sequential(
            nn.Conv2d(3, 64, 4, 2, 1, bias=False),
            nn.LeakyReLU(0.2, True),
            nn.Conv2d(64, 128, 4, 2, 1, bias=False),
            nn.LeakyReLU(0.2, True),
            nn.MaxPool2d(2, 2),
            nn.Conv2d(128, 256, 4, 2, 1, bias=False),
            nn.LeakyReLU(0.2, True),
            nn.MaxPool2d(2, 2),
            nn.Conv2d(256, 512, 4, 2, 1, bias=False),
            nn.LeakyReLU(0.2, True),
            nn.MaxPool2d(2, 2),
            nn.Flatten(),
            nn.Linear(8192, 4096),
            nn.LeakyReLU(0.2, True),
            nn.Linear(4096, 601),
            nn.Sigmoid()
        )

    def forward(self, x):
        return self.main(x)

'''
def detect(imagePath):
    tags = [
        "placeholder"
    ]
    model = train.Net()
    model.load_state_dict(torch.load("weights.pth"))
    model.eval()
    return tags[model(PIL.Image.open(imagePath).convert())]
'''

def detect(imagePath):
    tags = []
    model = Net()
    model.load_state_dict(torch.load("weights.pth"))
    tags = model(transforms.Compose((
  transforms.PILToTensor(),
  transforms.Resize((512, 512)),
))(PIL.Image.open(imagePath)).view((1, 3, 512, 512)))
    # tags = model(PIL.Image.open(imagePath))
    print(tags)
    return tags