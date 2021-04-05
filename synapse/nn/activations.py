
from synapse.nn.layers import Layer
from synapse.autograd.tensor import Tensor
from synapse.autograd import TensorFunction

import numpy as np

from typing import Callable


class Tanh(TensorFunction):
    def function(self, t1: Tensor) -> Tensor:
        requiresGrad = t1.requiresGrad
        data = np.tanh(t1.data)
        resultTensor = Tensor(data, requiresGrad)
        return resultTensor

    def gradFn0(self, t1: Tensor) -> Callable[[np.ndarray, Tensor], Tensor]:

        def tanhBackward(grad: np.ndarray) -> Tensor:
            data = 1 - np.tanh(t1.data)**2
            result = grad * data

            return Tensor(result)

        return tanhBackward

class ReLU(TensorFunction):
    def function(self, t1: Tensor) -> Tensor:
        requiresGrad = t1.requiresGrad
        data = np.where(t1.data < 0, 0 , t1.data)

        resultTensor = Tensor(data, requiresGrad)
        return resultTensor

    def gradFn0(self, t1: Tensor) -> Callable[[np.ndarray, Tensor], Tensor]:

        def reluBackward(grad: np.ndarray) -> Tensor:
            data = np.where(t1.data < 0, 0, 1)
            result = grad * data
            return Tensor(result)

        return reluBackward







