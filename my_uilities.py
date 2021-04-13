# file: my_uilities.copy
# function: miscellaneous utility functions

from datetime import date
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



def create_estimated_score(  X_new
                            ,Y_pred
                            ,base
                            ,time_signature_input_file
                            ,key_signature_input_file
                            ,score_title
                            ,composer
                           ):
    """
    Create a music Score based on predicted music information

    Params
    X_new                       a numpy array with measure and offset information in a measure
    Y_pred                      a numpy array with note values, notevalue, octavenumber and quarternoteduration
    base                        a fraction to with noteduration a quarternoteduration has to rounded to (base is 0.25 for quarter note, 0,125 for a 8th note, etc)
    time_signature_input_file   a time signature object with time signaure information of the input file
    key_signature_input_file
    score_title                 a string which contains the score title meta data
    composer                    a string which contains the composer meta data
    """

    # Debug info:
    #print("\n\n")
    #print("Estimated output in notes (Notename, octave and quarterLength):")
    #for r in Y_pred:
    #
    #    # round to a 0.25 resolution because input used 1/4 notes
    #    t=r[2]
    #    BASE=0.25
    #    v=t + (BASE - t) % BASE
    #    print(nc.getNoteName(int(round(r[0])), enharmonic=False),int(round(r[1])), v)


    # *** Create the score with estimated notes ***
    # *********************************************
    # https://web.mit.edu/music21/doc/usersGuide/usersGuide_06_stream2.html
    estimatedScore = m.stream.Stream()

    # Set Meta Data in estimated score
    meta_data = m.metadata.Metadata()
    meta_data.title = score_title
    today = date.today()
    # YYYY/mm/dd
    d1 = today.strftime("%d/%m/%Y")
    meta_data.date = str(d1)
    meta_data.composer = composer+" ("+str(d1)+")"

    upperStaffClef=m.clef.TrebleClef()
    lowerStaffClef=m.clef.BassClef()

    myPart = m.stream.Part()
    myPart_UpperStaff = m.stream.Part()
    # set Clef UpperStaff
    myPart_UpperStaff.append(upperStaffClef)

    # set TimeSignature UpperStaff
    myPart_UpperStaff.append(time_signature_input_file)
    
    # set keySignature UpperStaff
    myPart_UpperStaff.append(key_signature_input_file)
    
    myPart_LowerStaff = m.stream.Part()
    # set Clef UpperStaff
    myPart_LowerStaff.append(lowerStaffClef)

    # set TimeSignature LowerStaff
    myPart_LowerStaff.append(time_signature_input_file)
    
    # set keySignature LowerStaff
    myPart_LowerStaff.append(key_signature_input_file)

    # Do not use a Measure object
    # If you use a Time Signature object without a Measure object
    # when adding a notes, to a stream, measures are filled
    # automatically bases on note lengths
    myNote = m.note.Note()

    myPart_UpperStaff.partName="Piano Upper"
    myPart_LowerStaff.partName="Piano Lower"
    
    print("\n\n")
    print("process measures")
    itrNote = m.note.Note()
    if (X_new.shape[0] == Y_pred.shape[0]):
      # Normal Score
      cnt=0 # counter to sync X and Y (sync time and Notes)
      curMeasure=1
      noteCount=0
      for e in X_new:
    
        # Decoding Y_pred: get note properies  
        # Do the encoding as inverse of the decoding (see above) 
        note_properties = Y_pred[cnt]
        #print("!!! note_properties[", cnt, "]", note_properties)
        curNoteName=nc.getNoteName(int(round(note_properties[0])), enharmonic=False)
        print("curNoteName", curNoteName)
        curNoteOctave =  int(round(note_properties[1]))
        #print("curNoteOctave", curNoteOctave)
    
        # Process quarterDuration
        curNotequarterDuration = roundTo(note_properties[2], base)
    
        itrMeasure=int(e[0])
        itrOffset=e[1]
        print("ToDo itrMeasure=", itrMeasure, "itrOffset:", itrOffset)
    
        myNote=m.note.Note( name=curNoteName
                           ,quarterLength=curNotequarterDuration
                           ,octave=curNoteOctave
                           ,offset=itrOffset
                           #,type="quarter"  # use quarterLength or type not both
                          )
    
        # if you use a time signature object without a measure object then because of
        # the time signature measures are filled automatically by notes based on
        # its note duration
        myPart_UpperStaff.insert(cnt, myNote) 
        noteCount=noteCount+1      
        cnt=cnt+1
        print("cnt:", cnt)  
    else:
      # Unbalanced Score
      print("Program error: Score not balanced")  
    
    estimatedScore.insert(0, meta_data)
    estimatedScore.insert(1, myPart_UpperStaff)
    
    
    # *** Add a dummy LowerStaff with a dummy rest to create a Grand piano staff ***
    # When more staves are used, all staves
    # must be filled, before append to the total stream,
    # otherwise you get a corrupted stream when
    # empty staves are added to the total stream.
    dummyRest = m.note.Rest()
    dummyRest.duration.type='quarter'
    myPart_LowerStaff.insert(cnt, dummyRest)
    # If you do not want a grand staff comment statement below 
    # ToDo problem with creating lowerStaff !!!!!!!!!!!!!!!!!!!!!!
    ##estimatedScore.insert(2, myPart_LowerStaff)
    
    return(estimatedScore) # create_estimated_score