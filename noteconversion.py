# File: noteconversion.py
# Function: module noteconversion
#           Convert note to noteValue and
#           convert noteValue to note

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
    return(noteValues[noteName.upper()])


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