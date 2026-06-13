class solution():
    def countOdds(self,low: int, high: int) ->int:
        return (high//2) - (low//2)

obj = solution()
l=int(input("Enter start number: "))
h=int(input("Enter last number: "))
print(obj.countOdds(l,h))
