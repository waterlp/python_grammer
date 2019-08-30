def binarySearch_t(nums, target):
    # write your code here
    len_nums = len(nums)
    j = 0
    for i in range(0, len_nums):
        if target == nums[i]:
            j += 1
            return i
    if j == 0:
        return -1


def binarySearch_x(nums, target):
    left = 0
    right = len(nums)
    ans = -1
    while (left <= right):
        mid = int(round((left + right)/2,0)) - 1
        if (nums[mid] == target):
            while True:
                if (nums[mid] == target):
                    mid -= 1
                    continue
                else:
                    ans = mid + 1
                    break
            break
        elif (nums[mid] < target):
            left = mid + 1
        else:
            right = mid - 1
    return ans

def binarySearch(nums, target):
    left = 0
    max = len(nums)
    mid =

if __name__ == '__main__':
    nums = [4,5,9,9,12,13,14,15,15,18]
    target = 10
    s = binarySearch(nums,target)
    print(s)
    # x = 5
    # print(int(3 / 2))

