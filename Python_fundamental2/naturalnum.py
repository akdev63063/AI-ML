n = int(input('Enter Any number : '))
sum = 0
while(n != 0):
    rem = n % 10
    sum = rem + sum
    n /= 10
result = int(sum)
print('Sum of digits: ',result)

