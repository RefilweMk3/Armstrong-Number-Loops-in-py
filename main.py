n = int(input("Enter a number: "))
y = 0

x = n
while x > 0:
   digit = x % 10
   y += digit ** 3
   x //= 10

if n == y:
   print(n,"is an Armstrong number")
else:
   print(n,"is not an Armstrong number")
