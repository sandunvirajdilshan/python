nums = [1, 3, 5, 6]
number = int(input("Enter a Number: "))
s = 0
e = len(nums) - 1
while s <= e:
    m = (s + e) // 2
    if nums[m] == number:
        print(m)
        break
    elif nums[m] < number:
        s = m + 1
    else:
        e = m - 1
else:
    print("-1")
