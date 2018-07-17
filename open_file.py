
import os

path_new = r'D:\__各地市督办核查单\_新核查'


list_dirs = os.walk(path_new)


mould_name = ''
tList=[]
for root, dirs, files in list_dirs:
    # print('root:'+root)
    if root == path_new and len(files) > 0 :
        for f in files:
            if f.find('.doc') > 0:
                tList.append(os.path.join(root,f))


if len(tList) == 1:
    print(tList[0])
else:
    print(path_new+'\  目录下有%s个Word文档:' %len(tList))
    for L in tList:
        print('\t'+os.path.basename(L))


        # if len(files) > 0:
        #     print( files )
        #     print('xx')
        #     print(dirs)


    # for f in files:
    #     fn = os.path.join( root, f )
    #     print(fn)


        # if fn.find( r'__各地市督办核查单\2018' ) > 1 and fn.find( r'\工作核查单' ) > 1:
        #     if os.path.basename( fn ).find(
        #             '核查' ) > 1 and os.path.dirname( fn ).find( '原件' ) > 1:
        #         self.hcd.append( fn )
