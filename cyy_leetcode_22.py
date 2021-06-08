def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    res = []
    def back_track(s,left,right):
        if len(s) == 2*n:
            res.append(s)
            return 
        if left < n:
            back_track(s+"(",left+1,right)
        if right< left:                # 保证不会生成不合理的括号 ，必须要有配对的左括号已经存在
            back_track(s+")",left,right+1)
    back_track("",0,0)
    return res
print(generateParenthesis(3))

