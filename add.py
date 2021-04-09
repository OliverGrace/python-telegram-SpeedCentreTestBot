from get_link import convert
from random import*

sub3 = convert()
def add_node(name, link):
    sub3 = convert()
    a = len(sub3)
    sub_file = open('sub.txt', 'a+', encoding="UTF-8", errors="ignore")
    sub_file.writelines('\n' + str(a + 1) + ')' + ' ' + name + ' ' + link)
    sub_file.close()
    return '\n' + str(a + 1) + ')' + ' ' + name + ' ' + link


def random(num):
    r_list = ''
    count = 0
    if num == '':
        r = randint(0, len(sub3) + 1)
        r_list = sub3[r]
        print(r_list)
    else:
        num = int(num)
        while count < num:
            r = randint(0, len(sub3) + 1)
            count += 1
            r_list = r_list + sub3[r]+'\n'

    return r_list



