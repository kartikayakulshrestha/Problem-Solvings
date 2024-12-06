from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        for i in range(len(nums)+1):
            l=combinations(nums,i)
            for j in l:
                ans.append(list(j))
        return ans