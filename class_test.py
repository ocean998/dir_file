class first_test():
    def __init__(self, name):
        self.my_name = name
        self.my_name = self.my_name+' test !'
        self.nm=name
    def pnt_me(self):
        print(self.nm)
        return self.my_name

ft=first_test("tests")
print(ft.pnt_me())


class People:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name  = last_name

    def get_first_name(self):
        return self.first_name

a = People('lala','ouyang')
print(a.get_first_name())
print(a.first_name)


import re
a = 'hello word word word word'
strinfo = re.compile('word')
print(strinfo)
b = strinfo.sub( 'python',a,-1)
print (b)

inputStr = "hello crifan, nihao crifan"
replacedStr = re.sub(r"nihao ", "crifanli", inputStr)
print (replacedStr) #crifanli

x=str.replace("lemon tree", "e", "3", -1)
print(x)