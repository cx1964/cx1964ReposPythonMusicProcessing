# File: readMusicXML_music21_py3.py
# Function: Sample how to read a sheetmusic file in MusicXML format
#           with music21
# 

import music21 as m
import numpy as np

musescoreProg='MuseScore-3.6.2.548021370-x86_64_461d9f78f967c0640433c95ccb200785.AppImage'
scorePath = "/home/claude/Documents/sources/python/python3/cx1964ReposPythonMusicProcessing"
# Export de MuseScore File in musicxml (uncompressed music xml format musicxml extention)
museScoreFile  = "C_major_scale_ascending.musicxml" # in musicxml uncompressed
museScoreFile2 = "F_major_scale_ascending_8th_notes.musicxml" # in musicxml uncompressed
museScoreFile3 = "C_major_scale_ascending_mixed_duration.musicxml" # in musicxml uncompressed
keyC    = m.key.Key('C') #  lowercase = c minor. uppercase = C major
keyCmin = m.key.Key('c') #  lowercase = c minor. uppercase = C major

def getNoteValue(noteName):
    # Convert a NoteName in a numeric value
    # In music a flat is notated as -
    # Bb = B-
    noteValues = { 
                   'C' : 0, 'B-' : 0, 
                   'C#': 1, 'D-' : 1,
                   'D' : 2, 'C##': 2,
                   'D#': 3, 'Eb' : 3,
                   'E' : 4,

                   'F' : 5, 'E#' : 5,
                   'F#': 6, 'G-' : 6,
                   'G' : 7, 'F##': 7,
                   'G#': 8, 'A-' : 8,
                   'A' : 9, 'B--': 9,
                   'A#':10, 'B-' :10,
                   'B' :11, 'C-' :11
                   # ToDo
                   # append all double sharps
                   # append all double flats
                 }
    return(noteValues[noteName])


def getNoteName(noteValue, enharmonic=False):
    # Convert a NoteValue in a string with a noteName
    # In music a flat is notated as -
    # Bb = B-
    if enharmonic==False:
        noteName = { 
                     0: 'C' ,  
                     1: 'C#',  
                     2: 'D' , 
                     3: 'D#', 
                     4: 'E' ,
                     5: 'F' , 
                     6: 'F#', 
                     7: 'G' , 
                     8: 'G#', 
                     9: 'A' , 
                    10: 'A#', 
                    11: 'B'  
                   }
    else:
        noteName = { 
                     0: 'B-' ,
                     1: 'D-' ,
                     2: 'C##',
                     3: 'Eb' ,
                     4: 'E'  , # because no enharmonic available. x =def enharmonic(x)
                     5: 'E#' ,
                     6: 'G-' ,
                     7: 'F##',
                     8: 'A-' ,
                     9: 'B--',
                    10: 'B-' ,
                    11: 'C-' 
                   # ToDo
                   # append all double sharps
                   # append all double flats
                   }                 
    return(noteName[noteValue])


# Test conversion Note to noteValue
#print("noteValues['C#']",getNoteValue('C#'))
#ns='D#'
#print("noteValues['"+ns+"']",getNoteValue(ns))
#print("\n\n")
# Test conversion noteValue to Note
#for v in range(0,12,1):
#  n=getNoteName(v, enharmonic=False)
#  print(v,n)
#  n=getNoteName(v, enharmonic=True)
#  print(v,n)


# See: https://web.mit.edu/music21/doc/usersGuide/usersGuide_24_environment.html#usersguide-24-environment
# See: https://web.mit.edu/music21/doc/usersGuide/usersGuide_24_environment.html
env = m.environment.UserSettings()
env.delete()
env.create()
# set environmment
env['autoDownload'] = 'allow'
#env['lilypondPath'] = '/usr/bin/lilypond'
#env['musescoreDirectPNGPath'] = '/usr/bin/musescore3'
env['musicxmlPath'] = '/home/claude/Applications/'+musescoreProg

myScore  = m.converter.parse(scorePath+'/'+museScoreFile , format='musicxml')
myScore2 = m.converter.parse(scorePath+'/'+museScoreFile2, format='musicxml')
myScore3 = m.converter.parse(scorePath+'/'+museScoreFile3, format='musicxml')
#print("type(myScore):", type(myScore))



time_list = []
note_property_list=[]

# parse Stream structure of musicfile 
#for thing in myScore:
#    print(thing)

# Alternative
#myScore.show('text')  

# https://web.mit.edu/music21/doc/usersGuide/usersGuide_06_stream2.html
'''
for e in myScore.recurse():
    #print(e)
    print(e.offset, e, e.activeSite)
print("\n\n")
'''

# https://web.mit.edu/music21/doc/usersGuide/usersGuide_06_stream2.html
'''
# get the notes
for e in myScore.recurse().notes:
    #print(e)
    print(e.offset,e.name, e.octave, e.fullName, e.activeSite, "notevalue:", getNoteValue(e.name))
    #print(e.fullName)

    # ToDo
    # To prepare for AI convert NoteName to numeric Value with function getNoteValue
'''

'''
print("\n\n")
for e2 in myScore2.recurse().notes:
    #print(e2)
    print(e2.offset,e2.name, e2.octave, e2.fullName, e2.activeSite, "Notevalue:", getNoteValue(e2.name))
    #print(e.fullName)
'''

print("\n\n")
for e3 in myScore3.recurse().notes:
    #print(e3)
    #print(  "Measure:", e3.measureNumber
    #      ,"Note Offset in Measure:", e3.offset
    #      ,"Note:", e3.name
    #      ,"Octave:", e3.octave
    #      ,e3.nameWithOctave
    #      ,"Notevalue:", getNoteValue(e3.name)
    #      ,"Note duration:", e3.duration.type
    #      ,"Note quarterlength:", e3.duration.quarterLength
    #)

    # Fill time
    time_list.append(e3.measureNumber)      
    time_list.append(e3.offset) 
    #print("Time_list iter:", time_list)

    # File note properties
    note_property_list.append(e3.name)
    note_property_list.append(e3.octave)
    note_property_list.append(e3.duration.quarterLength)
    #print("Note_property_list iter:", note_property_list)

# Create 2 dimensional array for the time list with 2 elements per row
# First index -1 creates dynamically an amount off rows based on the size of the time list
X = np.array(time_list).reshape(-1, 2)
print("X.shape",X.shape)
print(X)

# Create 2 dimension array for the note property list with 3 elements per row
# First index -1 creates dynamically an amount off rows based on the size of the note list
Y = np.array(note_property_list).reshape(-1, 3)
print("Y.shape",Y.shape)
print(Y)

# ToDo
# 2. create X array (Measure, Note offset in Measure) Y array (Notevalue, Ocatve, NoteDuration )



#ToDo plot the  data to viualize the data
    
    
# load sheetmusic in musescore
#myScore.show()  
