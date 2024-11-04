class Solution:
    def compressedString(self, word: str) -> str:
        c=1
        word+="A"
        s=""
        for i in range(1,len(word)):
            
            if c==9 or word[i-1]!=word[i]:
                s+=str(c)+word[i-1]
                c=1
            else:
                c+=1
        return s
        