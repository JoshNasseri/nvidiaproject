# Rupee Currency Counter

As we progress into the future, we make technology that should further benefit our society. Being able reduce the need for human labor such as casheirs, or bank tellers would now be more possible with the model I have created. This model allows AI to recognise the value of the Rupee presented infront of it. This model could be implemented in robots and machines. This idea has a big impact in India because it would help further their technology.  

This image is the model recognising the amount of Rupeess that is presented infront of it 
<img src="https://i.imgur.com/pdXRqWM.png" width="500" length="400">


## The Algorithm

To get my images, I had looked on kaggle and was able to gather my images of different Rupees. I had run my script.py on my jetson-nano. Though my data was already sorted into its own catagories, I had needed to train Resnet-18 because it was not trained to identify different images on my computer. When running imagenet.py along with my model, it is able to define the value of the rupees that are presented infront of it. 


## Running this project
1. connect the jetson nano to VS code
2. navigate to the jetson-nano 
3. download my project on github using git clone https://github.com/JoshNasseri/nvidiaproject.git
4. download my dataset on kaggle using this link https://www.kaggle.com/datasets/vishalmane109/indian-currency-note-images-dataset-2020
5. zip and upload the file to jetson-nano under the data/Indian_Currency folder
6. Set the NET and DATASET variables
7. NET=model/Indian_Currency/
8. DATASET=data/
9. create new terminal and run the commmand   imagenet.py --model=$NET/resnet18.onnx --input_blob=input_0 --output_blob=output_0 --labels=$DATASET/labels.txt data/Indian_Currency/10__206.jpg 10__206.jpg


 
[View a video explanation here](video link)
