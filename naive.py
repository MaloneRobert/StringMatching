import time
import matplotlib.pyplot as plt

def findMatch(string, x):
    start_time = time.time()
    M = len(x)  # length of the pattern
    N = len(string) # length of the input string

    for si in range(N-M+1):  # si = current input string index
        xi = 0               # xi = current pattern index

        for xi in range(0, M):   #for each index in the pattern

            if(string[si + xi] != x[xi]):
                #if the char at the current index (index of the input string + the pattern index) does not equal the char at the current pattern index, break
                xi = xi - 1     # reduce xi by 1, otherwise it could look like it matched if on final index (break is same as end of loop)
                break

        if(xi == M-1):   #if every index in the pattern matched the indexes in the string, its a match!
            print("match found at " + str(si))

    out = time.time() - start_time
    return out
    print("--- string matching took %s seconds ---" % (time.time() - start_time))

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
    n[ni] = n[ni] * 8 + 5

plt.plot(n, y_hat)
plt.title("Naive Method - Time Complexity")
plt.xlabel("Size of string")
plt.ylabel("Time (Minutes)")
plt.show()
