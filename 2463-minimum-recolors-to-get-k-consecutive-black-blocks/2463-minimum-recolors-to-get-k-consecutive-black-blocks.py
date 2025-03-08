class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        black=0
        white=0
        n=len(blocks)
        i,j=0,0
        mini=n
        while j<n:
            if j-i<k:
                if blocks[j]=="W":
                    white+=1
                elif blocks[j]=="B":
                    black+=1
                j+=1
            else:
                if white<mini:
                    mini=white
                if blocks[i]=="W":
                    white-=1
                elif blocks[i]=="B":
                    black-=1
                i+=1
        return min(mini,white)
        