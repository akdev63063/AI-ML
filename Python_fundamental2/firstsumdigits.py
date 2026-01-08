n = int(input('Enter any Natural Number: '))
sum = 0
for i in range(1,n+1,1):
    print(i)
    sum += i

print('Sum of all first digits : ',sum)