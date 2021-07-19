from tensorflow.keras import layers
from tensorflow.keras import models
from tensorflow.keras import optimizers


def makeModel() :
    model = models.Sequential()
    model.add(layers.#TODO  (32,  #TODO   , activation='relu',
                            #TODO  =(150, 150, 3)))
    model.add(layers.#TODO  ((2, 2)))
    model.add(layers.#TODO  (64, (3, 3), activation='relu'))
    model.add(layers.#TODO  ((2, 2)))
    model.add(layers.#TODO  (128, (3, 3), activation='relu'))
    model.add(layers.##TODO    ((2, 2)))
    model.add(layers.Conv2D(128, (3, 3), activation='relu'))
    model.add(layers.#TODO  ((2, 2)))
    model.add(layers.#TODO  ())
    model.add(layers.#TODO  (512, activation='relu'))
    model.add(layers.Dense(1, #TODO  ='sigmoid'))
    #print ( model.summary() )

    model.compile(loss='binary_crossentropy',
                  optimizer=optimizers.RMSprop(lr=1e-4),
                  metrics=['acc'])
    return model

