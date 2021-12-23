with open("input11.txt") as input:
    data = input.read().split("\n")[:-1]
    data = [[int(j) for j in i] for i in data]
    countt = 0
    def dfs(data,row,col,visited):
        if row < 0 or col < 0 or row >= len(data) or col >= len(data[0]) or (row,col) in visited:
            return 0
        if data[row][col] > 9:
            visited[(row,col)] = True
            dfs(data,row+1,col, visited)
            dfs(data,row-1,col, visited)
            dfs(data,row,col+1, visited)
            dfs(data,row,col-1, visited)
            dfs(data,row+1,col-1, visited)
            dfs(data,row+1,col+1, visited)
            dfs(data,row-1,col+1, visited)
            dfs(data,row-1,col-1, visited)
        else:
            data[row][col] += 1
            if data[row][col] > 9:
                dfs(data,row,col, visited)
    for i in range(100):
        visited = {}
        for row in range(len(data)):
            for col in range(len(data[0])):
                data[row][col] += 1
                if data[row][col] > 9:
                    dfs(data,row,col, visited)
        for row in range(len(data)):
            for col in range(len(data[0])):
                if data[row][col] > 9:
                    countt += 1
                    data[row][col] = 0
    print(countt)
    step = 1
    flashes = True
    while True:
        visited = {}
        for row in range(len(data)):
            for col in range(len(data[0])):
                data[row][col] += 1
                if data[row][col] > 9:
                    dfs(data,row,col, visited)
        for row in range(len(data)):
            for col in range(len(data[0])):
                if data[row][col] > 9:
                    data[row][col] = 0
        if len(visited) == 100:
            print(step+100)
            break
        step +=1

