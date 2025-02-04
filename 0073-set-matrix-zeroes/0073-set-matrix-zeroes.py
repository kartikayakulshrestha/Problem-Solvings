class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        m=len(matrix[0])
        values=set()
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    values.add((i,j))
        for i,j in values:
            for k in range(n):
                matrix[k][j]=0
            for k in range(m):
                matrix[i][k]=0
        