from abc import ABC, abstractmethod


class Entity(ABC):
    @abstractmethod
    def scrap(self, url):
        pass

    @abstractmethod
    def parse(self, ResultSet):
        pass