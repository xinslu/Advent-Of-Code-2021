with open("input2.txt") as input:
    data = input.read().split("\n")
    horizontal = 0
    vertical = 0
    aim = 0
    for i in data:
        if len(i.split(" "))==2:
            distance=i.split(" ")[1]
            direction=i.split(" ")[0]
            if direction == "forward":
                horizontal += int(distance)
                vertical += aim * int(distance)
            elif direction == "up":
                aim -= int(distance)
            else:
                aim += int(distance)
    print(vertical*horizontal)

