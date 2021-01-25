def minion_game(string):
    # your code goes here
    v = ['A','E','I','O','U']
    s = 0
    k = 0
    for i in range(len(string)):
        if string[i] in v:
            k+= len(string)-i
        else:
            s+= len(string)-i
    if s>k:
        print("Stuart {}".format(s))
    elif k>s:
        print("Kevin {}".format(k))
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)
