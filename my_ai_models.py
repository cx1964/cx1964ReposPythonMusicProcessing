# file: my_ai_models.py
# function: neural net model definitions

# Model Building
#
# I have defined architectures here – GRU, WaveNet and LSTM 
# Please experiment with both the architectures to understand the importance of WaveNet architecture.

from keras.layers import *
from keras.models import *
from keras.callbacks import *
import keras.backend as K

def gru(units):
    """ GRU(Gated Recurrent Unit)
    Build GRU Model.

    # Arguments
        units: List(int), number of input, output and hidden units.
    # Returns
        model: Model, nn model.
    """

    # Doc: https://www.programcreek.com/python/example/97114/keras.layers.recurrent.GRU
    model = Sequential()
    model.add(GRU(units[1], input_shape=(units[0], 1), return_sequences=True))
    model.add(GRU(units[2]))
    model.add(Dropout(0.2))
    model.add(Dense(units[3], activation='sigmoid'))
    return (model)





def lstm():
  # LSTM architecture 
  # 
  # source from lstm.py
  # 
  """ lstm(long short time model)
  Build lstm Model.

  # Arguments
    none
  # Returns
    model: Model, nn model.
  """ 
    
  model = Sequential()
  model.add(LSTM(128,return_sequences=True))
  model.add(LSTM(128))
  model.add(Dense(256))
  model.add(Activation('relu'))
                              # problem: model.add(Dense(n_vocab))
  model.add(Dense(n_vocab))   # ????? what is its function????
                              # use same construct as in WaveNet() in 10_8.py
                              # model.add(Dense(unique_y)) dit not help !!!
  model.add(Activation('softmax'))
  model.compile(loss='sparse_categorical_crossentropy', optimizer='adam')
  return (model)


# source from 10_8.py
def WaveNet(): 
  """ GRU(Gated Recurrent Unit)
  Build WateNet Model.

  # Arguments
    none
  # Returns
    model: Model, neural net WaveNet model.
  """     
  model = Sequential()
      
  #embedding layer
  model.add(Embedding(len(unique_x), 100, input_length=32,trainable=True)) 
  
  model.add(Conv1D(64,3, padding='causal',activation='relu'))
  model.add(Dropout(0.2))
  model.add(MaxPool1D(2))
      
  model.add(Conv1D(128,3,activation='relu',dilation_rate=2,padding='causal'))
  model.add(Dropout(0.2))
  model.add(MaxPool1D(2))
  
  model.add(Conv1D(256,3,activation='relu',dilation_rate=4,padding='causal'))
  model.add(Dropout(0.2))
  model.add(MaxPool1D(2))
            
  #model.add(Conv1D(256,5,activation='relu'))    
  model.add(GlobalMaxPool1D())
      
  model.add(Dense(256, activation='relu'))
  model.add(Dense(len(unique_y), activation='softmax'))
      
  model.compile(loss='sparse_categorical_crossentropy', optimizer='adam')
  return (model)   