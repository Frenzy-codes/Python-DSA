class solution():
    def subtractProductSum(self, x: int):
        temp = x
        sum_ = 0
        prod = 1

        while temp>0:
            r = temp%10
            temp //=10

            sum_ +=r
            prod *=r

        return prod - sum_

obj = solution()
n = int(input("Enter the Number: "))
print(obj.subtractProductSum(n))
