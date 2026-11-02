from strategy import RatelimitStrategy

class FixedWindow(RatelimitStrategy):

    def __init__(self,limit,window):

        self._limit = limit
        self._window = window

        self._slots= {}
        self._count ={}

    def allow(self,user,now):
        slot = now//self._window

        if self._slots.get(user)!=slot:
            self._slots[user]=slot
            self._count[user] = 0

        if self._count[user]<self._limit:
            self._count[user]+=1
            return True
        return False