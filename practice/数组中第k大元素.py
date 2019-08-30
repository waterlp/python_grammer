
def kthLargestElement_t(n, nums):
    nums.sort()
    nums.reverse()
    m = nums[n-1]
    return m

def kthLargestElement(n, nums):
    nums_len = len(nums)
    for i in range(0,nums_len):
        for j in range(i,nums_len):
            if nums[j]>nums[i]:
                mid = nums[i]
                nums[i] = nums[j]
                nums[j] = mid
    m = nums[n - 1]
    print(nums)
    return m



if __name__ == '__main__':
    n = 5
    nums = [1,3,4,2,3,5]
    s = kthLargestElement(n,nums)
    print(s)
    # nums.sort()
    # nums.reverse()

