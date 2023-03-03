import numpy as np
import math

class SNN_class():
    def __init__(self, NT, numIn, numOut):
        self.vr = -60
        self.vPeak = 30
        self.dt = 1

        self.a, self.b, self.c, self.d = 0.02, 0.2, -65, 8
        self.aCN, self.bCN, self.cCN, self.dCN = 0.1, 0.2, -65, 6

        self.NT = NT
        self.numIn = numIn
        self.numOut = numOut

        self.tau1 = 10
        self.tau2 = 100

        self.gEx = 1
        self.gInhibit = -1

        print('Spiking Neural Network initialized!')
        print('# of input neurons: ', self.numIn)
        print('# of output neurons: ', self.numOut)

    def initilizationWeights(self, weightIn, weightOut):
        weight = abs(0.4+math.sqrt(2/weightIn) *
                     np.random.randn(self.numIn, self.numOut))
        weightInhit = 4*~np.eye(weightOut)
