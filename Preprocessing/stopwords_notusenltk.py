# -*- coding: utf-8 -*-
"""Stopwords_notUseNLTK.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lXxWQFtEaerc9Vy5d7sKx_9hHRa9o8lo
"""

tulisan="aku dan teman-teman suka jalan"

stp=["dan"]

# https://stackoverflow.com/questions/952914/how-do-i-make-a-flat-list-out-of-a-list-of-lists?page=1&tab=scoredesc#tab-top
def flatten(l):
    """
    Same as 
    flat_list = []
    for sublist in l:
    for item in sublist:
        flat_list.append(item)

    Example =[[1,2,3,4,5]] - > [1,2,3,4,5]
    """
    return " ".join([item for sublist in l for item in sublist])

filter_words=[]
tulisan=tulisan.split()
tulisan=[word for word in tulisan if word not  in stp]
filter_words.append(tulisan)

filter_words

flat_word=flatten(filter_words)

flat_word