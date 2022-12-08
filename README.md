# PCOS_classification
This project utilizes an ovarian ultrasound image [dataset available on kaggle](https://www.kaggle.com/datasets/anaghachoudhari/pcos-detection-using-ultrasound-images) in which some ovaries are infected with PCOS and others are not.
In this project, I attempt to build a neural network using the PyTorch library that is able to train on this dataset and generalize well on the given images. 
instead of building a neural network from scratch, I make use of an already existing model (DenseNet) which is pre-trained and fine-tune it to make it able to adjust to and process this specific dataset.
