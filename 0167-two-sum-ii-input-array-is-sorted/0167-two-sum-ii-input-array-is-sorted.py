class Solution:
    def twoSum(self, arr: List[int], target: int) -> List[int]:
        dic={}
        n=len(arr)
        for i in range(n):
            x=target-arr[i]
            if arr[i] in dic:
                return [dic[arr[i]]+1,i+1]
            dic[x]=i
        
