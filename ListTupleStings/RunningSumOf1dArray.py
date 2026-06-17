def runningSum(nums: list[int]):
    n = len(nums)
    ans = []

    ans.append(nums[0])

    for i in range(1, n):
        x = ans[i-1] + nums[i]
        ans.append(x)

    return ans

ls = [1,2,3,4]
print(runningSum(ls))