if __name__ == '__main__':
    N = int(input())
    stud_dict = dict()

    for i in range(N):
        a= input().split(' ')
        name = a[0]
        stud_dict[name] = (float(a[1]), float(a[2]), float(a[3]))

    name = input()
    print('%.2f' % (sum(stud_dict[name]) / 3.0))
