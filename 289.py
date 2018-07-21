class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m=len(board)
        n=len(board[0])
        def judge1(x,y):
            if x>=0 and y>=0 and x<m and y<n and (board[x][y]==1 or board[x][y]=='1'):
                return 1
            else:
                return 0
        def count1(x,y):
            count=0
            count+=judge1(x+1,y)
            count+=judge1(x+1,y+1)
            count+=judge1(x+1,y-1)
            count+=judge1(x-1,y)
            count+=judge1(x-1,y+1)
            count+=judge1(x-1,y-1)
            count+=judge1(x,y+1)
            count+=judge1(x,y-1)
            return count
        for i in range(m):
            for j in range(n):
                tmp=count1(i,j)
                if tmp>3 or tmp<2:
                    if board[i][j]==1:
                        board[i][j]='1'
                elif tmp==3:
                    if board[i][j]==0:
                        board[i][j]='0'
        for i in range(m):
            for j in range(n):
                if board[i][j]=='1':
                    board[i][j]=0
                if board[i][j]=='0':
                    board[i][j]=1