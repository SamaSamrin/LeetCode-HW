def shuffle(self, nums, n):
        solution = [None]*(2*n)
        
        index = 0
        for i in nums[0:n]:
            solution[index] = i
            index+=2
        
        index = 1
        for i in nums[n:]:
            solution[index] = i
            index+=2
            
        return solution
      
"""
Runtime: 76 ms
Memory Usage: 13.7 MB
"""
