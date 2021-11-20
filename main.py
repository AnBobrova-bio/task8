def kbig(nums, k):
    i = 1
    nums_new = nums
    for i in range(k):
        max_out = max(nums_new)
        j = nums_new.index(max_out)
        nums_new.pop(j)
    print(max_out)

nums = input().split()
k = int(input())
kbig(nums, k)