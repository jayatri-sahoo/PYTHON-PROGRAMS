3. Find Duplicate Elements in a List
numbers = [10, 20, 30, 20, 40, 10, 50, 30]

duplicates = []

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j] and numbers[i] not in duplicates:
            duplicates.append(numbers[i])

print("Duplicate elements:", duplicates)

Output:

Duplicate elements: [10, 20, 30]
