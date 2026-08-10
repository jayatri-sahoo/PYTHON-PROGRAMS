5. Find the Missing Number

Given numbers from 1 to n, one number is missing.

numbers = [1, 2, 3, 5, 6, 7, 8]

n = 8

expected_sum = n * (n + 1) // 2

actual_sum = 0

for num in numbers:
    actual_sum += num

missing = expected_sum - actual_sum

print("Missing number:", missing)

Output:

Missing number: 4
