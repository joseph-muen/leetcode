class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        counter = total_len = (len(nums1) + len(nums2))
        cut_off = total_len // 2 - 1
        comb_list = []
        while (counter >= cut_off) & (len(nums1) != 0) & (len(nums2) != 0):
            if nums1[-1] >= nums2[-1]:
                comb_list.insert(0, nums1.pop())
            else:
                comb_list.insert(0, nums2.pop())
            counter -= 1

        if (len(nums1) != 0) & (len(nums2) != 0):
            if total_len % 2 == 1:
                return comb_list[2]
            else:
                return (float(comb_list[2]) + float(comb_list[1]))/2

        else:
            tmp_list = nums1 + nums2 + comb_list
            if total_len % 2 == 1:
                return tmp_list[len(tmp_list)//2]
            else:
                return (float(tmp_list[len(tmp_list)//2-1]) + float(tmp_list[len(tmp_list)//2]))/2

nums1 = [1]
nums2 = [2,3,4,5,6,7,8]
a = Solution().findMedianSortedArrays(nums1, nums2)