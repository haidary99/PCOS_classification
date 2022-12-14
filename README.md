# PCOS_classification
This project utilizes an ovarian ultrasound image [dataset available on kaggle](https://www.kaggle.com/datasets/anaghachoudhari/pcos-detection-using-ultrasound-images) in which some ovaries are infected with PCOS and others are not. <br>
In this project, I attempt to build a neural network using the PyTorch library that is able to train on this dataset and generalize well on the given images. <br>
Instead of building a neural network from scratch, I make use of an already existing model (DenseNet) which is pre-trained and fine-tune it to make it able to adjust to and process this specific dataset. <br>
The environment I used is Google Colab to make use of the fast GPU it offers for accelerated training. After I finished training on Colab, I saved the model and reloaded it on my local machine (Macbook Air M1) to test it out and it worked very well. <br>
I have also divided some of the code into external Python scripts and placed them inside the going_modular directory in order to reduce the length of the original Jupyter Notebook file and avoid it being too long. <br> <br> 
The below image shows the difference between a polycystic ovary (with PCOS) vs. a normal ovary: <br> <br>
![alt text](pcos.jpeg)
