class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=j=0
        n=len(nums)
        while j<n:
            if nums[i]!=val:
                i+=1
                j+=1
            else:
                if nums[j]==val:
                    j+=1
                else:
                    nums[i],nums[j]=nums[j],nums[i]
                    i+=1
                    j=i
        return i
        