class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        digits, even = 0, 0
        for num in nums:
            while num != 0:
                num /= 10
                digits += 1
            
            if digits % 2 == 0:
                even += 1
            
            digits = 0
        
        return even
