# my solution
class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # create a new array to store expected results
        expected = heights[:]
        
        # sort this array using insertion sort
        length = len(expected)
        for x in range(1,length):
            key = expected[x] # current element
            j = x - 1 # point to element before
            
            while j >= 0 and expected[j] > key:
                expected[j + 1] = expected[j]
                j -= 1
            expected[j + 1] = key
                
        # check how many elements are not in the same position
        notMatched = 0
        
        for i in range(0, length):
            if heights[i] != expected[i]:
                notMatched += 1
                
        # return notMatched
        return notMatched

  # Time complexity: O(n^2)

#     // More optimal solution
#     expected = sorted(heights) // time complexity of O(n log n)
# 
#       // check how many elements are not in the same position
#       notMatched = 0
#       
#     for i in range(0, length):
#        if heights[i] != expected[i]:
#               notMatched += 1
#               
#       return notMatched


