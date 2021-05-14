class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        print(N,K)
        def swap(char):
            if char == '0':
                return '1'
            else:
                return '0'

        if N == 1:
            return '0'
        else:
            if K <= 2**(N-2):
                return Solution().kthGrammar(N-1, K)
            else:
                return swap(Solution().kthGrammar(N-1, K - 2**(N-2)))
