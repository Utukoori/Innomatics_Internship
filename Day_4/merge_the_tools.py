def merge_the_tools(string, k):
    # your code goes here
    n = len(string)
    for x in range(0, n, k):
        slicedStr = string[x : x+k]
        uni =[]
        for y in slicedStr:
            if y not in uni:
                uni.append(y)
        print (''.join(uni))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
