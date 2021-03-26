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
museScoreFile  = "C_major_scale_ascending.musicxml" # in musicxml uncompressed
museScoreFile2 = "F_major_scale_ascending_8th_notes.musicxml" # in musicxml uncompressed
museScoreFile3 = "C_major_scale_ascending_mixed_duration.musicxml" # in musicxml uncompressed
keyC    = m.key.Key('C') #  lowercase = c minor. uppercase = C major
keyCmin = m.key.Key('c') #  lowercase = c minor. uppercase = C major




# Test conversion Note to noteValue
# print("noteValues['C#']",nc.getNoteValue('C#'))
# print("noteValues['c#']",nc.getNoteValue('c#'))
#ns='d#'
#print("noteValues['"+ns+"']",nc.getNoteValue(ns))
#print("\n\n")
# Test conversion noteValue to Note
for v in range(0,12,1):
  n=nc.getNoteName(v, enharmonic=False)
  print(v,n)
  n=nc.getNoteName(v, enharmonic=True)
  print(v,n)


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



time_list = []
note_property_list=[]

# parse Stream structure of musicfile 
#for thing in myScore:
#    print(thing)

# Alternative
#myScore.show('text')  

# https://web.mit.edu/music21/doc/usersGuide/usersGuide_06_stream2.html
'''
for e in myScore.recurse():
    #print(e)
    print(e.offset, e, e.activeSite)
print("\n\n")
'''

# https://web.mit.edu/music21/doc/usersGuide/usersGuide_06_stream2.html
'''
# get the notes
for e in myScore.recurse().notes:
    #print(e)
    print(e.offset,e.name, e.octave, e.fullName, e.activeSite, "notevalue:", getNoteValue(e.name))
    #print(e.fullName)

    # ToDo
    # To prepare for AI convert NoteName to numeric Value with function getNoteValue
'''

'''
print("\n\n")
for e2 in myScore2.recurse().notes:
    #print(e2)
    print(e2.offset,e2.name, e2.octave, e2.fullName, e2.activeSite, "Notevalue:", getNoteValue(e2.name))
    #print(e.fullName)
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
    
# load sheetmusic in musescore
#myScore.show()  


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
m = LinearRegression()
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
model = m.fit(X, Y)

# Step 4: Get results
r_sq = model.score(X, Y)
print('coefficient of determination:', r_sq)
# coefficient of determination: ???

# When you’re applying .score(), the arguments are also the predictor x and regressor y, and the return value is 𝑅².
#
# The attributes of model are .intercept_, which represents the coefficient, 𝑏₀ and .coef_, which represents 𝑏₁:
print('intercept:', model.intercept_)
# intercept: 5.633333333333329
print('slope:', model.coef_)
# slope: [0.54]

# The code above illustrates how to get 𝑏₀ and 𝑏₁. 
# You can notice that .intercept_ is a scalar, while .coef_ is an array.

# The value 𝑏₀ = 5.63 (approximately) illustrates that your model predicts the response 5.63 when 𝑥 is zero.
# The value 𝑏₁ = 0.54 means that the predicted response rises by 0.54 when 𝑥 is increased by one.

# You should notice that you can provide y as a two-dimensional array as well.
# In this case, you’ll get a similar result. This is how it might look:
new_model = LinearRegression().fit(X, Y)
print('intercept:', new_model.intercept_)
# intercept: 
print('slope:', new_model.coef_)
# slope: 


# Step 5: Predict response
# Once there is a satisfactory model, you can use it for predictions with either existing or new data.

# To obtain the predicted response, use .predict():
y_pred = model.predict(X)
print('predicted response in numeric values:', y_pred, sep='\n')

print("\n\n")
print("Estimated output in notes (Notename, octave and quarterLength):")
for r in y_pred:
    #print(r)
    # Raw data
    # print(r[0],r[1], r[2])
    # Rounded data
    # Round r[0] to whole numbers
    # Round r[1] to whole numbers
    # Round r[2] to 0.25 when 1/4 note is used
    # print(int(round(r[0])),int(round(r[1])), r[2])
 
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


# ToDo
# rebuild this code to build the score
myData=[1, 1, 1,2,1,3,1,4,2,1,2,2,2,3,2,4,3,1,3,2,3,3,3,4]
x = np.array(myData).reshape(-1,2)
print(x)
print("\n\n")
curMeasure=1
for e in x:
  itrMeasure=e[0]
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
   