class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        counter = 0
        while counter < len(nums):
            num1 = nums[counter]
            num2 = target - num1
            if num2 in nums[(counter+1):]:
                index1 = counter
                index2 = nums[(counter+1):].index(num2) + counter + 1
                return [index1, index2]
            else:
                counter += 1


Solution().twoSum([3,2,4], 6)

a = [3,2,4]

for i in a:
    print(i)