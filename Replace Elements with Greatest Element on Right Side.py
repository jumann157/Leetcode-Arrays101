class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        if len(arr) == 1:
            arr[0] = -1
            
        max_value = arr[len(arr) -  1] # keeps tracks of max int to the right of the current index
        current = len(arr) - 2 # points to the current index
        
        while current >= 0:
            temp = arr[current]
            arr[current] = max_value
            max_value = max(max_value, temp)
            current -= 1
        arr[len(arr) - 1] = -1
        
        return arr
