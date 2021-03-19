# File: readMusicXML_music21_py3.py
# Function: Sample how to read a sheetmusic file in MusicXML format
#           with music21
# 

import music21 as m

scorePath = "/home/claude/Documents/sources/python/python3/cx1964ReposPythonMusicProcessing"
# Export de MuseScore File in musicxml (uncompressed music mxl format)
museScoreFile = "C_major_scale_ascending.MusicXML.MusicXML" # in musicxml uncompressed
keyCmin = m.key.Key('C') #  lowercase = c minor. uppercase = C major

# Zie: https://web.mit.edu/music21/doc/usersGuide/usersGuide_24_environment.html#usersguide-24-environment
env = m.environment.UserSettings()
env.delete()
env.create()
# set environmment
env['autoDownload'] = 'allow'
env['lilypondPath'] = '/usr/bin/lilypond'
env['musescoreDirectPNGPath'] = '/usr/bin/musescore3'
env['musicxmlPath'] = '/usr/bin/musescore3'

myScore = m.converter.parse(scorePath+'/'+museScoreFile, format='musicxml')
myScore.show()  