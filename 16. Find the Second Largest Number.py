1. Find the Second Largest Number
numbers = [10, 25, 8, 45, 32, 45, 18]

largest = numbers[0]
second_largest = None

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num != largest and (second_largest is None or num > second_largest):
        second_largest = num

print("Largest:", largest)
print("Second Largest:", second_largest)

Output:

Largest: 45
Second Largest: 32
