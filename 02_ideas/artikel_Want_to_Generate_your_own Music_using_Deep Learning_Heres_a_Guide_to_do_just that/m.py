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



# source form music_2/py
#for listing down the file names
import os

#Array Processing
import numpy as np

#specify the path
path='midi_music/' # 'schubert/'

#read all the filenames
files=[i for i in os.listdir(path) if i.endswith(".mid")]

#reading each midi file
notes_array = np.array([read_midi(path+i) for i in files])
