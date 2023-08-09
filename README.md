# PCOS Detection in Ultrasound Images via Deep Learning and CNNs
## Abstract:
This project presents a study on the use of deep convolutional neural networks (CNN) models such as DenseNet models to classify ovarian ultrasound images into healthy and infected cases. A much smaller model (IustNet) is also built from scratch in which its performance is compared to the DenseNet models. The datasets used in the study consisted of healthy ovaries and ovaries with Polycystic Ovary Syndrome (PCOS). Using transfer learning, a pre-trained DenseNet201 model was fine-tuned to train on the available dataset. Then, a DenseNet121d model is trained from scratch on the same dataset. Finally, IustNet is built from scratch and trained also on the dataset. Performance of the three models on the dataset was evaluated using accuracy, precision, and recall. Results of the study showed that DenseNet121d achieved the most desired outcome due to obtaining the highest recall which of utmost importance in medical classification tasks. The accuracy of the proposed model was able to achieve a somewhat satisfactory accuracy of roughly 72% on the test set. The suggested model was also deployed on the web for accessibility by doctors for usage as a decision support system. Lastly, the study also highlights the importance of the quality of the dataset in achieving more accurate results. This research contributes to the growing body of literature on the application of deep learning in medical imaging and has the potential to be applied to other medical imaging tasks. 
***
Frameworks and Libraries used: PyTorch, Matplotlib, Pandas, imgaug, Gradio <br>
1. PyTorch was used for transfer learning, import, build, and train CNN models. <br>
2. Matplotlib was used for visualizing and graphing training result metrics such as training and test accuracies. <br>
3. Pandas was to extract valuable information when comparing performance of the different models. <br>
4. imgaug was used to artificially create new Ultrasound images from existent ones due to small size of the dataset (Data augmentation) <br>
5. Gradio was used to build an interface for the model to make it accessible through a web application which is hosted on Hugging Face Spaces.
***
[Deplyed model on Hugging Face Spaces](https://huggingface.co/spaces/Haidary/PCOS_detector)
***

# All code for this project (main jupyter notebooks and python scripts) are available here on github. The 3 datasets used in this project are linked below: <br>
Sources of these datasets and how they are obtained are disscussed in detail within the project thesis.
1. [Dataset A](https://drive.google.com/drive/folders/1qPZkE1gftaioks28DPixCuQZ-lqCjMEJ?usp=sharing). This publically available  dataset [available on Kaggle](https://www.kaggle.com/datasets/anaghachoudhari/pcos-detection-using-ultrasound-images) was discovered to be erroneous and misleading during the work on this project. 
2. [Dataset B](https://dataverse.telkomuniversity.ac.id/dataset.xhtml?persistentId=doi:10.34820/FK2/QVCP6V)
3. [Dataset B modified](https://drive.google.com/drive/folders/1EIEZz6wjhcxYBjtS6W-ngT6vyR35PmY2?usp=sharing) - Modified by Image Augmentation techniques to artificially increase the number of available images.

***
Links to the trianed PyTorch models: 
1. Fine-tuned [DenseNet201](https://drive.google.com/file/d/13wckgFIl6i1FMjUyfVLdkRkDNBHTrnKQ/view?usp=share_link) model.
2. Trained [DenseNet121d](https://drive.google.com/file/d/1_TmP-vqdl7JvvxaNlhTynvTmbbZnN8PF/view?usp=drive_link) model from scratch.
3. [IustNet](https://drive.google.com/file/d/1-0P-C66B3gg5SLZi2BOHHHqLLGIqjgFm/view?usp=sharing) model that is built from scratch and trained.
***

Published 2 research papers due to the work on this project both of which available on Google Scholar:
1. [The Effectiveness of CNN in Evaluating Ultrasound Image Datasets: Diagnosing Polycystic Ovary Syndrome (PCOS) as an Example](https://www.hcsr.gov.sy/sjsi/no.1/) -The Syrian Journal for Science and Innovation 1(1), 85-96. 
2. [Diagnosing Polycystic Ovary Syndrome (PCOS) Using an Enhanced Transfer Learning Model](https://www.damascusuniversity.edu.sy/mag/conference/index.php?lang=1&set=3&id=431) - Damascus University Journal
