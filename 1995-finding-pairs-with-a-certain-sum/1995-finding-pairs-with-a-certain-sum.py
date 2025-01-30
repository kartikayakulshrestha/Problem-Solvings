class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.dic1={}
        self.dic2={}
        self.nums2=nums2
        for i in nums1:
            if i in self.dic1:
                self.dic1[i]+=1
            else:
                self.dic1[i]=1
        for i in nums2:
            if i in self.dic2:
                self.dic2[i]+=1
            else:
                self.dic2[i]=1
        return 

    def add(self, index: int, val: int) -> None:
        
        valAtIndex=self.nums2[index]
        
        self.dic2[valAtIndex]-=1
        if self.dic2[valAtIndex]==0:
            self.dic2.pop(valAtIndex)
        self.nums2[index]+=val
        p=valAtIndex+val
        if p in self.dic2:
            self.dic2[p]+=1
        else:
            self.dic2[p]=1
        return 

    def count(self, tot: int) -> int:
        c=0
        
        for val,count in self.dic1.items():
            if tot-val in self.dic2:
                print(tot-val,self.dic2[tot-val])
                c+=self.dic1[val]*self.dic2[tot-val]
        return c

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)