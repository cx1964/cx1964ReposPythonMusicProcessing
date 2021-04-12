# file: my_uilities.copy
# function: miscellaneous utility functions

import numpy as np

import music21 as m
import noteconversion as nc

def roundTo(numberValue, baseValue):
    """
    Round a numberValue, to multiples of baseValue

    Parameters:
    numberValue: a number to round
    baseValue:   a number multiples
    """
    # Round a numberValue, to multiples of baseValue
    return( numberValue + (baseValue - numberValue) % baseValue ) # roundTo


def import_musicxml_file(scorePath, museScoreFile):
    """
    Import musicfile in musicxml format and
    Return numpy arrays X and Y with musical information
    X contains measure number
    Y contains offest in current measure
   
    Params
    scorePath      a string which contains a filepath to input score 
    museScoreFile  a string which contains the filename of the input music file
    """

    myScore = m.converter.parse(scorePath+'/'+museScoreFile, format='musicxml')

    print("Hier")
    
    # Get used TimeSignature of input file
    for e in myScore.recurse().getElementsByClass('TimeSignature'):   # meter.timeSignature:
        print("time signature score:  ", e)
    used_time_signature = e # Because of grant staff only use the last

    # Get used KeySignature of input file
    for e in myScore.recurse().getElementsByClass('KeySignature'):   # meter.timeSignature:
        print("key signature score:  ", e)
    used_key_signature = e # Because of grant staff only use the last

    time_list = []
    note_property_list=[]
     
    for element in myScore.recurse().notes:
        # Encoding X
        # Fill time
        time_list.append(element.measureNumber)      
        time_list.append(element.offset) 
        #print("Time_list iter:", time_list)
       
        # Encoding Y 
        # Fill note properties
        note_property_list.append(nc.getNoteValue(element.name))
        note_property_list.append(element.octave)
        note_property_list.append(element.duration.quarterLength)
        #print("Note_property_list iter:", note_property_list)
    
    # Create 2 dimensional array for the time list with 2 elements per row
    # First index -1 creates dynamically an amount off rows based on the size of the time list
    X = np.array(time_list).reshape(-1, 2)
    #print("X.shape",X.shape)
    #print(X)
    
    # Create 2 dimension array for the note property list with 3 elements per row
    # First index -1 creates dynamically an amount off rows based on the size of the note list
    Y = np.array(note_property_list).reshape(-1, 3)
    #print("Y.shape",Y.shape)
    #print(Y)
    
    return(X, Y, used_time_signature, used_key_signature) # import_musicxml_file 