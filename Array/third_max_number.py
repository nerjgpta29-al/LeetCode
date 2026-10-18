class Solution(object):
    def thirdMax(self, nums):
        unique=set(nums)
        a=list(unique)
        a.sort(reverse=True)
        return a[2] if len(a)>=3 else a[0]
