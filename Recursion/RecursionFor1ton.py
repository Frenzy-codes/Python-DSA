#using while loop
# n =5 
# i = 1

# while i <=5:
#     print(i, end = " ")
#     i+=1

#using recursion
def printNumber(i, n):
    #base case
    if i>n:
        return
    # recursive case
    print(i, end=" ")
    printNumber(i+1, n)

printNumber(1, 5)