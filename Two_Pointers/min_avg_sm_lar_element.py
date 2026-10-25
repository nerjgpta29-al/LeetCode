class Solution(object):
    def minimumAverage(self, nums):
        nums.sort()
        a=[]
        l=0
        r=len(nums)-1
        while l<r:
            avg=(nums[l]+nums[r])/2.0
            l+=1
            r-=1
            a.append(avg)
        return min(a)
