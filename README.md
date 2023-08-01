# Rupee Currency Counter

As we progress into the future, we make technology that should further benefit our society. Being able reduce the need for human labor such as casheirs, or bank tellers would now be more possible with the model I have created. This model allows AI to recognise the value of the Rupee presented infront of it. This model could be implemented in robots and machines. This idea has a big impact in India because it would help further their technology.  

This image is the model recognising the amount of Rupeess that is presented infront of it 
<img src="https://i.imgur.com/pdXRqWM.png" width="500" length="400">


## The Algorithm

To get my images, I had looked on kaggle and was able to gather my images of different Rupees. Though my data was already sorted into its own catagories, I had needed to train Resnet-18 because it was not trained to identify different images on my computer. When running imagenet.py along with my model, it is able to define the value of the rupees that are presented infront of it. 


## Running this project
1. connect the jetson nano to VS code
2. download the file from github
3. move the file into the jetson nano folder
4. drag the testing files 
5. Make sure to have resnet-18.onnx and labels.txt from this project downloaded on the Jetson Nano


Set the NET and DATASET variables
NET=model/Indian_Currency/
DATASET=data/

Run the commmand   imagenet.py --model=$NET/resnet18.onnx --input_blob=input_0 --output_blob=output_0 --labels=$DATASET/labels.txt data/Indian_Currency/10__206.jpg 10__206.jpg

 
[View a video explanation here](video link)
