with open("input5.txt") as input:
    data = input.read().split("\n")
    for index,i in enumerate(data[:-1]):
        data[index] = [i.split()[0].split(",")]+[i.split()[2].split(",")]
    board =  [[0 for i in range(1000)]for j in range(1000)]
    counter = 0
    for start, end in data[:-1]:
        rowStart= int(start[0])
        columnStart = int(start[1])
        rowEnd = int(end[0])
        columnEnd = int(end[1])
        if rowStart == rowEnd:
            for column in range(min(columnStart, columnEnd), max(columnStart, columnEnd)+1):
                board[rowStart][column] += 1
        if columnStart == columnEnd:
            for row in range(min(rowStart, rowEnd), max(rowStart, rowEnd)+1):
                board[row][columnStart] += 1
        else:
            # print("burh")
            endCol = max(columnStart, columnEnd)+1
            startRow =  rowStart if max(columnStart, columnEnd) == columnStart else rowEnd
            startCol = columnStart if startRow == rowStart else columnEnd
            endRow = max(rowStart, rowEnd)+1
            if abs((columnStart - columnEnd)/(rowEnd - rowStart)) == 1.0:
                print("bruh")
                while endCol <= endCol:
                    print("bruh")
                    board[startRow][startCol] += 1
                    startRow += int(columnStart - rowStart)/(columnStart - columnEnd)

    for row in range(1000):
        for column in range(1000):
             if board[row][column] >= 2:
                counter+=1
    print(counter)
