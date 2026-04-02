class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        #n=len(num)
        l=1
        r=num
        while l<=r:
            m=(l+r)//2
            sq=m*m
            if sq >num:
                r=m-1
            elif sq< num:
                l=m+1
            else:
                return True
        return False                 