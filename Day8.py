with open("input8.txt") as input:
    data = input.read().split("\n")
    data = [i.split(" ") for i in data]
    ouputs = [i[11:] for i in data]
    data = [i[:10] for i in data][:-1]
    def part1():
        count = 0
        for i in ouputs:
            for output in i:
                if len(output) == 2 or len(output) == 4 or len(output) == 3 or len(output) == 7:
                    count += 1
        print(count)
    def part2():
        wordOutput = {0: "abcefg", 1: "cf", 2: "acdeg", 3: "acdfg", 4: "bcdf", 5: "abdfg", 6: "abdefg", 7: "acf", 8: "abcdefg", 9: "abcdfg"}
        count = 0
        for index, i in enumerate(data):
            outputsDict = {0: "", 1: "",2: "", 3: "", 4: "", 5: [], 6: [], 7: "", 8: "", 9: ""}
            for output in i:
                if len(output) == 2:
                    outputsDict[1] = output
                elif len(output) == 4:
                    outputsDict[4] = output
                elif len(output) == 3:
                    outputsDict[7] = output
                elif len(output) == 7:
                    outputsDict[8] = output
            for output in i:
                if len(output) != 2 and len(output) != 4 and len(output) != 3 and len(output) != 7:
                        outputsDict[len(output)].append(output)
            for i in outputsDict[5]:
                if len(set(i).intersection(set(outputsDict[1]))) == 2:
                    outputsDict[3] = i
                elif len(set(i).intersection(set(outputsDict[4]))) == 3:
                    outputsDict[5] = i
                else:
                    outputsDict[2] = i
            for i in outputsDict[6]:
                if len(set(i).intersection(set(outputsDict[4]))) == 4:
                    outputsDict[9] = i
                elif len(set(i).intersection(set(outputsDict[7]))) == 3:
                    outputsDict[0] = i
                else:
                    outputsDict[6] = i
            inv_map = {"".join(sorted(v)): k for k, v in outputsDict.items()}
            string = ""
            for j in ouputs[index]:
                string += str(inv_map["".join(sorted(j))])
            count += int(string)
        print(count)
    part1()
    part2()







