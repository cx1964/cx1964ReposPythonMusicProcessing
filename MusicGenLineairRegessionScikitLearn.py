# File: MusicGenLineairRegessionScikitLearn.py
# Function: First experiment to generate notes based on Lineair Regession estimates
#           based on a musicxml input file. To use Lineair Regession
#           python Scikit-learn module is used.
#           Music data is processed with music21 python module
# Documentation: For multi variant regresion see https://realpython.com/linear-regression-in-python/

# standard modules
import music21 as m
import numpy as np
# project specific own modules
import noteconversion as nc

musescoreProg='MuseScore-3.6.2.548021370-x86_64_461d9f78f967c0640433c95ccb200785.AppImage'
scorePath = "/home/claude/Documents/sources/python/python3/cx1964ReposPythonMusicProcessing"
# Export de MuseScore File in musicxml (uncompressed music xml format musicxml extention)
museScoreFile3 = "C_major_scale_ascending_mixed_duration.musicxml" # in musicxml uncompressed

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

myScore3 = m.converter.parse(scorePath+'/'+museScoreFile3, format='musicxml')


time_list = []
note_property_list=[]

# parse Stream structure of musicfile 
#for thing in myScore:
#    print(thing)

# Alternative
#myScore.show('text')  

# https://web.mit.edu/music21/doc/usersGuide/usersGuide_06_stream2.html


for e3 in myScore3.recurse().notes:
    # Encoding X
    # Fill time
    time_list.append(e3.measureNumber)      
    time_list.append(e3.offset) 
    #print("Time_list iter:", time_list)

    # Encoding Y 
    # Fill note properties
    note_property_list.append(nc.getNoteValue(e3.name))
    note_property_list.append(e3.octave)
    note_property_list.append(e3.duration.quarterLength)
    #print("Note_property_list iter:", note_property_list)

# Create 2 dimensional array for the time list with 2 elements per row
# First index -1 creates dynamically an amount off rows based on the size of the time list
X = np.array(time_list).reshape(-1, 2)
print("X.shape",X.shape)
print(X)

# Create 2 dimension array for the note property list with 3 elements per row
# First index -1 creates dynamically an amount off rows based on the size of the note list
Y = np.array(note_property_list).reshape(-1, 3)
print("Y.shape",Y.shape)
print(Y)

# Step 1: Import packages and classes
import numpy as np
from sklearn.linear_model import LinearRegression

# The fundamental data type of NumPy is the array type called numpy.ndarray.
# The rest of this article uses the term array to refer to instances of the
# type numpy.ndarray.
# The class sklearn.linear_model.LinearRegression will be used to perform
# linear and polynomial regression and make predictions accordingly.

# Step 2: Provide data
# for X and Y  see above


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
print('Predicted response in numeric values:', Y_pred, sep='\n')

print("\n\n")
print("Estimated output in notes (Notename, octave and quarterLength):")
for r in Y_pred:

    # toDo round to a 0.25 resolution because input used 1/4 notes
    t=r[2]
    base=0.25
    v=t + (base - t) % base 
    print(nc.getNoteName(int(round(r[0])), enharmonic=False),int(round(r[1])), v)


# Round for 1/4 notes to 0.25
#t=0.5064102564102564
#b=0.25
#t + (5 - t) % b
#print(t, t + (b - t) % b) 
#
#t=1.7064102564102564
#b=0.25
#t + (5 - t) % b
#print(t, t + (b - t) % b)  
#
#t=1.7664102564102564
#b=0.25
#t + (5 - t) % b
#print(t, t + (b - t) % b) 




# Constants
# timeSignature='4/4'
# keySignature=m.key.Key('F') #  lowercase = c minor. uppercase = C major

# Build the estimated Score
# estimatedScore= m.stream.Stream()

# set KeySignature
# estimatedScore.append(keySignature)
# set the clef
# tc=m.clef.TrebleClef()
# estimatedScore.append(tc)



# Constants
timeSignatureString='4/4'
keySignature=m.key.Key('F') #  lowercase = c minor. uppercase = C major
timeSignature=m.meter.TimeSignature(timeSignatureString)
upperStaffClef=m.clef.TrebleClef()
lowerStaffClef=m.clef.BassClef()

myScore = m.stream.Stream()


# set TimeSignature
#myScore.append(m.meter.TimeSignature(timeSignature))

myPart = m.stream.Part()
myPart_UpperStaff = m.stream.Part()
myPart_UpperStaff.append(upperStaffClef)
myPart_UpperStaff.append(timeSignature)
myPart_UpperStaff.append(keySignature)

myPart_LowerStaff = m.stream.Part()
myPart_LowerStaff.append(lowerStaffClef)
myPart_LowerStaff.append(timeSignature)
myPart_LowerStaff.append(keySignature)

myMeasure = m.stream.Measure()
myNote = m.note.Note()

myPart_UpperStaff.partName="Piano Upper"
myPart_LowerStaff.partName="Piano Lower"

# Begin build measure 1
myMeasure=m.stream.Measure(number=1)
myNote=m.note.Note(name="C", quarterLength=1, octave=4)
myMeasure.insert(0, myNote)

myNote=m.note.Note(name="C#", quarterLength=1, octave=4)
myMeasure.insert(1, myNote)

myNote=m.note.Note(name="D", quarterLength=1, octave=4)
myMeasure.insert(2, myNote)

myNote=m.note.Note(name="D#", quarterLength=1, octave=4)
myMeasure.insert(3, myNote)

myPart_UpperStaff.insert(1,myMeasure)
# End  build measure 1


myScore.insert(1, myPart_UpperStaff)
myScore.insert(2, myPart_LowerStaff)
myScore.show()


# Debug info
print("OK?")
print(X)
print("\n\n")


print("\n\n")
print("process measures")
itrNote = m.note.Note()
if (X_new.shape[0] == Y_pred.shape[0]):
  # Normal Score
  cnt=0 # counter to sync X and Y (sync time and Notes)
  curMeasure=1
  for e in X_new:

    # Decoding Y_pred: get note properies  
    # Do the encoding as inverse of the decoding (see above) 
    note_properties = Y_pred[cnt]
    print("!!! note_properties[", cnt, "]", note_properties)
    curNoteName=nc.getNoteName(int(round(note_properties[0])), enharmonic=False)
    print("curNoteName", curNoteName)
    curNoteOctave =  int(round(note_properties[1]))
    print("curNoteOctave", curNoteOctave)

    # Process quarterDuration
    # round to factors of 0.25     
    t=note_properties[2]
    base=0.25
    print("process quarterDuration:", t, t + (base - t) % base)  
    curNotequarterDuration = t + (base - t) % base 
    
    # Because timeSignature is set, no measure change detection is needed, just add notes. 
    # This is not true. ToDo: set TimeSignature

    itrNote.name = curNoteName
    itrNote.octave = curNoteOctave
    itrNote.duration.quarterLength = curNotequarterDuration # ToDo change value based on note_properties[2])
    

    itrMeasure=int(e[0])
    print("itrMeasure:", itrMeasure)
    # Try to detect when a measure changes 
    if curMeasure != itrMeasure:
      # Measuer is changed  
      print("\nNew measure", itrMeasure)
      curMeasure=itrMeasure
      print(e)
    else:
      # Measure is not changed  
      print("Existing measure", itrMeasure)
      print(e)

    cnt=cnt+1
    print("cnt:", cnt)  
else:
  # Unbalanced Score
  print("Program error: Score not balanced")  

# debug: Check all element e processed  ok => X_new.shape[0] = cnt
# #print("X_new.shape[0]", X_new.shape[0], "cnt:", cnt)


#estimatedScore.show() 
