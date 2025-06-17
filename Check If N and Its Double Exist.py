# This is my original solution
class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr) == 0:
            return False
         
        for i in range(len(arr)):
            for j in range(len(arr)): 
                if i == j or arr[i] % 2 != 0:
                    continue
                
                if arr[i] == 2 * arr[j]:
                    return True
                
        
        return False

  # This the optimized solution
  # It utilizes the set data structure and decreases time complexity from O(n^2) to O(n)

  # explored = set()
  # for num in arr:
  #   if (num * 2 in explored) or (num % 2 == 0 and num // 2 in explored):
  #     return True
  #   explored.add(num)
  # return False

