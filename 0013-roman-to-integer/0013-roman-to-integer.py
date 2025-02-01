class Solution:
    def romanToInt(self, s: str) -> int:
        dic={
            "I":1,
            "IV":4,
            "V":5,
            "IX":9,
            "X":10,
            "XL":40,
            "L":50,
            "XC":90,
            "C":100,
            "CD":400,
            "D":500,
            "CM":900,
            "M":1000
        }
        i=0
        c=0
        while i<len(s):
            p=s[i:i+2]
            
            if p in dic:
                c+=dic[p]
                i+=2
            else:
                c+=dic[s[i]]
                i+=1
        return c     
        