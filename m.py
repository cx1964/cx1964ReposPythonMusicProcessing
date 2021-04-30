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
# show output in a seprate window
plt.show()

# source form music_5.py
frequent_notes = [note_ for note_, count in freq.items() if count>=50]
print("frequent_notes (count>=50):",len(frequent_notes))

new_music=[]

for notes in notes_array:
    temp=[]
    for note_ in notes:
        if note_ in frequent_notes:
            temp.append(note_)            
    new_music.append(temp)
    
new_music = np.array(new_music, dtype=object)

# source form music_6.py
no_of_timesteps = 32
x = []
y = []

for note_ in new_music:
    for i in range(0, len(note_) - no_of_timesteps, 1):
        
        #preparing input and output sequences
        input_ = note_[i:i + no_of_timesteps]
        output = note_[i + no_of_timesteps]
        
        x.append(input_)
        y.append(output)
        
x=np.array(x)
y=np.array(y)

# source from music_7.py
# Now, we will assign a unique integer to every note:
unique_x = list(set(x.ravel()))
x_note_to_int = dict((note_, number) for number, note_ in enumerate(unique_x))

# We will prepare the integer sequences for input data
#preparing input sequences
x_seq=[]
for i in x:
    temp=[]
    for j in i:
        #assigning unique integer to every note
        temp.append(x_note_to_int[j])
    x_seq.append(temp)
    
x_seq = np.array(x_seq)


# Similarly, prepare the integer sequences for output data as well
unique_y = list(set(y))
y_note_to_int = dict((note_, number) for number, note_ in enumerate(unique_y)) 
y_seq=np.array([y_note_to_int[i] for i in y])

# Let us preserve 80% of the data for training and the rest 20% for the evaluation:
from sklearn.model_selection import train_test_split
x_tr, x_val, y_tr, y_val = train_test_split(x_seq,y_seq,test_size=0.2,random_state=0)



import keras.backend as K

K.clear_session()

import my_ai_models as mm
# config used deep learning model
#model=mm.lstm() # use lstm() or WaveNet()
                 # beware lstm() in lstm.py does not work yet. Problem with model.add(Dense(n_vocab))
#model=mm.WaveNet() # use lstm() or WaveNet()
units=[2, 4, 4, 4] # ToDo find correct values for units list
model=mm.gru(units)
model.summary() 

# ToDo2
# Finish from
# "Define the callback to save the best model during training:"
# in https://www.analyticsvidhya.com/blog/2020/01/how-to-perform-automatic-music-generation/