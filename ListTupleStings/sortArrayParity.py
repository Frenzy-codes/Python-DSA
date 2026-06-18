def sortArrayParity(nums: list[int]):
    n = len(nums)

    start = 0
    for i in range(n):
        if nums[i]%2 == 0:
            temp = nums[i]
            nums[i] = nums[start]
            nums[start] = temp
            start+=1

    return nums
ls = [5,1,6,2,7,4,3]
print(sortArrayParity(ls))