# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 17:18:08 2022

@author: ASUS
"""

def twoSum(nums, target):
        result = []
        iterator_for_i = 0
        iterator_for_j = 0
        for i in nums:
            #print("i=",  iterator_for_i)
            iterator_for_j=0
            for j in nums:
                #print("j=",  iterator_for_j)
                iterator_for_j+=1
                if j+i==target and iterator_for_i!=iterator_for_j:
                    #print("inside if")
                    result.append(iterator_for_i)
                    #print(result)
            iterator_for_i+=1
        result = list(dict.fromkeys(result))
        return result
    
r = twoSum([2,7,4,5], 6)
print("Final result=", r)