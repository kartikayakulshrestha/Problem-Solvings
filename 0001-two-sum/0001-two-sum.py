class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for i,e in enumerate(nums):
            dic[e]=i

        for i,e in enumerate(nums):
            x=target-e
            if x in dic and dic[x]!=i:
                return [i,dic[x]]
        return []