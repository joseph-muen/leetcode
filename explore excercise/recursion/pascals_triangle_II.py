class Solution(object):
    def getRow(self, rowIndex):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for row in range(0, rowIndex+1):
            tmp_result = []
            for col in range(0, row+1):
                if col == 0 or row == col:
                    value = 1
                else:
                    value = result[col-1] + result[col]
                tmp_result.append(value)
            result = tmp_result
        return result
