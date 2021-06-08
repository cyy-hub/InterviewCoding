class Solution(object):
    def __init__(self):
        self.res = 0
        self.flag = False

    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        p = 1
        prefix = 1
        while(p<k):
            count = self.getcount(prefix,n)
            print(prefix,count,p)
            if p+count > k:        # 在这个前缀里面   1+11=12< 19
                prefix *= 10
                p += 1
            else:                  # 不在这个前缀里面   
                prefix += 1
                p += count
        return prefix
    def getcount(self,prefix,n):
        cur_val = prefix
        next_val = prefix+1
        count = 0
        while(cur_val <= n ):
            count += min(next_val, n+1) - cur_val   #下一个前缀的起点，减去当前前缀的起点
            cur_val *=10
            next_val *=10
        return count
so = Solution()
print(so.findKthNumber(23,19))
    	
