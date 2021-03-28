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
myPart = m.stream.PartStaff()
myMeasure = m.stream.Measure()
myNote = m.note.Note()

myPart.partName="Piano"


myMeasure.number=1
myMeasure.append(m.note.Note(name="C" , quarterLength=1, octave=2))
myMeasure.append(m.note.Note(name="C#", quarterLength=1, octave=2))
myMeasure.append(m.note.Note(name="D" , quarterLength=1, octave=2))
myMeasure.append(m.note.Note(name="D#", quarterLength=1, octave=2))
myPart.append(myMeasure)


# Begin
# ToDo: create new method to Add Measure to Part.add
# if I used new instance of m.stream.Measure() it would work like measure2
# yoy can only once append a specific variable
'''
myMeasure.number=2
myMeasure.append(m.note.Note(name="E", quarterLength=1))
myMeasure.append(m.note.Note(name="F", quarterLength=1))
myMeasure.append(m.note.Note(name="F#", quarterLength=1))
myMeasure.append(m.note.Note(name="G" , quarterLength=1))
#myPart.append(myMeasure)
'''
# End
myPart.append(m.stream.Measure(number=2))


myScore.append(myPart)


print("\n\nmyScore")
myScore.show('text')  

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
