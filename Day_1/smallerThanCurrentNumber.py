class solution():
    def smallerThanCurrentNumber(self,nums):
        ans = []
        for i in nums:
            c = 0
            for j in nums:
                if j<i:
                    c = c + 1
            ans.append(c)
        return ans
    
obj = solution()
print(obj.smallerThanCurrentNumber([6,5,4,8]))