class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        def recur(index,l):
            if index==-1:
                return [l]
            left=recur(index-1,[nums[index]]+l)
            right=recur(index-1,l)
            return left+right
        
        return recur(n-1,[])