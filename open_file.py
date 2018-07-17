import os

path = ''
path_new = ''

def get_path(line):
    ln = str(line)
    x = ln.find('\'')
    y = ln.find('\'', x+1)
    if y > x and x > 10:
        return ln[x+1:y]


if os.path.exists(r'd:\set_path.txt') :
    f = open(r'd:\set_path.txt')
    for line in f.readlines():
        if line[0] == '#':
            print('本行为注释！')
        else:
            if line.find('source') > 3:
                path = get_path(line)
                print(path)

            if line.find('distinct')> 3:
                path_new = get_path(line)
                print(path_new)