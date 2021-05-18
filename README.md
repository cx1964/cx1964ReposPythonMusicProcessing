# cx1964ReposPythonMusicProcessing

ToDo 

ToDo1:
        MusicGenLineairRegessionScikitLearn.py als deze source wordt omgebouwd tbv het gebruik van LSTM,
        dan:
        - de tijd (Maatnummer en offset binnen maat) mbv encoding om bouwen tot een getal
        - beschouw de nootwaarden (nootnaam dwz nootnummer, octaafwaarde en quarterlenth waarde) als aparte features
        - checken of X (=de encode tijd) dan evenveel  waarden heeft als de Y
        - input van LSTM moet altijd een 3 dimensional shape zijn met [batch_size, timesteps, aantal features]
        - aantal_featuers wordt 3
        - Zie hoofdstuk 5.2 van "Long Short-Term Memory Networks With Python" om te bepalen welke LSTM men het
          beste kan gebruiken
        - timesteps wordt lengte van het stuk, dwz het aantal elementen in X 

ToDo1: 
fuse estimatedPart0 and estimatedPart1 to estimatedScore
rebuild create_estimated_score
see code below

ToDo2:
Refactor0
Apply standard python naming conventions:
- all capitals for constants
- no Cammel case or Pascal case bu use underscores for compound concepts


ToDo3
Create a copy of this source and use a polynomial regression (Nonlinear regression) in stead of a linear regression.
https://towardsdatascience.com/machine-learning-with-python-easy-and-robust-method-to-fit-nonlinear-data-19e8a1ddbd49
