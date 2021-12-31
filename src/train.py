# Trains the AI model. Requires a data/ folder with the training data.

import os
import json
import PIL.Image

import torch
from torch import nn, optim
from torch.utils.data import DataLoader
from torchvision.transforms import transforms

import numpy as np
from tqdm import tqdm

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


class ImageDataset(torch.Dataset):
    def __init__(self):
        self.labels = json.load(os.path.join("data", "labels.json"))
        self.imgs = self.labels.keys()
        self.img_dir = "data/imgs"
        self.transform = transforms.Compose((
            transforms.PILToTensor(),
            transforms.Resize((512, 512))
        ))
        # TODO: Implement target_transform to convert list of labels to list of 1. and 0.
        self.target_transform = lambda labels: torch.Tensor([])
    
    def __len__(self):
        return len(self.labels)
    
    def __getitem__(self, i):
        img_path = os.path.join(self.img_dir, self.imgs[i])
        image = PIL.Image.open(img_path)
        label = self.labels[img_path.split(".")[0]]
        if self.transform:
            image = self.transform(image)
        if self.target_transform:
            label = self.target_transform(label)
        return image, label


def main():
    if not os.path.exists("data"):
        print("You don't have a data folder!")
        exit()

    if not os.path.exists("data/labels.json"):
        print("You don't have any labels!")
        exit()
    
    device = "cuda" if torch.cuda.is_available() else "cpu"

    dataloader = DataLoader(ImageDataset(), 500, True)

    model = Net().to(device)
    model.train()

    criterion = nn.MSELoss()

    image = torch.Tensor(np.zeros((1, 3, 512, 512))).to(device)

    correct = torch.Tensor(np.asarray([1 for i in range(601)]).reshape((1, 601))).to(device)

    epochs = 5

    optimizer = optim.Adam(model.parameters(), lr=1e-3, betas=(0.5, 0.999))

    for epoch in tqdm(range(epochs)):
        optimizer.zero_grad()
        output = model(image)
        loss = criterion(output, correct)
        loss.backward()
        optimizer.step()
        # let me copyu from wiki real quick 
        # ^ programmer mindset

    model.eval()
    model.to('cpu')
    torch.save(model.state_dict(), "weights.pth")
    # weights.pth now has proper values
    model.to(device)
    print(model(torch.Tensor(np.zeros((1, 3, 512, 512))).to(device)).cpu())


if __name__ == "__main__":
    main()
    exit()

print("This is meant to be run as a file, not imported as a module.")