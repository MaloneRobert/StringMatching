import time
import matplotlib.pyplot as plt

# KMP Algorithm string-matching method - prints out the index in the input text where the search pattern was found
# @param pat - the string pattern to search for
# @param txt - the input text to search for the pattern in
def KMPSearch(pat, txt):
    start_time = time.time()
    M = len(pat)    # length of the search pattern
    N = len(txt)    # length of the input string
    lps = [0]*M     # create lps[] that will hold the longest prefix suffix values for pattern matching
    j = 0           # current index for pat[]

    computeLPSArray(pat, M, lps)    # Preprocess the pattern and calculate lps[] array

    i = 0           # current index for txt[]
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1
        if j == M:
            z = str(i-j)
            print("Found pattern at index " + z)
            j = lps[j-1]
        elif i < N and pat[j] != txt[i]:    # mismatch after j matches
                                            # Do not match lps[0..lps[j-1]] characters, as they will match anyway
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    out = time.time() - start_time
    return out
    print("--- string matching took %s seconds ---" % (time.time() - start_time))

# KMP algorithm pattern preprocessing method - builds the lps[] for the search pattern
# @param pat - the search pattern string
# @param M - the length of the search pattern string
# @param lps - the array for holding the lps[] for the search pattern string
def computeLPSArray(pat, M, lps):
    len = 0 # length of the previous longest prefix suffix
    lps[0] # lps[0] is always 0
    i = 1
    while i < M:        # the loop calculates lps[i] for i = 1 to M-1
        if pat[i]== pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len-1]
            else:
                lps[i] = 0
                i += 1

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

    t = KMPSearch(string, x)
    y_hat.append(t/60)

for ni in range(len(n)):
    n[ni] = n[ni] * 2 + 4

plt.plot(n, y_hat)
plt.title("KMP - Time Complexity")
plt.xlabel("Size of string")
plt.ylabel("Time (Minutes)")
plt.show()
