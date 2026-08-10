4. Check Whether a Number Is an Armstrong Number
num = 153

original = num
sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit ** 3
    num = num // 10

if sum == original:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

Output:

Armstrong Number

Try changing 153 to 370, 371, or 123.
