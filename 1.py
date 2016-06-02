
a=open('temp.txt','w')#以写模式，打开文件，如果没有该文件，则创建（权限）
a.write('this is my apple')#写入
a.close()#关闭
a=open('temp.txt','r')#以只读模式打开
a.read(50)#读取前50行
a.seek(0)#把游标设置为0--最前面
a=open('temp.txt','w')
a.write('hahjsaj\nshasdh\nhjshja\n1222\n9hs\nhh8')
a.close()
import linecache #help(linecache)
print linecache.getline("temp.txt",1)
print linecache.getline("temp.txt",2)
print linecache.getline("temp.txt",3)
lines=linecache.getlines("temp.txt")
print lines

"""
a='pyer'
b='apple'
# format方式
print 'my name is {0},i love {1}' .format(a,b)
print 'my name is {name},i love {pingguo}' .format(name=a,pingguo=b)
#字典方式
c={a:'pyer',b:'apple'}
print 'my name is' ,c[a] ,',' 'i love', c[b]
print 'my name is %(name)s , i love %(pingguo)s' %{'name':"pyer",'pingguo':"apple"}
print 'my name is %(name)s , i love %(pingguo)s' %{'name':a,'pingguo':b}

"""
#####  print 'my name is %(name)s , i love %(pingguo)s'  % {'name':"pyer",'pingguo':"apple"}