import os
import re
import shutil

# path = 'C:/Users/Administrator/Desktop'
path = r'D:\__各地市督办核查单'

os.chdir(r'D:\__各地市督办核查单')

dq = {'杭州': '01', '嘉兴': '02', '绍兴': '03', '金华': '04', '宁波': '05',
      '台州': '06', '丽水': '07', '湖州': '08', '衢州': '09', '温州': '10', '舟山': '11'}


# 列出在目录 ×××__各地市督办核查单\2018×××\ ××\..\ 下面的文件名为 工作核查单***.xxx 的文件
# 列出在在目录 ×××__各地市督办核查单\2018×××\ ××\..\ 下面的文件名为 工作督办单***.xxx   的文件


class Doc_name():
    def __init__(self, path, xflb):
        self.pt = path
        list_dirs = os.walk(self.pt)
        self.dbd = []
        self.hcd = []
        self.lb = xflb

        for root, dirs, files in list_dirs:
            # print(root)
            # print(dirs)
            # print(files)
            # print('_________________')
            for f in files:
                fn = os.path.join(root, f)
                if fn.find(r'__各地市督办核查单\2018') > 1 and fn.find(r'\工作核查单') > 1:
                    if os.path.basename(fn).find(
                            '核查') > 1 and os.path.dirname(fn).find('原件') > 1:
                        self.hcd.append(fn)
                        print(fn)

                if fn.find(r'__各地市督办核查单\2018') > 1 and fn.find(r'\工作督办单') > 1:
                    if os.path.basename(fn).find(
                            '督办') > 1 and os.path.dirname(fn).find('原件') > 1:
                        self.dbd.append(os.path.basename(fn))

    def get_name_list(self):
        if str(self.lb).find('核查') > 0:
            return self.dbd
        else:
            return self.hcd


class where_storing():
    # base：要生成文件的基础目录，db_hc：督办单，核查单
    def __init__(self, base, db_hc):
        self.basedir = base
        if str(db_hc).find('') >= 0:
            self.lb = 'dbd'
        else:
            self.lb = 'hcd'

        # 在基础目录中查找 哪些地市需要生成督办 或核查 单
        dq = {
            '杭州': '01',
            '嘉兴': '02',
            '绍兴': '03',
            '金华': '04',
            '宁波': '05',
            '台州': '06',
            '丽水': '07',
            '湖州': '08',
            '衢州': '09',
            '温州': '10',
            '舟山': '11'}
        list_dirs = os.walk(self.basedir)

        self.storing_dir = []
        for root, dirs, files in list_dirs:
            if os.path.basename(root) in dq:
                self.storing_dir.append(
                    root + '=' + dq[os.path.basename(root)])

    def get_dest_dir(self):
        print('\n**********要生成的核查单目录***********\n')
        p = re.compile('=[0-9]{2}')

        self.dest_dirs = []
        for x in self.storing_dir:
            pp = p.search(x)
            self.dest_dirs.append(x[0:pp.span()[0]])
            print(x[0:pp.span()[0]])
            pp = p.search(x).group(0)
            pp = pp[1:3]
            if
        return self.dest_dirs


# 根据文件名列表 计算新的文件名


def get_new_fname(old_fn, new_path):
    # p 定义要匹配的正则表达式条件
    p = re.compile(r'([0-9]{4}).([0-9]{2}).([0-9]{3})')
    old_s = old_fn
    # 取出第三个匹配的，为文件序号
    xh = p.search(old_s).group(3)

    # 序号+1 生成3位的新序号
    if int(xh) + 1 < 10:
        new_s = '00' + str(int(xh) + 1)
    elif int(xh) + 1 < 100:
        new_s = '0' + str(int(xh) + 1)
    else:
        new_s = str(int(xh) + 1)
    new_s = old_s.replace(xh, new_s)
    new_s = str(new_path) + '\\' + os.path.basename(new_s)
    # print(old_s + '\nrename to  \n' + new_s)
    return new_s


test = Doc_name(path, '核查')
x = test.get_name_list()
y = []
for n in x:
    # print('核查单 : %s' %n)
    if n.find('-08-') > 1:
        y.append(n)

y.sort(reverse=True)
print('*******************')
print(y[0])

fn = get_new_fname(y[0], 'D:\__各地市督办核查单\_新核查')
print(fn)
shutil.copyfile(y[0], fn)

newdir = where_storing(r'D:\__各地市督办核查单\_新核查', '核查单')
new_dir = newdir.get_dest_dir()
for d in new_dir:
    print(d)
