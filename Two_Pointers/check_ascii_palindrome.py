class Solution:
    def isPalindromic(self, s: str) -> bool:
        b_s="".join(f"{ord(c):08b}" for c in s)
        l=0
        r=len(b_s)-1
        while l<r:
            if b_s[l]!=b_s[r]:
                return False
            l+=1
            r-=1
        return True
