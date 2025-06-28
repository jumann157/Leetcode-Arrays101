class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
      
        # mark the index of every number that shows up by turning it negative
        for num in nums:
            pos = abs(num) - 1
            if nums[pos] > 0:
                nums[pos] *= -1
            
        # if it's still positive, it means that number didn't show up
        # so we just write it at the front of the array
        index = 0
        for x in range(n):
            if nums[x] > 0:
                nums[index] = x + 1
                index += 1
        
        return nums[:index]

  # Time complexity: O(n)
  # Space complexity: O(1)
