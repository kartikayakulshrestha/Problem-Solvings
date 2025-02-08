class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ass=int(a,2)
        bss=int(b,2)

        tot=ass+bss
        
        return bin(tot)[2:]