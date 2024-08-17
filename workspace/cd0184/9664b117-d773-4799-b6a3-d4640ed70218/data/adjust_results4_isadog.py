#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py
#                                                                             
# PROGRAMMER: Marah Dwikat
# DATE CREATED:   31-5-2024                              
# REVISED DATE: 31-5-2024
# PURPOSE: Create a function adjust_results4_isadog that adjusts the results 
#          dictionary to indicate whether or not the pet image label is of-a-dog, 
#          and to indicate whether or not the classifier image label is of-a-dog.
#          All dog labels from both the pet images and the classifier function
#          will be found in the dognames.txt file. We recommend reading all the
#          dog names in dognames.txt into a dictionary where the 'key' is the 
#          dog name (from dognames.txt) and the 'value' is one. If a label is 
#          found to exist within this dictionary of dog names then the label 
#          is of-a-dog, otherwise the label isn't of a dog. Alternatively one 
#          could also read all the dog names into a list and then if the label
#          is found to exist within this list - the label is of-a-dog, otherwise
#          the label isn't of a dog. 
#         This function inputs:
#            -The results dictionary as results_dic within adjust_results4_isadog 
#             function and results for the function call within main.
#            -The text file with dog names as dogfile within adjust_results4_isadog
#             function and in_arg.dogfile for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           whether or not the pet image label is of-a-dog as the item at index
#           3 of the list and whether or not the classifier label is of-a-dog as
#           the item at index 4 of the list. Note we recommend setting the values
#           at indices 3 & 4 to 1 when the label is of-a-dog and to 0 when the 
#           label isn't a dog.
#
##
# TODO 4: Define adjust_results4_isadog function below, specifically replace the None
#       below by the function definition of the adjust_results4_isadog function. 
#       Notice that this function doesn't return anything because the 
#       results_dic dictionary that is passed into the function is a mutable 
#       data type so no return is needed.
# 
def adjust_results4_isadog(results_dic, dogfile, results_stats_dic):
    """
    Adjusts the results dictionary to determine if the classifier correctly 
    classified images as 'a dog' or 'not a dog'. This function uses the dog names
    from the classifier function and the pet image files to make the determination.
    The results dictionary is modified to include additional information about
    whether the pet image label and classifier label are dogs or not.
    Parameters:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
                    list. The list contains the following items: 
                    index 0 = pet image label (string)
                    index 1 = classifier label (string)
                    index 2 = 1/0 (int) where 1 = match between pet image
                              and classifier labels, 0 = no match between labels
                    -- Additional items will be added by this function --
                    index 3 = 1/0 (int) where 1 = pet image 'is-a' dog,
                              0 = pet image 'is-NOT-a' dog
                    index 4 = 1/0 (int) where 1 = classifier classifies image 
                              'as-a' dog, 0 = classifier classifies image 
                              'as-NOT-a' dog
     dogfile - A text file that contains names of all dogs from the classifier
               function and dog names from the pet image files.
     results_stats_dic - Dictionary that contains the results statistics (either
                        a percentage or count) where the key is the statistic's
                        name (string) and the value is the statistic's value.
    Returns:
           None - results_dic and results_stats_dic are mutable data types
                  so no return needed.
    """
    dognames_dic = {}
    
    with open(dogfile, "r") as infile:
        line = infile.readline()
        while line != "":
            line = line.strip()
            if line not in dognames_dic:
                dognames_dic[line] = 1
            line = infile.readline()
    
    results_stats_dic['n_dogs_img'] = 0
    results_stats_dic['n_notdogs_img'] = 0

    for key in results_dic:
        if results_dic[key][0] in dognames_dic:
            results_stats_dic['n_dogs_img'] += 1
            if results_dic[key][1] in dognames_dic:
                results_dic[key].extend((1, 1))
            else:
                results_dic[key].extend((1, 0))
        else:
            results_stats_dic['n_notdogs_img'] += 1
            if results_dic[key][1] in dognames_dic:
                results_dic[key].extend((0, 1))
            else:
                results_dic[key].extend((0, 0))

    print("results_stats_dic after adjust_results4_isadog():")
    print(results_stats_dic)