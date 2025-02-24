class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        memo=[[-1]*(n+1) for i in range(n)]
        def recur(prev,index):
            if index==len(nums):
                return 0
            if memo[prev][index]!=-1:
                return memo[prev][index]
            pick=0
            if prev==-1 or nums[prev]<nums[index]:
                pick=recur(index,index+1)+1
            nonpick=recur(prev,index+1)
            memo[prev][index]=max(pick,nonpick)
            return memo[prev][index]
        
        return recur(-1,0)
        