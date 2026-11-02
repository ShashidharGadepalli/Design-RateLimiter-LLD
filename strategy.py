from abc import ABC,abstractmethod

class RatelimitStrategy(ABC):

    @abstractmethod
    def allow(self,user,now):
        pass