# file: music_4.py
# doc: https://www.analyticsvidhya.com/blog/2020/01/how-to-perform-automatic-music-generation/

#importing library
from collections import Counter

#computing frequency of each note
freq = dict(Counter(notes_))

#library for visualiation
import matplotlib.pyplot as plt

#consider only the frequencies
no=[count for _,count in freq.items()]

#set the figure size
plt.figure(figsize=(5,5))

#plot
plt.hist(no)