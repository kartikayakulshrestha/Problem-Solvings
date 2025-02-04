class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        m=len(matrix[0])
        for arr in matrix:
            if arr[0]<=target<=arr[m-1]:
                l=0
                r=m-1
                while l<=r:
                    mid=l+(r-l)//2
                    if arr[mid]==target:
                        return True
                    elif arr[mid]<target:
                        l=mid+1
                    else:
                        r=mid-1
        return False

        