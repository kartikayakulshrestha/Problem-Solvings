class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        n=len(board)
        m=len(board[0])
        def recur(i,j,s,index):
            if index>=len(word):
                print(s)
                if s==word:
                    
                    return True
                else:
                    return False
            top = left = right = down = False
            if j < m - 1:
                if board[i][j + 1] == word[index] and visited[i][j + 1]:
                    visited[i][j + 1] = False
                    right = recur(i, j + 1, s + board[i][j + 1], index + 1)
                    visited[i][j + 1] = True
            if i < n - 1:
                if board[i + 1][j] == word[index] and visited[i + 1][j]:
                    visited[i + 1][j] = False
                    down = recur(i + 1, j, s + board[i + 1][j], index + 1)
                    visited[i + 1][j] = True
            if j > 0:
                if board[i][j - 1] == word[index] and visited[i][j - 1]:
                    visited[i][j - 1] = False
                    left = recur(i, j - 1, s + board[i][j - 1], index + 1)
                    visited[i][j - 1] = True
            if i > 0:
                if board[i - 1][j] == word[index] and visited[i - 1][j]:
                    visited[i - 1][j] = False
                    top = recur(i - 1, j, s + board[i - 1][j], index + 1)
                    visited[i - 1][j] = True
            return top or down or left or right
        for i in range(n):
            for j in range(m):
                visited=[[True]*m for i in range(n)]
                if board[i][j]==word[0]:
                    visited[i][j]=False
                    x=recur(i,j,word[0],1)
                    if x:
                        return True
        return False