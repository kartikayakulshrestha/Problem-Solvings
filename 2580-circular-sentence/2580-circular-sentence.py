class Solution:
    def isCircularSentence(self, sentence: str) -> bool:

        x=sentence.split()
        x.append(x[0])
        
        for i in range(1,len(x)):
            if x[i-1][-1]!=x[i][0]:
                return False
        return True

        