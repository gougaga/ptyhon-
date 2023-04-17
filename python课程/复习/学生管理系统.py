list1 = []
def stu_jm():
    print('''
    ---------菜单----------
    1.添加功能
    2.删除功能
    3.查询功能
    4.展示功能
    5.修改功能
    -----------------------
    ''')


def stu_add():
    print('欢迎来到信息添加页面')
    name = input('请输入名字：')
    age = int(input('请输入年龄：'))
    gender = input('请输入性别：')
    for i in list1:
        if i['name'] == name and i['age'] == age and i['gender'] == gender:
            print('学生已经存在')
            return
    dict1 = {}
    dict1['name'] = name
    dict1['age'] = age
    dict1['gender'] = gender
    list1.append(dict1)


def stu_delete():
    print('进入删除页面')
    num = int(input('请输入需要删除的序号:'))
    if 0 <= num <= len(list1)-1:
        shuru = input('是否要删除该数据？（yes/no）')
        if shuru == 'y' or shuru == 'yes':
            del list1[num]
            print('删除成功')
        elif shuru == 'n' or shuru == 'no':
            print('取消删除')
        else:
            print('输入错误')
    else:
        print('输入序号不正确')


def stu_show():
    for i, j in enumerate(list1):
        print('序号%d 姓名%s 年龄%d 性别%s' % (i, j['name'], j['age'], j['gender']))

def stu_updata():
    print('------------欢迎来到修改信息页面--------------')
    stu_show()
    print('---------以上是所有学生信息-------------------')
    num = int(input('请输入需要更改信息的学生序号：'))
    if 0 <= num <= len(list1)-1:
        list1[num]['name'] = input('请输入修改后的姓名：')
        list1[num]['age'] = int(input('请输入修改后的年龄：'))
        list1[num]['gender'] = input('请输入修改后的性别：')
        print('修改成功')
        print(list1[num])
    else:
        print('请输入正确序号')


def stu_find():
    print('------欢迎来到查询信息页面----------')
    name = input('请输入需要查找的学生姓名：')
    for i in list1:
        if i['name'] == name:
            print(i)
        else:
            print('该学生不存在')


def main():
    while True:
        stu_jm()
        num = int(input('请输入需要的功能：'))
        if num == 1:
            stu_add()
        if num == 2:
            stu_delete()
        if num == 3:
            stu_find()
        if num == 4:
            stu_show()
        if num == 5:
            stu_updata()

if __name__ == '__main__':
    main()