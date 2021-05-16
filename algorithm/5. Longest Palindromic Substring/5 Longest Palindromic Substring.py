class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        result_str = s[0]
        pointer = 0

        while pointer < len(s) - 1:
            if s[pointer] == s[pointer + 1]:
                tmp_str = s[pointer: pointer + 2]
                right = pointer + 2
                left = pointer - 1
            else:
                tmp_str = s[pointer]
                left = pointer - 1
                right = pointer + 1
            while (left >= 0) & (right < len(s)):
                if len(set(tmp_str)) == 1:
                    if s[left] == tmp_str[0]:
                        tmp_str = s[left] + tmp_str
                        left -= 1
                    if s[right] == tmp_str[0]:
                        tmp_str = tmp_str + s[right]
                        right += 1
                    if (left < 0) | (right == len(s)):
                        break
                    else:
                        if s[left] == s[right]:
                            tmp_str = s[left: right + 1]
                            left -= 1
                            right += 1
                        else:
                            break
                else:
                    if s[left] == s[right]:
                        tmp_str = s[left: right + 1]
                        left -= 1
                        right += 1
                    else:
                        break
            if len(set(tmp_str)) == 1:
                if left >= 0:
                    if s[left] == tmp_str[0]:
                        tmp_str = s[left] + tmp_str
                elif right < len(s):
                    if s[right] == tmp_str[0]:
                        tmp_str = tmp_str + s[right]
                else:
                    pass
            if len(tmp_str) > len(result_str):
                result_str = tmp_str
            pointer += 1
        return result_str


'''
Runtime: 7264 ms, faster than 15.56% of Python online submissions for Longest Palindromic Substring.
Memory Usage: 13.7 MB, less than 29.08% of Python online submissions for Longest Palindromic Substring.
'''