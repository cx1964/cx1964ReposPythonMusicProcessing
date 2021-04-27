# file: music_2.py
# doc: https://www.analyticsvidhya.com/blog/2020/01/how-to-perform-automatic-music-generation/

#for listing down the file names
import os

#Array Processing
import numpy as np

#specify the path
path='schubert/'

#read all the filenames
files=[i for i in os.listdir(path) if i.endswith(".mid")]

#reading each midi file
notes_array = np.array([m.read_midi(path+i) for i in files])