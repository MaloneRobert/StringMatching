import time

# KMP Algorithm string-matching method
# @param pat - the string pattern to search for
# @param txt - the text to search for the pattern in
def KMPSearch(pat, txt):

    M = len(pat)
    N = len(txt)

# create lps[] that will hold the longest prefix suffix values for pattern matching
    lps = [0]*M
    j = 0 # index for pat[]

# Preprocess the pattern and calculate lps[] array
    computeLPSArray(pat, M, lps)

    i = 0 # index for txt[]
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1

        if j == M:
            z = str(i-j)
            print("Found pattern at index " + z)
            j = lps[j-1]

        # mismatch after j matches
        elif i < N and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters, as they will match anyway
            if j != 0:
                j = lps[j-1]
            else:
                i += 1

def computeLPSArray(pat, M, lps):
    len = 0 # length of the previous longest prefix suffix
    lps[0] # lps[0] is always 0
    i = 1

    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pat[i]== pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            # This is tricky. Consider the example: AAACAAAA and i = 7. The idea is similar to search step.
            if len != 0:
                len = lps[len-1]

                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1

txt = "aggcgtatgcgatcctgaccatgcaaaactccagcgtaaatacctagccatggcgacacaaggcgcaagacaggagatgacggcgtttagatcggcgaaatattaaagcaaacgacgatgacttcttcgggaaattagttccctactcgtgtactccaattagccataacactgttcgtcaagatatagggggtcacccatgaatgtcctctaaccagaccatttcgttacacgaacgtatct"
pat = "aggc"

start_time = time.time()

KMPSearch(pat, txt)

print("--- string matching took %s seconds ---" % (time.time() - start_time))
