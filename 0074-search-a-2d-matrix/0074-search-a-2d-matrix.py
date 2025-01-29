class Solution:
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        m=len(matrix[0])
        def applyBS(l,r,index):
            
            while l<=r:
                mid=l+(r-l)//2
                if matrix[index][mid]==target:
                    return True
                elif matrix[index][mid]<target:
                    l=mid+1
                else:
                    r=mid-1
            return False
        for i in range(n):
            l=0
            r=m-1
            if target<=matrix[i][r] and target>=matrix[i][l]:
                if applyBS(l,r,i):
                    return True
        return False
        