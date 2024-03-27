hap = 0
n = 1234  # Initialize n at the starting value

while n < 4568:
  if n % 444 == 0:
    hap += n
  n += 1

print(hap)