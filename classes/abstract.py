from abc import ABC, abstractmethod


class Engine(ABC):
    """
    абстрактный класс
    """
    @abstractmethod
    def get_request(self):
        pass

    @abstractmethod
    def get_offers(self):
        pass