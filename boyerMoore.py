string = 'aabaacaadaabaaba'
x = 'aaba'

def generateBadMatchTable(x):
    t = [0] * len(x)
    for i in range(len(x)):
        if(len(x) - i - 1 is not 0):
            t[x.index(x[i])] = len(x) - i - 1
        else:
            t[x.index(x[i])] = 1
    t[len(x)-1] = len(x)
    return t

def findMatch(string, x):
    badMatch = generateBadMatchTable(x)

    i = 0
    while(i < len(string) - len(x) + 1):
        j = len(x)
        while(j > 0 and x[j-1] == string[i+j-1]):
            j -= 1
        if(j > 0):
            if(string[i+j-1] in x):
                i += badMatch[x.index(string[i+j-1])]
            else:
                i += badMatch[len(x)-1]
        else:
            print("Match at " + str(i))
            i += len(x)-1

findMatch(string, x)
