from strategy import RatelimitStrategy

class TokenBucket(RatelimitStrategy):

    def __init__(self,capacity,refill):
        self._capacity = capacity
        self._refill = refill
        self._tokens = {}
        self._recent = {}

    def allow(self, user, now):
        if user not in self._tokens:
            self._tokens[user] = self._capacity
            self._recent[user] = now

        duration = now - self._recent[user]
        self._tokens[user] = self._tokens[user] + duration * self._refill

        if self._tokens[user]>self._capacity:
            self._tokens[user]=self._capacity
        self._recent[user] = now

        if self._tokens[user]>=1:
            self._tokens[user]-=1
            return True
        return False