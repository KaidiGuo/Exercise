
def arrayPairSum_561(input):
    #input1 = [1,4,2,3]
    print sum(sorted(input)[::2])

def hammingDistance_461(x, y):
    # str1 = bin(x)[2:]
    # str2 = bin(y)[2:]
    # count = 0
    # longer = max(str1, str2)
    # shorter = min(str1, str2)
    # shorter = shorter.zfill(len(longer))
    #
    # for i in range(len(longer)):
    #
    #     if longer[i] != shorter[i]:
    #         count += 1
    # return count
    return bin(x^y).count('1')

def reverseWords_557(s):
    # re = ""
    # for i in range(len(s)-1, -1, -1):
    #     re += s[i]
    # return re
    #thislist = list(s)
    # re = "".join(list(s)[::-1])
    # return re
    words = s.split(" ")
    revers = map(lambda x:x[::-1], words)
    re = " ".join(revers)
    return re

def findComplement_476(num):
    b = bin(num)[2:]
    c = ""
    for i in b:
        if i == "0":
            c += "1"
        else:
            c += "0"
    out = int(c,2)
    return out


def findWords_500( words):
    line1, line2, line3 = set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')
    ret = []
    for word in words:
        w = set(word.lower())
        if w.issubset(line1) or w.issubset(line2) or w.issubset(line3):
            ret.append(word)
    return ret

def fizzBuzz_412( n):
    numbers = []
    for i in range(n):
        if (i+1)%3 == 0 and (i+1)%5 == 0:
            numbers.append("FizzBuzz")
        elif (i+1)%3 == 0:
            numbers.append("Fizz")
        elif (i+1)%5 == 0:
            numbers.append("Buzz")
        else:
            numbers.append(str(i+1))
    return numbers



def reverseString_344(s):
    re = s[::-1]
    return re

def islandPerimeter_463(grid):
    count = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == 1:
                if x > 0 and grid[x-1][y] == 1:
                    count += 0
                else:
                    count += 1
                if y > 0 and grid[x][y-1] == 1:
                    count += 0
                else:
                    count += 1
                if x +1 < len(grid) and grid[x+1][y] == 1:
                    count += 0
                else:
                    count += 1
                if y +1 < len(grid[0]) and grid[x][y+1] == 1:
                    count += 0
                else:
                    count += 1
    return count

test = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
print islandPerimeter_463(test)
