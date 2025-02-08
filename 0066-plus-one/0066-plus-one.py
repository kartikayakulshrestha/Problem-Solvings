class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)
        carry=0
        for i in range(n-1,-1,-1):
            if i==n-1:
                if digits[i]==9:
                    digits[i]=0
                    carry=1
                else:
                    digits[i]+=1
                    return digits
            else:
                if digits[i]==9 and carry:
                    digits[i]=0
                else:
                    digits[i]+=carry
                    carry=0
        if carry==1:
            digits=[1]+digits
        return digits