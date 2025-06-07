class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [None] * len(nums)
        i = 0
        # if the first number is positive then the list is already ordered
        if nums[0] >= 0:
            for num in nums:
                result[i] = num ** 2
                i += 1
        # if the whole list is negative then it's already sorted but in reverse
        elif nums[len(nums) - 1] <= 0:
            for num in reversed(nums):
                result[i] = num ** 2
                i += 1
        # mix of positive and negative      
        else:
            end_pointer = len(nums) - 1
            start_pointer = 0
            result_index = len(nums) - 1
            while end_pointer > start_pointer:
                if nums[end_pointer] < abs(nums[start_pointer]):
                    result[result_index] = nums[start_pointer] ** 2
                    start_pointer += 1
                    
                elif nums[end_pointer] >= abs(nums[start_pointer]):
                    result[result_index] = nums[end_pointer] ** 2
                    end_pointer -= 1
                
                result_index -= 1
            result[result_index] = nums[end_pointer] ** 2
                    
        return result
