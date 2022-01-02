class Solution(object):
    def maximumProduct(self, nums):
        product = 1;
        if len(nums)<=3:
            for i in nums:
                product = product * i
            return product
        else:
            nums.sort()
            product = nums[-1] * nums[-2] * nums[-3]
            return product
