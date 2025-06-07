class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count = 0
        currentConsOne = 0
        for num in nums:
            if num == 1:
                currentConsOne += 1
            else:
                if currentConsOne > max_count:
                    max_count = currentConsOne
                    currentConsOne = 0
                else:
                    currentConsOne = 0

        if currentConsOne > max_count:
            max_count = currentConsOne
        
        return max_count
