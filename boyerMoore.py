import time
import matplotlib.pyplot as plt

def generateBadMatchTable(x):
    t = [0] * len(x)
    for i in range(len(x)):
        if(len(x) - i - 1 is not 0):
            t[x.index(x[i])] = len(x) - i - 1
        else:
            t[x.index(x[i])] = 1
    t[len(x)-1] = len(x)
    return t

def preprocessStrongSuffix(shift, bpos, x, m):
    i=m
    j=m+1
    bpos[i] = j
    while(i>0):
        while(j<=m and x[i-1] != x[j-1]):
            if(shift[j] == 0):
                shift[j] = j-1
            j = bpos[j]
        i -= 1
        j -= 1
        bpos[i] = j

def preprocess_case2(shift, bpos, x, m):
    j = bpos[0]
    for i in range(0, m):
        if(shift[i] == 0):
            shift[i] = j
        if(i == j):
            j = bpos[j]

def findMatch(string, x):
    start_time = time.time()
    badMatch = generateBadMatchTable(x)
    shift = [0] * (len(x) + 1)
    bpos = [0] * (len(x) + 1)
    preprocessStrongSuffix(shift, bpos, x, len(x))
    preprocess_case2(shift, bpos, x, len(x))

    i = 0
    counter = 0
    while(i < len(string) - len(x) + 1):
        j = len(x)
        counter += 1
        while(j > 0 and x[j-1] == string[i+j-1]):
            j -= 1
        if(j > 0):
            if(string[i+j-1] in x):
                b = badMatch[x.index(string[i+j-1])]
                s = shift[j]
                if(b > s):
                    i += b
                else:
                    i += s
            else:
                i += badMatch[len(x)-1]
        else:
            print("Match at " + str(counter))
            i += len(x)-1
    out = time.time() - start_time
    return out

# ----------------------------------

n = [10, 100, 1000, 10000, 100000, 500000, 1000000]
y_hat = []

for ni in range(len(n)):
    part = 'colorado'
    string = ''
    x = 'state'
    for i in range(n[ni]):
        string = string + part
    string = string + x

    t = findMatch(string, x)
    y_hat.append(t/60)

for ni in range(len(n)):
    n[ni] = n[ni] * 2 + 4

plt.plot(n, y_hat)
plt.title("Boyer-Moore - Time Complexity")
plt.xlabel("Size of string")
plt.ylabel("Time (Minutes)")
plt.show()
