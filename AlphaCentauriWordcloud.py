# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 12:43:03 2019

@author: Miriam
"""

from os import path
import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

# Please change the working directory to your path!
root_path = os.getcwd()

# Read the whole text.
with open(path.join(root_path, 'BlurbsEdit.txt'), 'r', encoding='utf-8', errors='ignore') as outout_file:
    text = outout_file.readlines()


# Mask
suns_pic = np.array(Image.open(path.join(root_path, "peace3.jpg")))

stopwords = set(STOPWORDS)
stopwords.add("will")
stopwords.add("us")
stopwords.add("one")

# Construct Word Cloud
# no backgroundcolor and mode = 'RGBA' create transparency
wc = WordCloud(max_words=1000, mask=suns_pic,
               stopwords=stopwords, mode='RGBA', background_color=None)

# Pass Text
wc.generate(text[0])

# store to file
wc.to_file(path.join(root_path, "alphacentauriwords.png"))

# to show the picture 
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")# 
plt.show()
