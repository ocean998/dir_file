import re
import os

# p = re.compile(r'(\d+)-(\d+)-(\d+)')
# print(p.match('2018-08-002').group(2))
# '工作核查单（JL2018-08-004）-湖州.doc'
def get_new_fname (old_fn):
    # p 定义要匹配的正则表达式条件
    p = re.compile(r'([0-9]+).([0-9]+).([0-9]+)')
    old_s= old_fn
    # 取出第三个匹配的，为文件序号
    xh=p.search(old_s).group(3)

    # 序号+1 生成3位的新序号
    if int(xh)+1 <10 :
        new_s = '00'+str(int(xh)+1)
    elif int(xh)+1<100:
        new_s = '0'+str(int(xh)+1)
    else:
        new_s = str(int(xh)+1)
    # new_s = old_s.replace(xh,new_s)
    # print(old_s + '\nrename to  \n' + new_s)
    new_s = '-'+new_s
    new_s = re.sub(r'-([0-9]{3})', new_s,old_s)
    return  new_s
fn = get_new_fname('工作核查单（JL2018-08-004）-湖州.doc')
print(fn)

srcDir = r'D:\2_TDDOWNLOAD\0703021\babes.1.alexis.crystal.and.vicky.love.silent.musings.mp4'
dstDir = r'D:\2_TDDOWNLOAD\0703021\love6699.mp4'

try:
    os.rename(srcDir,dstDir)
except Exception as e:
    print (e)
    print ('rename dir fail\n')
else:
    print ('rename dir success\n')

#
#
# s=re.sub(r'-([0-9]{3})','-xxx','工作核查单（JL2018-08-003）.docx')
# print(s)
#
# old_s='工作核查单（JL2018-003-003）.docx'
# s=old_s.replace('003','004')
# print(s)