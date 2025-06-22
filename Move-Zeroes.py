class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        x = -1 # tracks first zero
        y = 0 # iterates over array
        
        while y < len(nums):
            if x >= 0:
                if nums[y] != 0:
                    nums[x] = nums[y]
                    nums[y] = 0
                    x += 1  
            else:
                if nums[y] == 0:
                    x = y
                    
            y += 1 # outside of if-statement
