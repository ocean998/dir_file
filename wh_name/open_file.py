f = open('C:\\Users\Administrator\Desktop\表库名称.csv')
dict = {}
for line in f.readlines():
    # print(line)
    dict[line.split(',', 4)[1]] = [line.split(',', 6)[2],line.split(',', 6)[5]]

list = list(dict.keys())

# print(dict)
# print(list)

for id in list:
    name=dict[id][0]
    jb=dict[id][1]
    # 不是×××供电公司或××供电公司的情况
    if name.find('供电公司', 0, len(name)) not in (2,3):
        # print(x)
        str2='id:'+ str(id)+'\t名称错误\t'
        str2=str2.center(22)
        str2=str2+"\t"+ name
        print(str2 )