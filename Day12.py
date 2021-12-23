with open("input12.txt") as input:
    data = input.read().split("\n")[:-1]
    adj = {}
    lower = []
    for i in data:
        key, value = i.split("-")
        if key in adj:
            adj[key].append(value)
        else:
            adj[key] = [value]
        if value in adj:
            adj[value].append(key)
        else:
            adj[value] = [key]
    for i in adj:
        if i.islower() and i!="start" and i!="end":
            lower.append(i)
    def countPaths(s, d, visited, pathCount):
        if not s.isupper():
            visited.add(s)
        if (s == d):
            pathCount[0] += 1
        else:
            for edge in adj[s]:
                if edge not in visited:
                    countPaths(edge, d, visited, pathCount)
        if not s.isupper():
            visited.remove(s)
    pathCount = [0]
    countPaths("start", "end", set(), pathCount)
    print(pathCount[0])
    part1 = pathCount[0]
    def countPathsWithRep(s, d, visited, pathCount,repChar, repCounter):
        if not s.isupper() and s!=repChar:
            visited.add(s)
        if s == repChar and repCounter>=2:
            visited.add(repChar)
        if (s == d):
            pathCount[0] += 1
        else:
            for edge in adj[s]:
                if edge not in visited:
                    if edge!=repChar:
                        countPathsWithRep(edge, d, visited, pathCount, repChar, repCounter)
                    else:
                        countPathsWithRep(edge, d, visited, pathCount, repChar, repCounter+1)
        if not s.isupper() and s!=repChar:
            visited.remove(s)
        if s == repChar and repCounter >= 2:
            visited.remove(repChar)
    sumt = 0
    for i in lower:
        pathCount = [0]
        countPathsWithRep("start", "end", set(), pathCount, i, 0)
        sumt+= abs(part1-pathCount[0])
    print(sumt+part1)
