class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        reached=[0]*n
        if nums[0]==0:
            reached[0]=False
        else:
            reached[0]=True
        
        if n==1:
            return True
        for i in range(n):
            if reached[i]:
                for j in range(i+1,min(i+nums[i]+1,n)):
                    reached[j]=True
        return True if reached[-1] else False
        