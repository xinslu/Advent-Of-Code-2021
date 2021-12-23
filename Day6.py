with open("input6.txt") as input:
    data = input.read().split("\n")
    numbers = [int(i) for i in data[0].split(",")]
    memo = {}
    def count(x,days):
        if (x,days) in memo:
            return memo[(x,days)]
        if x>days or (x == 0 and days == 0):
            return 1
        elif x == 0:
            result = count(6, days - 1) + count(8, days - 1)
        else:
            result = count(0, days - x)
        memo[(x,days)] = result
        return result

    def part1():
        result = [count(days, 80) for days in numbers]
        return sum(result)
    def part2():
        result = [count(days, 256) for days in numbers]
        return sum(result)

    print(part1())
    print(part2())
