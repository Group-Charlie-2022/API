from abc import ABC, abstractmethod

class Rountine(ABC):

    @abstractmethod
    def process(self, input: str) -> str:
        return NotImplemented
