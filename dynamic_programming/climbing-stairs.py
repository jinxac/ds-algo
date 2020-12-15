class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        cache = {}
        def getFib(n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            
            if n in cache:
                return cache[n]
            
            cache_n = getFib(n-1) + getFib(n-2)
            cache[n] = cache_n
            return cache_n

        return getFib(n)
        
