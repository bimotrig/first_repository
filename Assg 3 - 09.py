total = 0
for num in range(3333, 9999):
  if num % 1234 != 0:
    continue  

  if total > 100000:
    break  

  total += num

print(total)
