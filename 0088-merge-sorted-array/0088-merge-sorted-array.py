class Solution:
    
            
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1Index=m-1
        nums2Index=n-1
        
        newCreation=n+m-1
        while nums1Index>-1 and nums2Index>-1:
            
            if nums1[nums1Index]<nums2[nums2Index]:
                nums1[newCreation]=nums2[nums2Index]
                newCreation-=1
                nums2Index-=1
            else:
                nums1[newCreation]=nums1[nums1Index]
                newCreation-=1
                nums1Index-=1
        while nums2Index>-1:
            nums1[newCreation]=nums2[nums2Index]
            newCreation-=1
            nums2Index-=1     
        while nums1Index>-1:
            nums1[newCreation]=nums1[nums1Index]
            newCreation-=1
            nums1Index-=1