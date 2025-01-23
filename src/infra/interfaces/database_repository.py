from abc import ABC, abstractmethod
from typing import Dict

class DatabaseRepositoryInterface(ABC):

    @classmethod
    @abstractmethod
    def insert_artist(cls, data: Dict) -> None:
        pass
