def quick_sort(nums,l,r):
    if l < r:
        p = patition(nums,l,r)
        quick_sort(nums,l,p-1)
        quick_sort(nums,p+1,r)
    return nums
def patition(nums,i,j):
    pivort = nums[i]
    while(i<j):
        while(i<j and nums[j]>pivort):
            j-=1
        nums[i] = nums[j]
        while(i<j and nums[i]<= pivort):
            i+=1
        nums[j] = nums[i]
    nums[i] = pivort
    return i
# print(quick_sort([2,1,4,3,6,9],0,5))

def quick_sort_iter(nums,l,r):   # 
    stack = [l,r]
    while(stack):       
        i,j = stack.pop(0),stack.pop(0)
        p = patition(nums,i,j)
        if i<p-1:
            stack.append(i)
            stack.append(p-1)
        if p+1< j:
            stack.append(p+1)
            stack.append(j)
    return nums
# print(quick_sort_iter([2,1,4,3,6,9],0,5))

def merge_sort(nums,l,r):
    if l == r:
        return 
    mid = (l+r)//2
    merge_sort(nums,l,mid)
    merge_sort(nums,mid+1,r)
    tmp = []
    i,j = l,mid+1       # lr,ij一定要搞清楚
    while(i<=mid or j <= r):
        if (i>mid or (j<=r and nums[i] > nums[j]) ):
            tmp.append(nums[j])
            j+=1
        else:
            tmp.append(nums[i])
            i+=1
    nums[l:r+1] = tmp[:] 

# nums = [2,1,4,3,6,9]
# merge_sort(nums,0,5)
# print(nums)

def top_k(nums,k):
    n = len(nums)
    for i in range((n-2)//2,-1,-1):   # 构建一个堆，前一半是父亲节点，最底层的父亲节点开始
        shift(nums,i,n)
    for i in range(n-1,n-1-k,-1):
        nums[i], nums[0] = nums[0],nums[i]
        shift(nums,0,i)
    return nums[-k:]
def shift(nums,fa_index,high):
    tmp = nums[fa_index]
    chil_index = fa_index*2 +1
    while(chil_index<high):
        if chil_index+1 <high and nums[chil_index+1]> nums[chil_index]:
            chil_index +=1
        if tmp < nums[chil_index]:
            nums[fa_index]=nums[chil_index]
            fa_index = chil_index
            chil_index = fa_index*2+1
        else:
            nums[fa_index] = tmp
            break
    nums[fa_index] = tmp
        
print(top_k([2,1,4,3,1,9],2))