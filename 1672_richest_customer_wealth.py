# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 22:21:28 2022

@author: Sama Samrin

Runtime: 40 ms
Memory Usage: 13.5 MB
"""

def maximumWealth(accounts):
        total_wealth = [None]*len(accounts) 
        i=0
        
        while i<len(accounts):
            i_wealth = 0
            for j in accounts[i]:
                i_wealth = i_wealth + j   
            total_wealth[i] = i_wealth
            i+=1
            
        max_wealth = max(total_wealth)
        
        return max_wealth
    
print(maximumWealth([[1,2,3],[3,2,1]])) #6
print(maximumWealth([[1,5],[7,3],[3,5]])) #10
print(maximumWealth([[2,8,7],[7,1,3],[1,9,5]])) #17
