a = ['张三',  '张四', '张五', '王哈']
for i in a:
    if '张' in i:
        a.remove(i)
print(a)
del a[0]
print(a)

