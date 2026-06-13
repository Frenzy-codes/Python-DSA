class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int):
        maxCandies = max(candies)
        ans = []

        for i in candies:
            if (i + extraCandies) >= maxCandies:
                ans.append(True)
            else:
                ans.append(False)

        return ans
        
obj = Solution()
print(obj.kidsWithCandies([2,3,5,1,3], 3))