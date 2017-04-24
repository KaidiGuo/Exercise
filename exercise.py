
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





