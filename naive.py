string = 'bbbbbbbaaabasdasdfasda'
x = 'aaab'

def findMatch(string, x):
    for si in range(len(string)):
        xi = 0
        while(string[si] == x[xi]):
            si += 1
            xi += 1
            if(xi == len(x)-1):
                return True
        else:
            continue

print(findMatch(string, x))
