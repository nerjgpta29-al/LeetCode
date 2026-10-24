class Solution(object):
    def reverseOnlyLetters(self, s):
        a=set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        sl=list(s)
        l=0
        r=len(s)-1
        while l<r:
            while l<r and sl[l] not in a:
                l+=1
            while l<r and sl[r] not in a:
                r-=1
            sl[l],sl[r]=sl[r],sl[l]
            l+=1
            r-=1
        return "".join(sl)
