#
# a = [1,2,3]
# b = [23,31,12]
#
# res = {"aa" : a ,"bb":b}
#
# print(res)


temp = [
    {"a" : 1 , "b" : "scva" , "c" :"2022-01-12"},
{"a" : 12, "b" : "dsb" ,"c" :"2022-01-04"},
{"a" : 31 , "b" : "zasc","c" :"2022-01-22"},
{"a" : 331 , "b" : "fdd","c" :"2022-02-12"},
{"a" : 111 , "b" : "dds", "c" :"2022-11-22"},
{"a" : 120 , "b" : "asds" ,"c" :"2022-03-32"},
]

print(type(temp[0]))
print(temp)
res = sorted(temp, key=lambda d: d['a'])
print(res)
res1 = sorted(temp , key=lambda d :d['b'])
print(res1)
res2 = sorted(temp , key=lambda d :d['c'])
print(res2)
