# File: MusicGenLineairRegessionScikitLearn.py
# Function: First experiment to generate notes based on Lineair Regession estimates
#           based on a musicxml input file. To use Lineair Regession
#           python Scikit-learn module is used.
#           Music data is processed with music21 python module
# Documentation: For multi variant regresion see https://realpython.com/linear-regression-in-python/
#
# Opmerking: Letop
#            Tbv ombouwen van deze source naar een versie die gebruik maakt van LSTM
#            ipv een Lineair Regession moet men 
#            niet de X shape van de LTSM gaan vullen met de tijd. Dit is een denk fout. 
#            Men kan muziek genereren namelijk opvatten als een autocorrelation probleem. 
#            Waarbij de correlatie binnen het gegeven zelf ligt en aparte relatie is
#            tussen het gegeven aan de ene kant en de tijd aan de ander kant. Het is dus niet dat x=tijd en y=het gegeven.
#            Voor de uitleg van het gebruik van time series met autocorrelatie en LSTMS zie de Youtub video
#            "166 - An introduction to time series forecasting - Part 5 Using LSTM"
#            https://www.youtube.com/watch?v=97bZKO6cJfg
#            In deze video wordt gebruik gemaakt van eenvoorbeeld op passasiersgegevens. 
#            Dit gegeven bevat bavt ook een autocorrelatie. De passagiersaantallen flucteren door de tijd. 
#            Voor de  X input shape van de LSTM wordt een sequence gebruik van passaiers aantallen 
#            binnen een bepaald interval (tijdsinterval ti - ti+n-1). Voor de Y input shape wordt 
#            gebruik gemaakt van een passagiers aantal op tijdstip ti+n. De X input shape bevat dus niet de tijd!.
#            Als men muziekgeneren ook als time series probleem obv autocorrelatie beschouwd dan
#            dan moet men de X shape van de LSTM NIET vullen met de tijd (maatgetal en offest binnen de maat),
#            maar wordt de X shape gevuld worden met een sequence van noot informatie (voor een bepaald tijdsinterval ti - ti+n-1)
#            en bevat de Y shape   noot informatie op tijdstip ti+n.
#
#
# Naming conventions: https://visualgit.readthedocs.io/en/latest/pages/naming_convention.html
# cx1964 20210411


#ToDo
# zie de ToDos in README.md

# standard modules
import numpy as np
from sklearn.linear_model import LinearRegression

import music21 as m
# project specific own modules
import noteconversion as nc
import my_utilities as mu


# Constants
# Status Naming conventions Constants: 
# BASE = 0.25 # round Note durations to multiples of base factors. Round 1/4 notes to base=0.25 and 1/8 notes to base=0.125 0.0625, 0,03125 etc
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
#old:   X, Y, time_signature_input_file, key_signature_input_file, smallest_quarter_duration = mu.import_musicxml_file(SCOREPATH, MUSESCOREFILE)
music_info_dict = mu.import_musicxml_file_idea(SCOREPATH, MUSESCOREFILE)
# for e in music_info_dict.keys():
#    print("main prog: e", e)
# get info from dict music_info_dict
time_signature0 = music_info_dict['time_signature0']
key_signature0 = music_info_dict['key_signature0']
smallest_quarterlength0 = music_info_dict['smallest_quarterlength0']
X0 = music_info_dict['X0']
Y0 = music_info_dict['Y0']
time_signature1 = music_info_dict['time_signature1']
key_signature1 = music_info_dict['key_signature1']
smallest_quarterlength1 = music_info_dict['smallest_quarterlength1']
X1 = music_info_dict['X1']
Y1 = music_info_dict['Y1']


#ToDo Change code below:
# 
# X, Y, time_signature_input_file, key_signature_input_file, smallest_quarter_duration = ????


#print("smallest_quarter_duration:", smallest_quarter_duration)

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
model0 = mdl.fit(X0, Y0)
model1 = mdl.fit(X1, Y1)

# Step 4: Get results
r_sq0 = model0.score(X0, Y0)
r_sq1 = model1.score(X1, Y1)
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
new_model0 = LinearRegression().fit(X0, Y0)
new_model1 = LinearRegression().fit(X1, Y1)

# Step 5: Predict response
# Once there is a satisfactory model, you can use it for predictions with either existing or new data.

# To obtain the predicted response, use .predict():
print("\n\n")
print("Tempory solution voor X_new")
X_new0 = X0 # ToDo: create better way to fill X_new0
X_new1 = X1 # ToDo: create better way to fill X_new1
Y_pred0 = model0.predict(X_new0)
Y_pred1 = model1.predict(X_new1)
print('\n\nPredicted response in numeric values Y_pred0:', Y_pred0, sep='\n')
print('\n\nPredicted response in numeric values Y_pred1:', Y_pred1, sep='\n')

estimatedPart0 = mu.create_estimated_score(  X_new0
                                            ,Y_pred0
                                            ,smallest_quarterlength0
                                            ,time_signature0
                                            ,key_signature0
                                            ,SCORE_TITLE
                                            ,COMPOSER
                                          )

estimatedPart1 = mu.create_estimated_score(  X_new1
                                            ,Y_pred1
                                            ,smallest_quarterlength1
                                            ,time_signature1
                                            ,key_signature1
                                            ,SCORE_TITLE
                                            ,COMPOSER
                                          )

# ToDo: 
# fuse estimatedPart0 and estimatedPart1 to estimatedScore
# rebuild create_estimated_score

#estimatedPart0.show('text')
estimatedPart0.show()
#estimatedPart1.show()

#estimatedScore.show() 
#estimatedScore.show('text') 

# parse Stream structure of musicfile 
# for thing in myScore:
#     print(thing)
