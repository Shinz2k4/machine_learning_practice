import torch
import torch.nn as nn
from torchvision import datasets, transforms, models
from torch.utils.data import DataLoader

# Transform: resize, crop, normalize
transform = {
    "train": transforms.Compose([
        transforms.Resize((128,128)),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize([0.5,0.5,0.5], [0.5,0.5,0.5])  # scale về [-1,1]
    ]),
    "val": transforms.Compose([
        transforms.Resize((128,128)),
        transforms.ToTensor(),
        transforms.Normalize([0.5,0.5,0.5], [0.5,0.5,0.5])
    ])
}

train_dataset = datasets.ImageFolder("../../datas/dogs_cats/train", transform=transform["train"])
val_dataset = datasets.ImageFolder("../../datas/dogs_cats/val", transform=transform["val"])

train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=32, shuffle=False)


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f'{device}')
print('data: ',train_dataset)


class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 32, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2),
            nn.Conv2d(32, 64, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2),
            nn.Conv2d(64, 128, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2),
        )
        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(128 * 16 * 16, 256), nn.ReLU(), nn.Dropout(0.5),
            nn.Linear(256, 1), nn.Sigmoid()
        )

    def forward(self, x):
        x = self.features(x)
        x = self.classifier(x)
        return x
    



class SGD:
    def __init__(self, params, lr=0.01, momentum=0.0, weight_decay=0.0):
        self.params = list(params)
        self.lr = lr
        self.momentum = momentum
        self.weight_decay = weight_decay
        self.velocity = {id(p): torch.zeros_like(p.data) for p in self.params}

    def step(self):
        for p in self.params:
            if p.grad is None:
                continue

            grad = p.grad.data
            if self.weight_decay != 0:
                grad = grad + self.weight_decay * p.data

            if self.momentum != 0:
                v = self.velocity[id(p)]
                v.mul_(self.momentum).add_(grad)
                update = v
            else:
                update = grad

            p.data -= self.lr * update

    def zero_grad(self):
        for p in self.params:
            if p.grad is not None:
                p.grad.zero_()

def bce_loss(outputs, targets, eps=1e-7):
    outputs = torch.clamp(outputs, eps, 1 - eps)
    loss = - (targets * torch.log(outputs) + (1 - targets) * torch.log(1 - outputs))
    return loss.mean()


model = SimpleCNN().to(device)
criterion = bce_loss
optimizer = SGD(model.parameters(), lr=0.005)

num_epochs = 10
for epoch in range(num_epochs):
    model.train()
    total_loss, correct, total = 0, 0, 0
    for imgs, labels in train_loader:
        imgs, labels = imgs.to(device), labels.float().unsqueeze(1).to(device)
        
        optimizer.zero_grad()
        outputs = model(imgs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        
        total_loss += loss.item()
        preds = (outputs > 0.5).float()
        correct += (preds == labels).sum().item()
        total += labels.size(0)

    acc = correct / total
    print(f"Epoch [{epoch+1}/{num_epochs}] Loss: {total_loss/len(train_loader):.4f} Acc: {acc:.4f}")


model.eval()
correct, total = 0, 0
with torch.no_grad():
    for imgs, labels in val_loader:
        imgs, labels = imgs.to(device), labels.float().unsqueeze(1).to(device)
        outputs = model(imgs)
        preds = (outputs > 0.5).float()
        correct += (preds == labels).sum().item()
        total += labels.size(0)

print(f"Validation Accuracy: {100*correct/total:.2f}%")
