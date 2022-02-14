from abc import ABC, abstractmethod

class Routine(ABC):

    @staticmethod
    @abstractmethod
    def process(self, inp: str, history) -> str:
        return NotImplemented
