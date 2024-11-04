class MedianFinder:

    def __init__(self):
        self.arr=[]
        
        return None

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        return None
    def findMedian(self) -> float:
        self.arr.sort()
        n = len(self.arr)
        if n%2:
            return self.arr[n//2]
        return (self.arr[n//2-1]+self.arr[n//2])/2
        
        

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()