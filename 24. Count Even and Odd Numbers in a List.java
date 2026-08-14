24. Count Even and Odd Numbers in a List
numbers = [10, 15, 22, 31, 40, 47, 50]


even = 0
odd = 0


for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1


print("Even numbers:", even)
print("Odd numbers:", odd)

Output:

Even numbers: 4
Odd numbers: 3
