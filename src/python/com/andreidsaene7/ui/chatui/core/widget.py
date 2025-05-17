from abc import ABC, abstractmethod

class Widget(ABC):
    @abstractmethod
    def build(self, master): pass

