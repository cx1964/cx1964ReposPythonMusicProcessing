# File: createSheetMusicmusic21_py3.py
# Function: Sample how to create sheetmusic in python code
#           with music21
# 

import music21 as m

musescoreProg='MuseScore-3.6.2.548021370-x86_64_461d9f78f967c0640433c95ccb200785.AppImage'
scorePath = "/home/claude/Documents/sources/python/python3/cx1964ReposPythonMusicProcessing"
# Export de MuseScore File in musicxml (uncompressed music xml format musicxml extention)
museScoreFile = "C_major_scale_ascending_mixed_duration.musicxml" # in musicxml uncompressed

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

readScore = m.converter.parse(scorePath+'/'+museScoreFile, format='musicxml')
#print("type(myScore):", type(myScore))



time_list = []
note_property_list=[]

# parse Stream structure of musicfile 
#for thing in myScore:
#    print(thing)

# Alternative
readScore.show('text')  

# https://web.mit.edu/music21/doc/usersGuide/usersGuide_06_stream2.html
# https://web.mit.edu/music21/doc/usersGuide/usersGuide_06_stream2.html


myScore = m.stream.Stream()
myPart = m.stream.Part()
myMeasure = m.stream.Measure()
myNote = m.note.Note()

myPart.partName="Piano"

# Begin build measure 1
myMeasure=m.stream.Measure(number=1)
myNote=m.note.Note(name="C", quarterLength=1, octave=4)
myMeasure.insert(0, myNote)

myNote=m.note.Note(name="C#", quarterLength=1, octave=4)
myMeasure.insert(1, myNote)

myNote=m.note.Note(name="D", quarterLength=1, octave=4)
myMeasure.insert(2, myNote)

# add a Chord
myChord=m.chord.Chord(["C", "F#","A"])
myMeasure.insert(3, myChord)

myPart.insert(1,myMeasure)
# End  build measure 1


# Begin build measure 2
myMeasure=m.stream.Measure(number=2)
myNote=m.note.Note(name="E", quarterLength=1, octave=4)
myMeasure.insert(0, myNote)

myNote=m.note.Note(name="F", quarterLength=1, octave=4)
myMeasure.insert(1, myNote)

myNote=m.note.Note(name="F#", quarterLength=1, octave=4)
myMeasure.insert(2, myNote)

myNote=m.note.Note(name="G", quarterLength=1, octave=4)
myMeasure.insert(3, myNote)

myPart.insert(2,myMeasure)
# End  build measure 2


# Begin build measure 3
myMeasure=m.stream.Measure(number=3)
myNote=m.note.Note(name="A", quarterLength=1, octave=4)
myMeasure.insert(0, myNote)

myNote=m.note.Note(name="A#", quarterLength=1, octave=4)
myMeasure.insert(1, myNote)

myNote=m.note.Note(name="B", quarterLength=1, octave=4)
myMeasure.insert(2, myNote)

myNote=m.note.Note(name="C", quarterLength=1, octave=5)
myMeasure.insert(3, myNote)

myPart.insert(3,myMeasure)
# End  build measure 3


myScore.insert(0, myPart)


print("\n\nmyScore")
# debug  myScore.show('text')  

# Show Score in Music Notation program
myScore.show()

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
'''
