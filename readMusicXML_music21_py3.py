# File: readMusicXML_music21_py3.py
# Function: Sample how to read a sheetmusic file in MusicXML format
#           with music21
# 

import music21 as m

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
                   'F' : 6, 'E#' : 6,
                   'F#': 7, 'G-' : 7,
                   'G' : 8, 'F##': 8,
                   'G#': 9, 'A-' : 9,
                   'A' :10, 'B--': 10,
                   'A#':11, 'B-' :11,
                   'B' :12, 'C-' :12
                   # ToDo
                   # append all double sharps
                   # append all double flats
                 }
    return(noteValues[noteName])

#ToDo
# Create a Function which convert NoteValue to NoteName


print("noteValues['C#']",getNoteValue('C#'))
ns='D#'
print("noteValues['"+ns+"']",getNoteValue(ns))
print("\n\n")

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

# parse Stream structure of musicfile 
#for thing in myScore:
#    print(thing)

# Alternative
#myScore.show('text')      

# https://web.mit.edu/music21/doc/usersGuide/usersGuide_06_stream2.html
for e in myScore.recurse():
    #print(e)
    print(e.offset, e, e.activeSite)
print("\n\n")


print("ToDo:")
print("Use code below to prepare Notes for AI Neuralnetwork")
print("Create vectors (<measure 1>, <offset 1>, <notevalue 1>), (<measure 2>, <offset 2>, <notevalue 2>) .. (<measure i>, <offset i>, <notevalue i>) to feed to neuralnetwork")
# https://web.mit.edu/music21/doc/usersGuide/usersGuide_06_stream2.html
# get the notes
for e in myScore.recurse().notes:
    #print(e)
    print(e.offset,e.name, e.octave, e.fullName, e.activeSite, "notevalue:", getNoteValue(e.name))
    #print(e.fullName)

    # ToDo
    # To prepare for AI convert NoteName to numeric Value with function getNoteValue

print("\n\n")
for e2 in myScore2.recurse().notes:
    #print(e)
    print(e2.offset,e2.name, e2.octave, e2.fullName, e2.activeSite, "notevalue:", getNoteValue(e2.name))
    #print(e.fullName)


print("\n\n")
for e3 in myScore3.recurse().notes:
    #print(e)
    print(e3.offset, e3.name, e3.octave, e3.fullName, e3.activeSite, "notevalue:", getNoteValue(e3.name))
    #print(e.fullName)
#ToDo plot the  data to viualize the data
    
    
# load sheetmusic in musescore
#myScore.show()  
