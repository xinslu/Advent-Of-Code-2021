import numpy as np
with open("input7.txt") as input:
    data = input.read().rstrip("\n").split(",")
    numbers = [int(i) for i in data]
    def part1():
        median = int(np.median(numbers))
        sumt = 0
        for i in numbers:
            sumt += abs(median - i)
        print(sumt)
    def part2():
        mean = int(np.mean(numbers))
        num1 = sum([abs(i-mean-1)*(abs(i-mean-1)+1)/2 for i in numbers])
        num2 = sum([abs(i-mean)*(abs(i-mean)+1)/2 for i in numbers])
        print(int(min(num1,num2)))
    part1()
    part2()
