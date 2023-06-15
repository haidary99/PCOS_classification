# PCOS Detection in Ultrasound Images via Deep Learning and CNNs
## Abstract:
This project presents a study on the use of deep convolutional neural networks (CNN) models such as DenseNet models to classify ovarian ultrasound images into healthy and infected cases. A much smaller model (IustNet) is also built from scratch in which its performance is compared to the DenseNet models. The datasets used in the study consisted of healthy ovaries and ovaries with Polycystic Ovary Syndrome (PCOS). Using transfer learning, a pre-trained DenseNet201 model was fine-tuned to train on the available dataset. Then, a DenseNet121d model is trained from scratch on the same dataset. Finally, IustNet is built from scratch and trained also on the dataset. Performance of the three models on the dataset was evaluated using accuracy, precision, and recall. Results of the study showed that DenseNet121d achieved the most desired outcome due to obtaining the highest recall which of utmost importance in medical classification tasks. The accuracy of the proposed model was able to achieve a somewhat satisfactory accuracy of roughly 72% on the test set. The suggested model was also deployed on the web for accessibility by doctors for usage as a decision support system. Lastly, the study also highlights the importance of the quality of the dataset in achieving more accurate results. This research contributes to the growing body of literature on the application of deep learning in medical imaging and has the potential to be applied to other medical imaging tasks. 

# All code for this project (main jupyter notebooks and python scripts) are available here on github. The 3 datasets used in this project are linked below:
1. [Dataset A](https://drive.google.com/drive/folders/1qPZkE1gftaioks28DPixCuQZ-lqCjMEJ?usp=sharing)
2. [Dataset B](https://drive.google.com/drive/folders/1VqDvcmG3UuQFhyO8LWoa7iLssnO8aUEN?usp=sharing)
3. [Dataset B modified](https://drive.google.com/drive/folders/1EIEZz6wjhcxYBjtS6W-ngT6vyR35PmY2?usp=sharing)
***
[Deplyed model on Hugging Face Spaces](https://huggingface.co/spaces/Haidary/PCOS_detector)
***
Links to the trianed PyTorch models: 
1. Fine-tuned [DenseNet201](https://drive.google.com/file/d/13wckgFIl6i1FMjUyfVLdkRkDNBHTrnKQ/view?usp=share_link) model.
2. Trained [DenseNet121d](https://drive.google.com/file/d/1_TmP-vqdl7JvvxaNlhTynvTmbbZnN8PF/view?usp=drive_link) model from scratch.
3. [IustNet](https://drive.google.com/file/d/1-0P-C66B3gg5SLZi2BOHHHqLLGIqjgFm/view?usp=sharing) model that is built from scratch and trained.
