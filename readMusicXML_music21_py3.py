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
myScore.show()  