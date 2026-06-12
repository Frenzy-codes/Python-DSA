def find_duplicates(numbers):
    for i in numbers:
        for j in numbers:
            if i != j and numbers[i] == numbers[j]:
                return True
    return False

numbers = [1,2,3,4,5,5,6,7,8,9,10]

result = find_duplicates(numbers)

if result:
    print("Duplicate found")
else:
    print("No duplicates found") 