import torch
import torch.nn as nn
import torchvision.models as model


class ExModel(nn.Module):
    
    def __init__(self):
        super().__init__()
                
        self.model = model.resnet18(pretrained=False)
        self.model = torch.nn.Sequential(*(list(self.model.children())[:-1]))    
        
        self.classifier = torch.nn.Linear(1024, 1000) #TODO Change this classifier according to your application!


    def forward(self, image):
        # Get predictions from ResNet18
        resnet_pred = self.model(image).squeeze()
        out = self.classifier(resnet_pred)
        
        return out
    