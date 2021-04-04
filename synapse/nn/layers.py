
from synapse.autograd.tensor import Tensor
import numpy as np

class Layer:
    def __init__(self,
                 inFeatures: int ,
                 outFeatures: int,
                 useBias: bool =False,
                 name: str = "Layer" ) -> None:
        raise NotImplementedError

    def __call__(self, x: "Tensor") -> 'Tensor':
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError

    def backwards(self, grad: 'Tensor') -> 'Tensor':
        raise NotImplementedError


class Linear(Layer):
    def __init__(self,
                 inFeatures: int,
                 outFeatures: int,
                 useBias: bool =False,
                 name: str = 'Linear') -> None:

        self.useBias = useBias
        self.__inFeatures = inFeatures
        self.__outFeatures = outFeatures
        self.__name = name

        self.weights = Tensor(
            data=np.random.randn(outFeatures, inFeatures),
            requiresGrad=True)

        if useBias:

            # self.bias must handle broadcasting
            # but idk how to implement it
            self.bias = Tensor(
                np.random.randn(out_features, 1),
                requiresGrad=True)

    def __call__(self, x: 'Tensor') -> 'Tensor':
        """Forward Propagation"""

        if self.useBias:
            self.__output = self.weights @ x + self.bias
        else:
            self.__output = self.weights @ x

        # self.weights.shape == out x in
        # x.shape == in x num
        return self._output

    def __str__(self) -> str:
        return f'\n== {self.__name} == \
            \n\t- in features: {self.__inFeatures}\
            \n\t- out features: {self.__outFeatures}'

    def backwards(self, grad: 'Tensor') -> 'Tensor':
        self.__output.backwards(grad)
        return self.__output.grad




