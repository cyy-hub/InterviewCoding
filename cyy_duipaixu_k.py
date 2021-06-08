# 大顶堆，如果
def shift(nums,fa_index,high):
    tmp = nums[fa_index]
    chile_index = fa_index*2 + 1
    while(chile_index < high):
        if chile_index + 1 < high and nums[chile_index+1] < nums[chile_index]:
            chile_index += 1
        if tmp > nums[chile_index]:
            nums[fa_index] = nums[chile_index]
            fa_index = chile_index
            chile_index = fa_index * 2 + 1
        else:
            nums[fa_index] = tmp
            break
        nums[fa_index] = tmp

def building(nums):
    n = len(nums)
    for i in range((n-2)//2,-1,-1):
        shift(nums,i,n)

class Solution(object):
    def __init__(self):
        self.stack = []
    def find_topk(self, val,k):
        if len(self.stack) < k:
            self.stack.append(val)
            if len(self.stack) == k:
                building(self.stack)
        else:
            if val > self.stack[0]:
                self.stack[0] = val
                shift(self.stack,0,k)
so = Solution()
k = 3
nums = [3,2,1,5,6,4]
for val in nums:
    so.find_topk(val,k)
for i in range(k-1, -1, -1):
    so.stack[0],so.stack[i] = so.stack[i], so.stack[0]
    shift(so.stack, 0, i)
print(so.stack)

