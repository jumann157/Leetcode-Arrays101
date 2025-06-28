class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = pow(-2, 33)
        second = pow(-2, 33)
        third = pow(-2, 33)
        max_return = 0
        
        for num in nums:
            if num != first and num != second and num != third:
                if num > first:
                    third = second
                    second = first
                    first = num
                elif num > second:
                    third = second
                    second = num
                elif num > third:
                    third = num
          
        if third == pow(-2, 33):
            max_return = first
        else:
            max_return = third
            
        return max_return
        
