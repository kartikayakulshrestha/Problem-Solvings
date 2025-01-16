from heapq import *
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=[]
        for i in nums:
            heappush(heap,-i)
        x=0
        for i in range(k):
            x=-heappop(heap)
        return x