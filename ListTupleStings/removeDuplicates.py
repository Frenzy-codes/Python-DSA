def removeDuplicates(nums: list[int]):
    n = len(nums)

    start = 0
    for i in range(1,n):
        if nums[i] != nums[start]:
            start+=1
            nums[start] = nums[i]
    
    print(f"Unique: {nums[:start+1]}")
    return (start+1)


ls = [3,3,5,7,7,7,9,9,12,12]   
print(removeDuplicates(ls))
