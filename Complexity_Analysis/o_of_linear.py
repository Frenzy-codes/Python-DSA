def find_name(names, target):
    for i in names:
        if i == target:
            return True
    return False

names = ["rahul", "rohan", "ankit", "shubham", "satyam", "sagar", "abhay", "abhijeet", "rahul", "rohit"]
print(find_name(names, "satyam"))

if "satyam" in names:
    print("Present")
else:
    print("Not Present")
    