import math

op = [sum, math.prod, min, max,
      lambda ls: ls[0],
      lambda ls: 1 if ls[0] > ls[1] else 0,
      lambda ls: 1 if ls[0] < ls[1] else 0,
      lambda ls: 1 if ls[0] == ls[1] else 0]

with open("input16.txt") as input:
    data = input.read().split("\n")[:-1]
    data = bin(int('1'+data[0], 16))[3:]

def part1(data, startbit):
    index = startbit
    totalVersion = int(data[index:index+3],2)
    typeID = int(data[index+3:index+6],2)
    index += 6
    if typeID == 4:
        while True:
            index += 5
            if data[index-5] == '0':
                break
    else:
        if data[index] == '0':
            endIndex = index + 16 + int(data[index+1:index+16],2)
            index += 16
            while index < endIndex:
                index, version = part1(data, index)
                totalVersion += version
        else:
            number = int(data[index+1:index+12],2)
            index += 12
            for _ in range(number):
                index, version = part1(data,index)
                totalVersion += version
    return index,totalVersion

def part2(data, startbit):
    index = startbit
    totalVersion = int(data[index:index+3],2)
    typeID = int(data[index+3:index+6],2)
    index += 6
    if typeID == 4:
        vals = [0]
        while True:
            vals[0] = 16*vals[0] + int(data[index+1:index+5],2)
            index += 5
            if data[index-5] == '0':
                break
    else:
        vals = []
        if data[index] == '0':
            endIndex = index + 16 + int(data[index+1:index+16],2)
            index += 16
            while index < endIndex:
                index, value = part2(data, index)
                vals.append(value)
        else:
            number = int(data[index+1:index+12],2)
            index += 12
            for _ in range(number):
                index, value = part2(data,index)
                vals.append(value)
    return index, op[typeID](vals)

print(part1(data,0)[1])
print(part2(data,0)[1])
