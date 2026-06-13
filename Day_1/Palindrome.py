class solution():
    def palindrome(self, x: int):
        temp = x
        rev = 0

        while temp>0:
            r = temp%10
            rev = rev * 10 + r
            temp //=10

        if rev == x:
            return True
        else:
            return False
        
obj = solution()
n = int(input("Enter the number: "))
print(obj.palindrome(n))