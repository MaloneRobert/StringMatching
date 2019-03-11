import time

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

# ----------------------------------------

txt = "aggcgtatgcgatcctgaccatgcaaaactccagcgtaaatacctagccatggcgacacaaggcgcaagacaggagatgacggcgtttagatcggcgaaatattaaagcaaacgacgatgacttcttcgggaaattagttccctactcgtgtactccaattagccataacactgttcgtcaagatatagggggtcacccatgaatgtcctctaaccagaccatttcgttacacgaacgtatct"
pat = "aggc"

runs = 10
i = 0

while(i < runs):
    KMPSearch(pat, txt)
    i += 1
