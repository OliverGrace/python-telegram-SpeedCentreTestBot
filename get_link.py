def get_link(search, sub3):
    # print(sub3)
    sub_f = []
    a = 0
    is_found = 0
    f = open("sub_found.txt", "w", encoding="GBK", errors="ignore")
    for current in sub3:
        index = current.find('http')
        if search == '':
            return 0
        if (current[0:index].find(search) != -1) or (current[0:index].lower().find(search.lower()) != -1):
            # print('(' + str(a + 1) + ')' + '#' + sub3[a][(sub3[a].find(')') + 2):index])
            # print((sub3[a][index:len(sub3[a])]))
            sub_f.append('(' + str(a + 1) + ')' + '#' + sub3[a][(sub3[a].find(')') + 2):index]+'\n'+(sub3[a][index:len(sub3[a])])+'\n')
            is_found = 1
        a += 1
        if a == len(sub3) and is_found == 0:
            # print('机场没找到')
            f.close()
            return is_found
    f.writelines(''.join(sub_f))
    f.close()
    return is_found




def convert():
    f = open("sub.txt", "r", encoding="UTF-8", errors="ignore")
    sub = f.readlines()
    f.close()
    sub2 = ''.join(sub)
    # print(sub2)     #txt转换完成
    sub3 = sub2.split('\n')  # 分割字符串
    return sub3


def pure_link(sub3):
    # print(sub3)
    a = 0
    sub4 = []
    for current in sub3:
        index = current.find('http')
        sub4.append(sub3[a][index:len(sub3[a])])
        a += 1
    return sub4





