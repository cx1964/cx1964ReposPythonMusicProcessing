# File: readMusicXML_music21_py3.py
# Function: Sample how to read a sheetmusic file in MusicXML format
#           with music21
# 

import music21 as m

musescoreProg='MuseScore-3.6.2.548021370-x86_64_461d9f78f967c0640433c95ccb200785.AppImage'
scorePath = "/home/claude/Documents/sources/python/python3/cx1964ReposPythonMusicProcessing"
# Export de MuseScore File in musicxml (uncompressed music xml format musicxml extention)
museScoreFile = "C_major_scale_ascending.musicxml" # in musicxml uncompressed
keyCmin = m.key.Key('C') #  lowercase = c minor. uppercase = C major

def getNoteValue(noteName):
    # Convert a NoteName in a numeric value
    noteValues = { 
                   'C' : 0, 'B#' : 0, 
                   'C#': 1, 'Db' : 1,
                   'D' : 2, 'C##': 2,
                   'D#': 3, 'Eb' : 3,
                   'E' : 4,
                   'F' : 6, 'E#' : 6,
                   'F#': 7, 'Gb' : 7,
                   'G' : 8, 'F##': 8,
                   'G#': 9, 'Ab' : 9,
                   'A' :10,
                   'A#':11, 'Bb' :11,
                   'B' :12, 'Cb' :12
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

myScore = m.converter.parse(scorePath+'/'+museScoreFile, format='musicxml')
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


# load sheetmusic in musescore
#myScore.show()  