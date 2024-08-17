#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#                                                                             
# PROGRAMMER: Marah Dwikat
# DATE CREATED:  30-5-2024                               
# REVISED DATE: 30-5-2024
# PURPOSE: Create a function classify_images that uses the classifier function 
#          to create the classifier labels and then compares the classifier 
#          labels to the pet image labels. This function inputs:
#            -The Image Folder as image_dir within classify_images and function 
#             and as in_arg.dir for function call within main. 
#            -The results dictionary as results_dic within classify_images 
#             function and results for the functin call within main.
#            -The CNN model architecture as model wihtin classify_images function
#             and in_arg.arch for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           classifier label as the item at index 1 of the list and the comparison 
#           of the pet and classifier labels as the item at index 2 of the list.
#
##
# Imports classifier function for using CNN to classify images 
from classifier import classifier 
from os import listdir
# TODO 3: Define classify_images function below, specifically replace the None
#       below by the function definition of the classify_images function. 
#       Notice that this function doesn't return anything because the 
#       results_dic dictionary that is passed into the function is a mutable 
#       data type so no return is needed.
# 
def classify_images(images_dir, results_dic, model):
    """
    Creates classifier labels with the classifier function, compares pet labels to 
    the classifier labels, and adds the classifier label and the comparison of 
    the labels to the results dictionary using the extend function. Be sure to
    format the classifier labels so that they will match your pet image labels.
    The format will include putting the classifier labels in all lowercase 
    letters and stripping the leading and trailing whitespace characters from them.
    Parameters: 
      images_dir - The (full) path to the folder of images that are to be
                   classified by the classifier function (string)
      results_dic - Results Dictionary with 'key' as image filename and 'value'
                    as a List. Where the list will contain the following items: 
                    index 0 = pet image label (string)
                    --- where index 1 & index 2 are added by this function ---
                    NEW - index 1 = classifier label (string)
                    NEW - index 2 = 1/0 (int)  where 1 = match between pet image
                                     and classifier labels, and 0 = no match between labels
      model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images,
              values must be either: resnet, alexnet, vgg (string)
    Returns:
           None - results_dic is a mutable data type, so no return is needed.         
    """
    filename_list = listdir(images_dir)

    for filename in filename_list:
        low_pet_image = filename.lower()
        word_list_pet_image = low_pet_image.split("_")
        pet_name = " ".join([word for word in word_list_pet_image if word.isalpha()])
        results_dic[filename] = [pet_name.strip()]

    for filename in results_dic:
        classifier_label = classifier(images_dir + filename, model)
        formatted_label = classifier_label.lower().strip()
        results_dic[filename].extend([formatted_label])

        if results_dic[filename][0] in formatted_label:
            results_dic[filename].extend([1])
        else:
            results_dic[filename].extend([0])