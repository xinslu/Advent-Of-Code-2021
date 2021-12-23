import numpy as np
with open("input13.txt") as input:
    data = input.read().split("\n")[:-1]
    points = []
    folds = []
    maxx = 0
    maxy = 0
    for i in data:
        if len(i.split(","))==2:
            points.append([int(i.split(",")[0]),int(i.split(",")[1])])
            maxx = max(maxx,int(i.split(",")[0]))
            maxy = max(maxy,int(i.split(",")[1]))
        elif len(i)>1:
            fold = i.split("=")
            if fold[0][-1] == "x":
                folds.append([int(fold[1]),0])
            else:
                folds.append([0,int(fold[1])])
    matrix = np.zeros((maxy+1, maxx+1))
    for x,y in points:
        matrix[y][x] = 1
    for x,y in folds:
        if x!=0:
            temp = matrix[:,x+1:]
            newArray = matrix[:,:x]
            if temp.shape[1] < newArray.shape[1]:
                temp = np.concatenate((temp, np.zeros((894,newArray.shape[1]-temp.shape[1]))),axis=1)
            elif temp.shape[1] > newArray.shape[1]:
                newArray = np.concatenate((newArray, np.zeros((894,temp.shape[1]-newArray.shape[1]))),axis=1)
            temp = np.flip(temp,1)
            temp2 = np.add(temp,newArray)
            matrix = temp2
        if y!=0:
            temp = matrix[y+1:,:]
            newArray = matrix[:y,:]
            if temp.shape[0] < newArray.shape[0]:
                temp = np.concatenate((temp, np.zeros((newArray.shape[0]-temp.shape[0],temp.shape[1]))),axis=0)
            elif temp.shape[1] > newArray.shape[1]:
                newArray = np.concatenate((newArray, np.zeros((temp.shape[0]-newArray.shape[0],temp.shape[1]))),axis=0)
            temp = np.flip(temp,0)
            temp2 = np.add(temp,newArray)
            matrix = temp2
    countt = 0
    for rows in matrix:
        for cols in rows:
            if cols>=1:
                countt+=1
    matrix = matrix.tolist()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] >= 1:
                matrix[i][j] = "X"
            else:
                matrix[i][j] = " "
    for rows in matrix:
        print(*rows)



