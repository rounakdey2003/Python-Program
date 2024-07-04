low = int(input("Enter the lower limit: "))
upp = int(input("Enter the upper limit: "))
print("\nThe prime numbers within ",low," and ",upp," ....\n\n")
for i in range(low,upp):
  flag = 0
  for j in range(2,i-1):
    if (i % j) == 0:
      flag = 1
      break
  if flag == 0:
    print("\b  ",i)