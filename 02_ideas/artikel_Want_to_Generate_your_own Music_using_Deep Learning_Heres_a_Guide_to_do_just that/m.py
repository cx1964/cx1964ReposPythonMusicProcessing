# file: m.py
# doc: https://www.analyticsvidhya.com/blog/2020/01/how-to-perform-automatic-music-generation/

import music21 as m


# source from music_1.py
#defining function to read MIDI files
def read_midi(file):
    
    print("Loading Music File:",file)
    
    notes=[]
    notes_to_parse = None
    
    #parsing a midi file
    midi = m.converter.parse(file)
  
    #grouping based on different instruments
    s2 = m.instrument.partitionByInstrument(midi)

    #Looping over all the instruments
    for part in s2.parts:
    
        #select elements of only piano
        if 'Piano' in str(part): 
        
            notes_to_parse = part.recurse() 
      
            #finding whether a particular element is note or a chord
            for element in notes_to_parse:
                
                #note
                if isinstance(element, m.note.Note):
                    notes.append(str(element.pitch))
                
                #chord
                elif isinstance(element, m.chord.Chord):
                    notes.append('.'.join(str(n) for n in element.normalOrder))

    return np.array(notes)



# source form music_2.py
#for listing down the file names
import os

#Array Processing
import numpy as np

#specify the path
path='midi_music/' # 'schubert/'

#read all the filenames
files=[i for i in os.listdir(path) if i.endswith(".mid")]

#reading each midi file
# for usage of dtype=object
# see also https://stackoverflow.com/questions/65980867/numpy-visibledeprecationwarning-creating-an-ndarray-from-ragged-nested-sequence
# The object dtype array preserves the type of the inputs.
notes_array = np.array([read_midi(path+i) for i in files], dtype=object) 


# source form music_3.py
#converting 2D array into 1D array
notes_ = [element for note_ in notes_array for element in note_]

#No. of unique notes
unique_notes = list(set(notes_)) # set function returns unique notes
print("unique_notes:",len(unique_notes))


# source form music_4.py
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