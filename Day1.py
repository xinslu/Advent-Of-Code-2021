with open("input.txt") as input:
    data = input.read().split("\n")
    count = 0
    a = 0
    b = 1
    while b<len(data)-3:
        if (int(data[a])+int(data[a+1])+int(data[a+2])) < (int(data[b])+int(data[b+1])+int(data[b+2])):
            count+=1
        a+=1
        b+=1
    print(count)
