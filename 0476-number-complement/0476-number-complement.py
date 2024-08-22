class Solution:
    def findComplement(self, num: int) -> int:
        binary=bin(num).lstrip("0b")
        x=""
        for i in range(len(binary)):
            if binary[i]=="1":
                x+="0"
            else:
                x+="1"
        return (int(x,2))
        