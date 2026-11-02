from strategy import RatelimitStrategy

class SldingWindow(RatelimitStrategy):

    def __init__(self,limit,window):

        self._limit = limit
        self._window = window
        self._times = {}

        '''self._slots= {}
        self._count ={}'''

    def allow(self, user, now):
        times = self._times.get(user,[])
        recent = []
        for t in times:
            if now - t< self._window:
                recent.append(t)

        if len(recent)<self._limit:
            recent.append(now)
            self._times[user]=recent
            return True
        self._times[user]=recent
        return False

'''    def allow2(self,user,now):
        slot = now//self._window
        if self._slots[user]!=slot:
            self._slots[user]=slot
            self._count[user] = 0

        if self._count[user]<self._limit:
            self._count[user]+=1
            return True
        return False'''