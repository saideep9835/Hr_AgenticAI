from abc import ABC, abstractmethod

class BaseMemory(ABC):
    @abstractmethod
    def get(self, key: str):
        pass

    @abstractmethod
    def put(self, key: str, value):
        pass

    @abstractmethod
    def clear(self):
        pass