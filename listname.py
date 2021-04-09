def listname():
    f = open("sub.txt", "r", encoding="UTF-8", errors="ignore")
    sub = f.readlines()
    f.close()
    sub2 = ''.join(sub)
    subf = []
    sub3 = sub2.split('\n')  # 分割字符串
    a = 0
    for current in sub3:
        index = current.find('http')
        # print('(' + current[0:index].ljust(10), end=' ')
        subf.append('(' + current[0:index].ljust(10)+' ')
        a += 1
        if a % 3 == 0:
            # print('\n')
            subf.append('\n')
    return ''.join(subf)
