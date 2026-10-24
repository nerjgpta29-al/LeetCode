class Solution(object):
    def moveZeroes(self, nums):
        pos=0
        for i in range(len(nums)):
            if nums[i]!=0:
                temp=nums[i]
                nums[i]=nums[pos]
                nums[pos]=temp
                pos+=1
        return nums
