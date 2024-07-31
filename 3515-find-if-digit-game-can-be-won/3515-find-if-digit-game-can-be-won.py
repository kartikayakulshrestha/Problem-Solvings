class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        ssum=0
        dsum=0
        for i in nums:
            if len(str(i))==1:
                ssum+=i
            elif len(str(i))==2:
                dsum+=i
        return dsum!=ssum