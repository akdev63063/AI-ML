num = int(input('Enter any number: '))
count = 1

while(count <= 10):
    if count % 2 == 0:
        count += 1   # increment to avoid infinite loop
        continue
    print(count)
    count += 1
