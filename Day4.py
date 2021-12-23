import sys
with open("input4.txt") as input:
    data = input.read().split("\n")
    numbers = data[0].split(",")
    bingoTickets = []
    board = []
    found = False
    for i in data[2:]:
        if i == "":
            bingoTickets.append(board)
            board = []
        else:
            i = i.strip()
            board += [i.split()]
    counter = 0
    foundCounter = [0 for i in range(100)]
    for i in numbers:
        for boardNumber, board in enumerate(bingoTickets):
            for x, line in enumerate(board):
                for y, number in enumerate(line):
                    if number == i:
                        board[x][y] = int(board[x][y])
        counter+=1
        if counter>=5:
            for boardNumber, board in enumerate(bingoTickets):
                for col in range(5):
                    for row in range(5):
                        if type(board[row][col]) != int:
                            break
                    else:
                        foundCounter[boardNumber] = 1
                        try:
                            foundCounter.index(0)
                        except:
                            sumt = 0
                            for i in bingoTickets[boardNumber]:
                                for number in i:
                                    if type(number) != int:
                                        sumt += int(number)
                            print(sumt*int(numbers[counter-1]))
                            sys.exit(0)
                        break
            for boardNumber, board in enumerate(bingoTickets):
                for x, line in enumerate(board):
                    for y, number in enumerate(line):
                        if type(number) != int:
                            break
                    else:
                        foundCounter[boardNumber] = 1
                        try:
                            foundCounter.index(0)
                        except:
                            sumt = 0
                            for i in bingoTickets[boardNumber]:
                                for number in i:
                                    if type(number) != int:
                                        sumt += int(number)
                            print(sumt*int(numbers[counter-1]))
                            sys.exit(0)
                        break
        if found:
            break



