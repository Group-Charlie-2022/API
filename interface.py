from abc import ABC, abstractmethod

class Rountine(ABC):

    @abstractmethod
    def process(self, inp: str, history) -> str:
        return NotImplemented
