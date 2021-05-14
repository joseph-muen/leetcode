class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return len(nums)
        else:
            pointer_1 = 0
            while pointer_1 < len(nums)-1:
                pointer_2 = pointer_1 + 1
                if nums[pointer_1] == nums[pointer_2]:
                    nums.remove(nums[pointer_2])
                else:
                    pointer_1 += 1
            return len(nums)
