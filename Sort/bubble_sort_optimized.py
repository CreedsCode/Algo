from asyncio import FastChildWatcher


input = [43, 2, 47, 17, 4, 8, 15]

swapped = True

itteration_count = 0

while(swapped):
    swapped = False
    for i in range(len(input) - itteration_count - 1):
        if input[i] > input[i+1]:
            input[i], input[i+1] = input[i+1], input[i]
            swapped = True

    itteration_count +=1
print (input)