class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1 # nums1 pointer
        j = n - 1 # nums2 pointer
        list_pointer = (m + n) - 1
        while list_pointer >= 0:
            if j < 0:
                break
            elif i >= 0 and nums1[i] >= nums2[j]:
                nums1[list_pointer] = nums1[i]
                nums1[i] = 0
                i -= 1
            else:
                nums1[list_pointer] = nums2[j]
                j -= 1
            list_pointer -= 1
