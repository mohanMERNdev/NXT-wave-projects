N = int(input())
number = 1
counter = 1
sum = 0
while counter <= N:
    square = number ** 2
    sum = square + sum
    number = number + 1
    counter = counter + 1
print(sum)
