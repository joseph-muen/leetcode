class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        print(x,n)
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n < 0:
            return Solution().myPow(1/x, -n)
        else:
            if n % 2 == 0:
                return Solution().myPow(x*x, n/2)
            else:
                return x * Solution().myPow(x, n-1)
