"""
This file contains all the non deep learning models
"""
import pickle
import sys

import numpy
from sklearn.neural_network import MLPClassifier

from . import Model


class MLModel(Model):
    """
    This class is parent class for all Non Deep learning models
    """

    def __init__(self, **params):
        super(MLModel, self).__init__(**params)

  

    def train(self, x_train, y_train, x_val=None, y_val=None):
        self.model.fit(x_train, y_train)
        self.trained = True
        if self.save_path:
            self.save_model()

    def predict_one(self, sample):
        if not self.trained:
            sys.stderr.write(
                "Model should be trained or loaded before doing predict\n")
            sys.exit(-1)
        return self.model.predict(numpy.array([sample]))





class NN(MLModel):
    """
    NN implements use of Neural networks for speech emotion recognition
    """

    def __init__(self, **params):
        params['name'] = 'Neural Network'
        super(NN, self).__init__(**params)
        self.model = MLPClassifier(activation='logistic', verbose=False,
                                   hidden_layer_sizes=(512,), batch_size=32)
