# parse the command line
import argparse
import sys
import os
import shutil

from jetson_inference import imageNet
from imagenet import process_images
from jetson_utils import videoSource, videoOutput, Log

parser = argparse.ArgumentParser(description="Classify a live camera stream using an image recognition DNN.", 
                                 formatter_class=argparse.RawTextHelpFormatter, 
                                 epilog=imageNet.Usage() + videoSource.Usage() + videoOutput.Usage() + Log.Usage())

parser.add_argument("input", type=str, default="", nargs='?', help="URI of the input stream")
parser.add_argument("output", type=str, default="", nargs='?', help="URI of the output stream")
parser.add_argument("--network", type=str, default="googlenet", help="pre-trained model to load (see below for options)")
parser.add_argument("--topK", type=int, default=1, help="show the topK number of class predictions (default: 1)")

try:
	args = parser.parse_known_args()[0]
except:
	print("")
	parser.print_help()
	sys.exit(0)

# define a variable called error
categories = os.listdir(args.input)
total = 0
error = 0
# get the length of the input folder and assign it to a variable called length
images = os.listdir(args.input)
length = len(images)

def check_output(catagory, labels):
    for label in labels:
        if category in label:
            return True
    return False

# loop through images in input
for category in categories:
    category_folder_path = os.path.join(args.input, category)
    result_category_folder_path = os.path.join(args.output, category)

    if os.path.exists(result_category_folder_path):
        shutil.rmtree(result_category_folder_path)
    os.makedirs(result_category_folder_path, exist_ok=True)

    images = os.listdir(category_folder_path)

    total += len(images)

    for image in images:
        image_path = os.path.join(category_folder_path, image)
        output_path = os.path.join(result_category_folder_path, "test_{}".format(image))

        labels = process_images(image_path, output_path, args.network, args.topK)

        if not check_output(category, labels):
                error += 1
    # call process_image() with image, output folder path, network, and topK and assign the result to a variable called labels
    # loop through the labels list to check if the folder name is in the list
accuracy = (total - error) / total
print("Accuracy: ", accuracy)

# if the folder name (correct label) is not in the list, add one to error

# outside the loop, calculate the accuracy:
# accuracy = (total - error) / total

# print("accuracy: ", accuracy)