from collections import defaultdict
with open("input14.txt") as input:
    data = input.read().split("\n")[:-1]
    template = data[0]
    polymers = data[2:]
    rules = dict()
    for i in polymers:
        k,v = i.split("->")
        rules[k.strip()] = v.strip()
    pairMap = defaultdict(int)
    for i in range(len(template)-1):
        pairMap[template[i:i+2]] += 1
    def part1(string, rules, step):
        if step == 10:
            return string
        newString = ""
        for i in range(len(string)-1):
            if i == 0:
                substring = string[i]+string[i+1]
                if substring in rules:
                    newString += string[i]+rules[substring]+string[i+1]
                else:
                    newString += string[i]+string[i+1]
            else:
                substring = string[i]+string[i+1]
                if substring in rules:
                    newString += rules[substring]+string[i+1]
                else:
                    newString += string[i+1]
        return part1(newString,rules,step+1)

    def part2(pairMap, rules, step):
        if step == 40:
            return pairMap
        for mol, amount in list(filter(lambda x: x[1] > 0, list(pairMap.items()))):
            if mol[:2] not in rules:
                continue
            new_atom = rules[mol[:2]]
            pairMap[mol] -= amount
            pairMap[mol[0]+new_atom] += amount
            pairMap[new_atom+mol[1]] += amount
        return part2(pairMap,rules,step+1)

    result = part1(template,rules,0)
    chars = defaultdict(int)
    for char in result:
        chars[char] += 1
    result = sorted(chars.items(), key=lambda k : k[1])
    print(result[-1][1]-result[0][1])
    result = part2(pairMap,rules,0)
    chars = defaultdict(int)
    for char in result:
        chars[char[1]] += result[char]
    result = sorted(chars.items(), key=lambda k : k[1])
    print(result[-1][1]-result[0][1])


