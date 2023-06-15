#!pip install timm==0.6.13
import torch
import timm

from torchvision import transforms

def create_DenseNet121_model(): # Returns trained DenseNet121 model and its transforms
  model_file = "DenseNet121d_22_From_Scratch_model0.pth"
  model = torch.load(model_file, map_location=torch.device('cpu'))

  transform = transforms.Compose([
    transforms.Resize((224, 224)), # 1. Reshape all images to 224x224
    transforms.ToTensor(), # Turn pixel values to between 0 & 1
    transforms.Normalize(mean=[0.485, 0.456, 0.406], # 3. A mean of [0.485, 0.456, 0.406] (across each colour channel)
                         std=[0.229, 0.224, 0.225]), # 4. A standard deviation of [0.229, 0.224, 0.225] (across each colour channel)
    transforms.Grayscale() ##### change number of color channels from 3 to 1 (I added this)
  ])

  return model, transform
