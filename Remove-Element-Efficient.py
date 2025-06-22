class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        k = 0 # keeps track of non-val elements
        y = 0 # iterates over array
        
        while y < len(nums):
            if nums[y] != val:
                nums[k] = nums[y]
                k += 1
            y += 1
            
        return k
