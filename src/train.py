# Trains the AI model. Requires a data/ folder with the training data.

def main():
    import os

    if not os.path.exists("data"):
        print("You don't have a data folder!")
        exit()

    if not os.path.exists("weights.pth"):
        print("You don't have any weights!")
        exit()

    if not os.path.exists("data/labels.json"):
        print("You don't have any labels!")
        exit()

    # import torch
    from torch import nn
    # from torchvision.transforms import transforms
    # import PIL

    class Net(nn.Module):
        def __init__(self):
            super(Net, self).__init__()
            self.main = nn.Sequential(
                # Define layers here
            )

        def forward(self, x):
            return self.main(x)


if __name__ == "__main__":
    main()
    exit()

print("This is meant to be run as a file, not imported as a module.")
