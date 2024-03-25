from abc import ABC, abstractmethod


class InterfaceVacuumCleaner(ABC):

    @abstractmethod
    def run(self):
        pass
