class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        

        # Method:: Recursion
        cache = {}
        def getFib(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            
            if n in cache:
                return cache[n]
            
            cache_n = getFib(n-1) + getFib(n-2)
            cache[n] = cache_n
            return cache_n

        return getFib(N)
        
