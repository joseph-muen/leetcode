# question link : https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/554/week-1-september-1st-september-7th/3445/

class Solution(object):
    def largestTimeFromDigits(self, arr):
        """
        :type arr: List[int]
        :rtype: str
        """
        def filter_condition(hour, min1, min2):
            if hour <= 23:
                if max(min1, min2) < 60:
                    return hour, max(min1, min2)
                else:
                    if min(min1, min2) < 60:
                        return hour, min(min1, min2)
                    else:
                        return -99, -99
            else:
                return -99, -99

        max_hour = -99
        max_min = -99
        for i in range(4):
            first_digit = arr[i]
            if first_digit <= 2:
                for j in range(3):
                    tmp_arr = arr.copy()
                    tmp_arr.remove(first_digit)
                    second_digit = tmp_arr[j]
                    hour = first_digit*10 + second_digit
                    tmp_arr2 = tmp_arr.copy()
                    tmp_arr2.remove(second_digit)
                    min1, min2 = tmp_arr2[0] *10 + tmp_arr2[1], tmp_arr2[1] *10 + tmp_arr2[0]
                    result = filter_condition(hour, min1, min2)
                    if result[0] > max_hour:
                        max_hour = result[0]
                        max_min = result[1]
                    elif result[0] == max_hour:
                        if result[1] > max_min:
                            max_min = result[1]
        if max_hour == -99:
            return ""
        else:
            if max_hour <10:
                max_hour = "0" + str(max_hour)
            if max_min < 10:
                max_min = "0" + str(max_min)
            return str(max_hour) + ":" + str(max_min)


arr = [1,9,6, 0]

Solution().largestTimeFromDigits(arr)