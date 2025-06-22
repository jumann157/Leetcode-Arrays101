class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        oddTracker = -1
        l = len(nums)
        
        for i in range(l):
            if oddTracker >= 0:
                if nums[i] % 2 == 0:
                    temp = nums[oddTracker]
                    nums[oddTracker] = nums[i]
                    nums[i] = temp
                    oddTracker += 1
            else:
                if nums[i] % 2 != 0:
                    oddTracker = i
                    
        return nums
# This solution has O(n) time complexity and O(1) space complexity
