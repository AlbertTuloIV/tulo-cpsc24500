from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self) -> float:
        raise NotImplementedError
    
    @abstractmethod
    def perimeter(self) -> float:
        raise NotImplementedError
    
    @abstractmethod
    def describe(self) -> str:
        raise NotImplementedError