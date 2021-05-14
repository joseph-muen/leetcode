class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        for i in range(len(nums)):
            for j in range(i+1, min(i+k+1, len(nums))):
                diff = abs(nums[i] - nums[j])
                if diff <= t:
                    return True
        return False

nums = [1,5,9,1,5,9]
k = 2
t = 3

Solution().containsNearbyAlmostDuplicate(nums, k, t)