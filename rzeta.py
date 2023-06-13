# This program estimates the value of the Riemann Zeta function for a given value of s and a given number of summations.

total = 0

sums = int(input("Enter the number of summations: "))
s = int(input("Enter the value of s: "))

for n in range(0, sums):
  total += 1/((n+1)**(s))

print(total)
