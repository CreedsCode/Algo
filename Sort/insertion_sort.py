input = [15, 2, 43, 17, 4, 8, 47]

for i in range(1, len(input)):
    temp = input[i]

    j = i-1
    while j >= 0 and temp < input[j]:
        input[j+1] = input[j]
        j -= 1
    input[j+1] = temp

print(input)