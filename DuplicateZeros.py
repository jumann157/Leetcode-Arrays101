class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        i, j = 0, 0
        while i < len(arr) - 1:
            if arr[i] == 0:
                j = len(arr) - 1
                while j!=i:
                    arr[j] = arr[j - 1]
                    j -= 1
                i += 2
                j += 2
            else:
                i += 1
                j += 1
        
