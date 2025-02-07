class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        
        p=str(x)
        return p==p[::-1]