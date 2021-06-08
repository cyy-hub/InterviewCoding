import pdb
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def isValid(string):
            count = 0
            for char in string:
                if char == "(":
                    count += 1
                elif char == ")":
                    count -= 1
                if count < 0:     # 中途中计数器如果小于0说明，不明多余右括号出现
                    return False
            return count == 0
         # BFS
        level = {s}  # 用set避免重复
        # pdb.set_trace()
        while True:
            valid = list(filter(isValid, level))  # 所有合法字符都筛选出来
            if valid: return valid # 如果当前valid是非空的，说明已经有合法的产生了
            # 下一层level
            next_level = set()
            for item in level:
                for i in range(len(item)):
                    if item[i] in "()":                     # 如果item[i]这个char是个括号就删了，如果不是括号就留着
                        next_level.add(item[:i]+item[i+1:])
                        print(item[:i]+item[i+1:])
            print(level,next_level,valid)
            level = next_level

so = Solution()
so.removeInvalidParentheses("()())()")