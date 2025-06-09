class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # i is the main pointer, j tracks the number of elements that need to be shifted
        i = len(nums) - 1
        j = 0
        count2 = 0
        # loop through the array
        while i >= 0:
            # if the current element is equal to the value
            if nums[i] == val:
                count2+=1
                j = i + 1
                # loop through the array from the current index + 1 element until the end of the array
                while j < len(nums):
                    nums[j - 1] = nums[j]
                    j+= 1
            i -= 1
        
        return len(nums) - count2
