from abc import ABC, abstractmethod
from collections.abc import Sequence

class Routine(ABC):
    '''
    Interface for question handling routines
    '''

    @staticmethod
    @abstractmethod
    def process(inp: str, history: Sequence[tuple[str, str]]) -> str:
        '''
        inputs:
            inp: question asked by the user
            history: list of pairs (question, answer) exchanged with this user

        output:
            answer ready to give to the user
        '''
        return NotImplemented
