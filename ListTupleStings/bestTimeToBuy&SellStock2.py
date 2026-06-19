def maxProfit(prices: list[int]):
    profit = 0
    n = len(prices)

    for i in range(n-1):
        if prices[i+1] > prices[i]:
            profit += (prices[i+1] - prices[i])

    return profit

ls =[7,1,5,3,6,4]
print(maxProfit(ls))