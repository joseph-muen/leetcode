# my own solution
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 1
        else:
            max_len = 0
            index_1 = 0
            while index_1 < len(s):
                index_2 = index_1 + 1
                while index_2 < len(s):
                    if s[index_2] in s[index_1: index_2]:
                        max_len = max(max_len, index_2 - index_1)
                        break
                    else:
                        max_len = max(max_len, index_2 - index_1 + 1)
                        index_2 += 1
                index_1 += 1

            return max_len

# optimised solution from leetcode

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        mp = {}
        ans = 0
        i = 0
        for j in range(len(s)):
            if s[j] in mp:
                i = max(mp[s[j]], i)

            ans = max(j - i + 1, ans)
            mp[s[j]] = j+1
        return ans


x = Solution().lengthOfLongestSubstring('abcbad')