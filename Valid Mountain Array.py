# My original solution
class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr) < 3:
            return False
        
        # keeps track of the peak
        i = -1
        
        for index in range(len(arr) - 1):
            if index != 0:
                if arr[index] == arr[index + 1]:
                    return False
                elif i < 0 and arr[index] > arr[index + 1]:
                    i = index
                elif i > 0 and arr[index] <= arr[index + 1]:
                    return False
            else:
                if arr[index] >= arr[index + 1]:
                  return False
               
        if i < 0:
            return False
        return True

# Cleaner solution

# if len(arr) < 3:
#   return False:
#
# i = 0 –– keeps track of peak
#
# walk up mountain
# while i < len(arr) - 1 and arr[i] < arr[i + 1]:
#   i += 1
# 
# check peak
# if i == 0 or i == len(arr)
#   return False
#
# walk down mountain
# while i < len(arr) - 1 and arr[i] > arr[i + 1]:
#   i += 1
#
# return i == len(arr) - 1
