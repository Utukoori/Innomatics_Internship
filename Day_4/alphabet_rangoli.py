def print_rangoli(size):
    # your code goes here
    from string import ascii_lowercase
    pattern = []
    for i in range(size):
        s = "-".join(ascii_lowercase[i:size])
        pattern.append((s[::-1]+s[1:]).center(4*size-3,"-"))
    print('\n'.join(pattern[:0:-1]+pattern))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
