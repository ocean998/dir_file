import os

#path = 'C:/Users/Administrator/Desktop'
path = r'D:\__各地市督办核查单'

os.chdir(r'D:\__各地市督办核查单')

dq={'杭州':'01','嘉兴':'02','绍兴':'03','金华':'04','宁波':'05',
    '台州':'06','丽水':'07','湖州':'08','衢州':'09','温州':'10','舟山':'11'}

class Doc_name():
    def __init__(self,path,xflb):
        self.pt=path
        list_dirs = os.walk(self.pt)
        self.dbd=[]
        self.hcd=[]
        self.lb=xflb

        for root, dirs, files in list_dirs:
            for f in files:
                fn=os.path.join(root, f)
                if fn.find(r'__各地市督办核查单\2018') > 1 and fn.find(r'\工作核查单') > 1:
                    self.hcd.append(os.path.basename(fn))

                if fn.find(r'__各地市督办核查单\2018') > 1 and fn.find(r'\工作督办单') > 1:
                    self.dbd.append(os.path.basename(fn))


    def get_name_list(self):
        if str(self.lb).find('核查') > 0:
            return self.dbd
        else:
            return self.hcd
    #end of def __init__(self):


    #
    # print('****************************')
    # for n in dbd:
    #     if n.find('DB08') > 1:
    #         print('工作督办单 : %s' %n)


test=Doc_name(path, '核查')
x=test.get_name_list()
for n in x:
    # print('核查单 : %s' %n)
    if n.find('-08-') > 1:
        print('核查单 : %s' %n)
