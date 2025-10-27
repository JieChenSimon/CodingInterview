def findFirstX(nums, x):
    left, right = 0, len(nums) -1
    results = -1

    while(left <= right):
        mid = left + right // 2
        if nums[mid] >= x:
            results = mid
            right = mid - 1
        else:
            left = mid + 1
    return results
CodingInterview



