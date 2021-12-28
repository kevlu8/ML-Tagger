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
            # Define layers here
        )
    def forward(self, x):
        return self.main(x)

def detect(imagePath):
    tags = [
        "placeholder"
    ]
    model = Net()
    model.load_state_dict(torch.load("weights.pth"))
    model.eval()
    return tags[model(transforms.F.pil_to_tensor(PIL.Image.open(imagePath)))]