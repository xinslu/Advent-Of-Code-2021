with open("input9.txt") as input:
    data = input.read().split("\n")
    data = [list(i) for i in data]
    data = data[:-1]
    sumt = 0
    low = {}
    for row, rowI in enumerate(data):
        for col,colI in enumerate(rowI):
            check = True
            if row != 0:
                check = check and data[row][int(col)] < data[int(row)-1][int(col)]
            if int(col) != 0:
                check = check and data[int(row)][int(col)] < data[int(row)][int(col)-1]
            if row != len(data)-1:
                check = check and data[row][col] < data[row+1][col]
            if col != len(data[0])-1:
                check = check and data[row][col] < data[row][col+1]
            if check:
                sumt += 1 + int(data[row][col])
                low[(row,col)] = 1
    print(sumt)
    count = 1
    results = []
    visitedDict = {}
    for key in low:
        rowKey, colKey = key
        def dfs(row,col,visited):
            if row < 0 or col < 0 or row >= len(data) or col >= len(data[0]) or data[row][col] == "9" or (row,col) in visited:
                return 0
            visited[(row,col)] = True
            sumt = 1 + dfs(row+1,col,visited) + dfs(row,col+1,visited) + dfs(row-1,col,visited) + dfs(row,col - 1,visited)
            return sumt
        results.append(dfs(rowKey,colKey,visitedDict))
        results = sorted(results)
    print(results[-1]*results[-2]*results[-3])




