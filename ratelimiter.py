from strategy import RatelimitStrategy
class RateLimit:

    def __init__(self,strategy:RatelimitStrategy):

        self._stategy = strategy

    def allow(self,user,now):
        return self._stategy.allow(user,now)