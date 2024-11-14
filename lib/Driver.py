from abc import abstractmethod

class Driver:
    @abstractmethod
    def listen(self, firefly):
        pass

    @abstractmethod
    def send(self, firefly):
        pass