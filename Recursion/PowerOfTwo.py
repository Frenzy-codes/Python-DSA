def IsPowerOfTwo(n):
    #using loops
    # if n<=0:
    #     return False
    # while n%2 == 0:
    #     n//=2
    #     return True

    #using recursion
    if n<=0:
        return False
    if n==1:
        return True
    if n%2 != 0:
        return False
    
    return IsPowerOfTwo(n//2)
    
print(IsPowerOfTwo(16))