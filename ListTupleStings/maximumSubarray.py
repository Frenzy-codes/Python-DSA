def maximumSubarray(nums: list[int]):
    n = len(nums)

    curr_sum = 0
    max_sum = nums[0]

    for i in range(n):
        curr_sum += nums[i]

        if curr_sum > max_sum:
            max_sum = curr_sum

        if curr_sum < 0:
            curr_sum = 0
    return max_sum

ls = [-2,1,-3,4,-1,2,1,-5,4]
print(maximumSubarray(ls))