class Solution(object):

    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        def gcd(x, y):
            while(y):
                x, y = y, x % y
            return x
        # define lcm function
        def lcm(x, y):
            lcm = (x*y)/gcd(x,y)
            return lcm

        counter = 1
        tmp_A = A
        while len(A) <= lcm(len(tmp_A), len(B)):
            if B in A:
                return counter
            else:
                counter += 1
                A += tmp_A
                print(len(A))
        return -1
"abcabcabcabc"
"abac"
