# file: tmp4.py

# File: MusicGenLineairRegessionScikitLearn.py
# Function: First experiment to generate notes based on Lineair Regession estimates
#           based on a musicxml input file. To use Lineair Regession
#           python Scikit-learn module is used.
#           Music data is processed with music21 python module
# Documentation: For multi variant regresion see https://realpython.com/linear-regression-in-python/
#
# Naming conventions: https://visualgit.readthedocs.io/en/latest/pages/naming_convention.html
# cx1964 20210411

# ToDo1: 
#  
# Use the same time signature and key signature for estimated score as used
# in input file. 

# ToDo2:
#
# Refactor0
# Apply standard python naming conventions:
# - all capitals for constants
# - no Cammel case or Pascal case bu use underscores for compound concepts
# 
# Refactor1
# Refactor this source file so
# that it gets a seperate funnction which creates a estimated score. 
# Input Params de estimated X en Y arrays with music information 

# # Refactor2
# Use key signature and time signature for estimated score from imput file. 

# ToDo3
# Create a copy of this source and use a polynomial regression (Nonlinear regression) in stead of a linear regression.
# https://towardsdatascience.com/machine-learning-with-python-easy-and-robust-method-to-fit-nonlinear-data-19e8a1ddbd49

# standard modules
from datetime import date
import numpy as np
from sklearn.linear_model import LinearRegression

import music21 as m
# project specific own modules
import noteconversion as nc
import my_uilities as mu


# Constants
# Status Naming conventions Constants: 
TIME_SIGNATURE_STRING='3/4'
KEY_SIGNATURE=m.key.Key('F') #  lowercase = c minor. uppercase = C major
BASE = 0.25 # round Note durations to multiples of base factors. Round 1/4 notes to base=0.25 and 1/8 notes to base=0.125 0.0625, 0,03125 etc
SCOREPATH = "/home/claude/Documents/sources/python/python3/cx1964ReposPythonMusicProcessing"
# Export de MuseScore File in musicxml (uncompressed music xml format musicxml extention)
MUSESCOREFILE = "C_major_scale_ascending_mixed_duration.musicxml" # in musicxml uncompressed
MUSESCOREPROG='MuseScore-3.6.2.548021370-x86_64_461d9f78f967c0640433c95ccb200785.AppImage'
MUSESCOREPROGPATH='/home/claude/Applications/'
SCORE_TITLE="python3 Machine learning Generated Sheetmusic "
COMPOSER="cx1964"

# See: https://web.mit.edu/music21/doc/usersGuide/usersGuide_24_environment.html#usersguide-24-environment
# See: https://web.mit.edu/music21/doc/usersGuide/usersGuide_24_environment.html
env = m.environment.UserSettings()
env.delete()
env.create()
# set environmment
env['autoDownload'] = 'allow'
#env['lilypondPath'] = '/usr/bin/lilypond'
#env['musescoreDirectPNGPath'] = '/usr/bin/musescore3'
env['musicxmlPath'] = MUSESCOREPROGPATH+MUSESCOREPROG


# Import musicfile in musicxml format and
# fill numpy arrays X and Y
X, Y = mu.import_musicxml_file(SCOREPATH, MUSESCOREFILE)

# The class sklearn.linear_model.LinearRegression will be used to perform
# linear and polynomial regression and make predictions accordingly.

# Step 3: Create a model and fit it
mdl = LinearRegression()
# This statement creates the variable model as the instance of LinearRegression.
# You can provide several optional parameters to LinearRegression:
#
# fit_intercept     is a Boolean (True by default) that decides whether to calculate
#                   the intercept 𝑏₀ (True) or consider it equal to zero (False).
# normalize         is a Boolean (False by default) that decides whether to normalize
#                   the input variables (True) or not (False).
# copy_X            is a Boolean (True by default) that decides whether to copy (True)
#                   or overwrite the input variables (False).
# n_jobs            is an integer or None (default) and represents the number of jobs
#                   used in parallel computation. None usually means one job and -1 to
#                    use all processors.
#
# This example uses the default values of all parameters.
#
# It’s time to start using the model. First, you need to call .fit() on model:
model = mdl.fit(X, Y)

# Step 4: Get results
r_sq = model.score(X, Y)
# print('coefficient of determination:', r_sq)
# coefficient of determination: ???

# Unneeded code voor music gen
# When you’re applying .score(), the arguments are also the predictor x and regressor y, and the return value is 𝑅².
#
# The attributes of model are .intercept_, which represents the coefficient, 𝑏₀ and .coef_, which represents 𝑏₁:
# print('intercept:', model.intercept_)
# intercept: 5.633333333333329
# print('slope:', model.coef_)
# slope: [0.54]

# The code above illustrates how to get 𝑏₀ and 𝑏₁. 
# You can notice that .intercept_ is a scalar, while .coef_ is an array.

# The value 𝑏₀ = 5.63 (approximately) illustrates that your model predicts the response 5.63 when 𝑥 is zero.
# The value 𝑏₁ = 0.54 means that the predicted response rises by 0.54 when 𝑥 is increased by one.

# You should notice that you can provide y as a two-dimensional array as well.
# In this case, you’ll get a similar result. This is how it might look:
new_model = LinearRegression().fit(X, Y)

# Step 5: Predict response
# Once there is a satisfactory model, you can use it for predictions with either existing or new data.

# To obtain the predicted response, use .predict():
print("\n\n")
print("Tempory solution voor X_new")
X_new = X # ToDo: create better way to fill X_new
Y_pred = model.predict(X_new)
print('\n\nPredicted response in numeric values Y_pred:', Y_pred, sep='\n')

print("\n\n")
print("Estimated output in notes (Notename, octave and quarterLength):")
for r in Y_pred:

    # toDo round to a 0.25 resolution because input used 1/4 notes
    t=r[2]
    BASE=0.25
    v=t + (BASE - t) % BASE
    print(nc.getNoteName(int(round(r[0])), enharmonic=False),int(round(r[1])), v)


# *** Create the score with estimated notes ***
# *********************************************
# https://web.mit.edu/music21/doc/usersGuide/usersGuide_06_stream2.html
estimatedScore = m.stream.Stream()

# Set Meta Data in estimated score
meta_data = m.metadata.Metadata()
meta_data.title = SCORE_TITLE
today = date.today()
# YYYY/mm/dd
d1 = today.strftime("%d/%m/%Y")
meta_data.date = str(d1)
meta_data.composer = COMPOSER+" ("+str(d1)+")"

timeSignature=m.meter.TimeSignature(TIME_SIGNATURE_STRING)
upperStaffClef=m.clef.TrebleClef()
lowerStaffClef=m.clef.BassClef()

myPart = m.stream.Part()
myPart_UpperStaff = m.stream.Part()
# set Clef UpperStaff
myPart_UpperStaff.append(upperStaffClef)
# set TimeSignature UpperStaff
myPart_UpperStaff.append(timeSignature)
# set keySignature UpperStaff
myPart_UpperStaff.append(KEY_SIGNATURE)

myPart_LowerStaff = m.stream.Part()
# set Clef UpperStaff
myPart_LowerStaff.append(lowerStaffClef)
# set TimeSignature LowerStaff
myPart_LowerStaff.append(timeSignature)
# set keySignature LowerStaff
myPart_LowerStaff.append(KEY_SIGNATURE)

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
    curNotequarterDuration = mu.roundTo(note_properties[2], BASE)

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
estimatedScore.insert(2, myPart_LowerStaff)



estimatedScore.show() 
# estimatedScore.show('text') 

# parse Stream structure of musicfile 
# for thing in myScore:
#     print(thing)
   
