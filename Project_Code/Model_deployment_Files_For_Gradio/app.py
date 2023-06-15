### 1. Imports and class names setup ###
import gradio as gr
import os
import torch

from model import create_DenseNet121_model
from timeit import default_timer as timer
from typing import Tuple, Dict

# Setup class names
class_names = ['infected', 'notinfected']

### 2. Model and transforms preparation ###

# Create an instance of trained DenseNet121 model
Dense121, transform = create_DenseNet121_model()

### 3. Predict function ###

# Create predict function
def predict(img) -> Tuple[Dict, float]:
  """
  Transforms and performs a prediction on img then returns prediction and time taken
  """
  # Start the timer
  start_time = timer()

  # Transform the target image and add a batch dimension
  img = transform(img).unsqueeze(0)
  
  # Put model into evaluation mode and turn on the inference mode
  Dense121.eval()
  with torch.inference_mode():
    # Pass the transformed image through the model and turn the prediction logit intp prediction probability
    pred_logit = Dense121(img).squeeze()
    pred_prob = torch.sigmoid(pred_logit)
    pred_label = torch.round(pred_prob)
    pred_label = pred_label.type(torch.int64)
    pred_class = class_names[pred_label.cpu()]
    # pred_prob = float(pred_prob) # This line and next one are for formatting the pred_prob to print only 4 decimal places
    # pred_prob = round(pred_prob, 4)

  # Create a prediction label and prediction probability dictionary for each prediction class (this is the required format for Gradio's output parameter)
  pred_label = pred_class 

  # Calculate the prediction time
  pred_time = round(timer() - start_time, 5)

  # Return the prediction dictionary and prediction time
  return pred_label, pred_time

### 4. Gradio app ###

# Create title and description strings
title = "PCOS Detector in Ultrasound Images"
description = "A DenseNet121 feature extractor computer vision model trained from scratch to classify ultrasound images of ovaries into PCOS infected or not infected."
article= "Code implementation available at [GitHub](https://github.com/haidary99?tab=repositories)"

# Create examples list from "examples/" directory
example_list = [["examples/" + example] for example in os.listdir("examples")]

# Create the Gradio demo
demo = gr.Interface(fn=predict, # mapping function from input to output
                    inputs=gr.Image(type="pil"),
                    outputs=[gr.Label(label="Model Prediction"),
                             gr.Number(label="Prediction time (s)")],
                    # Create examples list from "examples/" directory
                    examples=example_list,
                    title=title,
                    description=description,
                    article=article)

# Launch the demo
demo.launch()
