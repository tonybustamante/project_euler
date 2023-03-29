div = 0 
count = 1 
i = 0
j = 0 

while div <= 500: 
    i = count
    
    sum=1
    while i > 0: 
      sum += i
      i -= 1

    count += 1
    div += 1
    j = 1 
    print(sum, end=': ')
    div = 0

    while j <= sum: 
        if sum % j == 0: 
          div += 1 
        if j*j == sum:
          break
        if j > (sum / 2): 
          break
        j+=1
    div += 1
    print(" | Divisors", div)
    print('\n') 
