class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # board[i][j] 都进行深度优先匹配
        def dfs(i,j,word):
            if len(word) == 0:    # word 为空字符串时,匹配完成
                return True
            if len(word) == 1 and board[i][j] == word[0]:
                return True
            if board[i][j] != word[0]: # 第一字符不匹配，完全不用递归，直接输出
                return False
            tmp = board[i][j]                           # 完全没有考虑不能重复走 
            board[i][j] = None
            for r,c in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]: # 第一哥字符匹配，递归处理
                if 0<= r < m and 0 <= c < n:
                    if dfs(r,c,word[1:]):  # 如果四个方向中有一格方向是可行的就返回True       
                        return True
            board[i][j] = tmp
            return False                # 第一个字符匹配了，但是后面的都不配，输出False
            

        m = len(board)
        if m == 0:
            return word == "" 
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if dfs(i,j,word):
                    return True
        return False  # 所有遍历过了，没有就输出false

#[["a"]],"a"
#[["a"]],"a"