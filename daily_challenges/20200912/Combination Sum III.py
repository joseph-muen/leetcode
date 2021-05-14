class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        arr = []
        while n!= 1:
            for i in range(n):
                tmp_arr = []
                for j in range(k):
                    tmp_arr.apend(i)


        # def helper(arr, k, n, counter):
        #     if n == 1:
        #         if k < counter:
        #             return []
        #         if k >= counter:
        #             arr.append(k)
        #             return arr
        #     else:
        #         arr.append(counter)
        #         n -= 1
        #         k -= counter
        #         counter += 1
        #         return helper(arr, k, n, counter)
        #
        # result = []
        # for counter_n in range(1, n):
        #     arr = []
        #     tmp_result = helper(arr, k, n, counter_n)
        #     if tmp_result:
        #         result.append(tmp_result)
        # return result




Solution().combinationSum3(9, 3)


arr = []
k = 7
n = 3
counter = 1
flag = True