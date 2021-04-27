# file: 10_8.py
# doc: https://www.analyticsvidhya.com/blog/2020/01/how-to-perform-automatic-music-generation/

# Model Building
#
# I have defined 2 architectures here – WaveNet and LSTM.
# Please experiment with both the architectures to understand the importance of WaveNet architecture.

def WaveNet(): 
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
 