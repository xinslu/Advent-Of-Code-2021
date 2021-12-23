with open("input10.txt") as input:
    data = input.read().split("\n")[:-1]
    closing={')':'(','}':'{',']':'[', ">":"<"}
    opening = {v: k for k, v in closing.items()}
    sumt = 0
    sumArray = []
    for i in data:
        corrupted = False
        stack=[]
        scores = {")":3,"]":57,"}":1197,">":25137}
        for c in i:
            if c not in closing:
                stack.append(c)
            else:
                if not stack or stack[-1]!=closing[c]:
                    corrupted = True
                    character = c
                    break
                stack.pop()
        if corrupted:
            sumt += scores[character]
    print(sumt)
    for i in data:
        incomplete = False
        stack=[]
        scores = {")":1,"]":2,"}":3,">":4}
        sumt = 0
        for c in i:
            if c not in closing:
                stack.append(c)
            else:
                if not stack or stack[-1]!=closing[c]:
                    break
                stack.pop()
        else:
            if stack!=[]:
                for i in stack[::-1]:
                    sumt = 5*sumt + scores[opening[i]]
            sumArray.append(sumt)
    print(sorted(sumArray)[len(sumArray)//2])

