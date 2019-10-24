# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
#
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it.
#
# Example:
#
# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for row in range(0, numRows):
            tmp_result = []
            for col in range(0, row+1):
                if col == 0 or row == col:
                    value = 1
                else:
                    value = result[row-1][col-1] + result[row-1][col]
                tmp_result.append(value)
            result.append(tmp_result)
        return result

