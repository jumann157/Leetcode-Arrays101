class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 0 # points to position of last unique element
        j = 1 # scan through the array
        while j < len(nums):
            if nums[k] == nums[j]:
                j += 1
            else:
                nums[k + 1] = nums[j]
                k += 1
                j += 1
        return k + 1
