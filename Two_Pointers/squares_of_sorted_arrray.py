class Solution(object):
    def sortedSquares(self, nums):
        s=[]
        for i in nums:
            a=i*i
            s.append(a)  
        s.sort()
        return s
