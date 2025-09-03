import torch
import torch.nn as nn 
from torchvision import datasets, transforms, models 
from torch.utils.data import DataLoader

transform = {
    "train_transform":transforms.Compose([
        transforms.Resize((128,128)),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize([0.5,0.5,0.5],[0.5,0.5,0.5])
        ]),
    "val_transform":transforms.Compose([
        transforms.Resize((128,128)),
        transforms.ToTensor(),
        transforms.Normalize([0.5,0.5,0.5],[0.5,0.5,0.5])
    ])
}


train_dataset = datasets.ImageFolder("../../datas/dogs_cats/train", transform = transform["train_transform"])
val_dataset = datasets.ImageFolder("../../datas/dogs_cats/val",transform= transform["val_transform"])

train_loader = DataLoader(train_dataset,batch_size = 32, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size = 32, shuffle= True)

device = ("cuda" if torch.cuda.is_available() else " cpu")
print(f'{device}')

