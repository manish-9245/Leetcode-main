class Solution:
    def fib(self, n: int) -> int:
        return functools.reduce(lambda s,y: (s[0]+s[1], s[0]),range(n), (1,0))[1]