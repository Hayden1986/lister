a=[1,2,3]
a[-1]
b=[[1,2,3],[4,5,6]]
b
b[0]
b[0][0]
b[1][0]
b[1][1]
#列表赋值，列表对象是可变的，类型也是可变的
b[0][1]=7
b[1][1]='a'
b
d=[1,2,3,4,5,6,7]
#列表切片
d[0:4:1] #从左开始取数
#从右开始取数
d[-1:-4:-1]
d
#添加操作
#+ 生成一个新的列表
a+b
#  Extand接受参数并将该参数中的每个元素都添加到原油的列表中，不改变id
a=[1,2,3]
b=[4,5,6]
id(a)
a.extend(b)
id(a)
a
#  append 将任意对象添加到列表的末端
c=[1,1,1,1,1]
a.append(c)
c.append(4)
# insert 在列表任意位置插入对象
a=[1,2,3]
a.insert(2,0)
a=[1,2,3]
a.insert(a[0],0)
a

## 修改列表 --直接赋值即可
##删除操作
#del 通过索引删除指定位置的元素
#remove 移除列表中指定位置的第一个匹配值，无法匹配则报错
#pop 返回最后一个元素，并从list中删除
a=[1,2,3,0,0,0,0,1000,999]
del a[1]
a.remove(0)
a=[1,2,3,0,0,0,0,1000,999]
a.pop(0)
a.pop()
##列表成员关系 返回一个布尔值
a=[0,1,1,2,'a',4]
2 in a 
5 in a
###列表推导式
[x for x in range(1,101) if x>20]
range(1,101)[x for x in range(1,101) if x>20]
[x for x in range(1,11)]
####；列表/翻转排序
###排序sort
a=[3,2,4,1]
b=a.sort()
print b  ####结果为None
###翻转 序列 reverse
c=a.reverse()
print c ####结果为None
##################################
a=[1,2,3,4,5,333,11,44]
print a[3:6]
##########
a=[1,2,3]
b=[4,5,6]
c=a+b
print c
a.extend(b)
a.insert(b[0:2],2)
a=[1,99,33,44,55,22]
a.insert(a[0],2)
a.append((11,33,54))#####  1 
a.insert(a[0],2)
a.insert(3,101)########    2
#############################











