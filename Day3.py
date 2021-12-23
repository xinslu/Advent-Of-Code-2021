with open("input3.txt") as input:
    data = input.read().split("\n")
    oxygenRating = []
    co2rating = []
    index = 0
    while (len(oxygenRating) != 1 or len(co2rating) != 1) and index<len(data[0]):
        hash = {0: [], 1: []}
        if index == 0:
            for i in data:
                if len(i)>1:
                    if i[0] == "0":
                        if 0 in hash:
                            hash[0] += [i]
                        else:
                            hash[0] = [i]
                    else:
                        if 1 in hash:
                            hash[1] += [i]
                        else:
                            hash[1] = [i]
            if len(hash[1]) >= len(hash[0]):
                oxygenRating = hash[1]
                co2rating = hash[0]
            else:
                oxygenRating = hash[0]
                co2rating = hash[1]
            index += 1
        else:
            for i in oxygenRating:
                if i[index] == "0":
                    if 0 in hash:
                        hash[0] += [i]
                    else:
                        hash[0] = [i]
                else:
                    if 1 in hash:
                        hash[1] += [i]
                    else:
                        hash[1] = [i]
            if len(hash[1]) >= len(hash[0]):
                oxygenRating = hash[1]
            else:
                oxygenRating = hash[0]
            hash = {0: [], 1: []}
            for i in co2rating:
                if i[index] == "0":
                    if 0 in hash:
                        hash[0] += [i]
                    else:
                        hash[0] = [i]
                else:
                    if 1 in hash:
                        hash[1] += [i]
                    else:
                        hash[1] = [i]
            if len(hash[1]) >= len(hash[0]):
                co2rating = hash[0]
            else:
                co2rating = hash[1]
            index+=1

        print("Oxygen: ",oxygenRating)
        print("Co2: ",co2rating)
print(int('101000100010',2)*int('010100011001',2))




