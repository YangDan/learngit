
# -*- coding:utf-8 _*_

'a test module'

__author__ = 'Michale Liao'

import math
import sys
from PIL import Image



print 'hello,world!'

print ord('A')


t =(1,['A','B'])

classmates = ['dan','bob','lev',['we','all']];

t[1][0]  = 'X'
t[1][1]  = 'Y'

print  t

print   classmates[0]

print  classmates[3][1]


age = 20

if age >= 6:
	print 'your age is',age
	print 'teenager'
elif age >=18:
	print 'your age is',age
	print 'adult'
else:
	print 'your age is',age
	print 'kid'

sum = 0

for x in range(101):
	sum = sum + x
print sum


sum = 0
n=99
while n>0:
	sum = sum + n
	n = n - 2
print sum

birth = int(raw_input('birth: '))
if birth < 2000:
	print 'ok'
else:
	print 'pp'


def myabs(x):
	if x > 0:
		return x
	else:
		return -x

print myabs(-2)



def person (name,age,**kw):

	print 'name:',name, 'age:',age,'other:',kw

person('Dan','24', city = 'beijing',gender ='M',job ='Engineer')

L = []
n = 1
while n <=99:
	L.append(n)
	n = n + 2

print L[-10:]

d = {'a':1,'b':2,'c':3}
for key in d:
	print key
for value in d.itervalues():
	print value

for key,value in d.iteritems():
	print key+str(value)

def is_odd(n):
	return n % 2 == 0

print filter(is_odd,[1,2,3,4,5,6,7,8,9,10,20,11,14,15,16,11])

def fil(n):
	flag = 0
	for i in range(2,int(math.sqrt(n)+1)):
		if n % i == 0:
			flag = 1
			break
	if flag == 1:
		return n
		
print filter(fil,range(1,101))


l = range(1,101)
def delprimenum(str):
	if str == 1:
		return str
	for i in range(2,int(math.sqrt(str)+1)):
		if str%i == 0:
			return str

print filter(delprimenum,l) 

def reserved_cmp(x , y):
	if x > y:
		return -1
	elif x < y :
		return 1
	else :
		return 0

print sorted([36,5,12,9,21],reserved_cmp)


def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
		return ax
	return sum


f=lazy_sum(1,3)
print f()

def count():
	fs = []
	for i in range(1,4):
		def f():
			return i*i
		fs.append(f)
	return fs
f1,f2,f3 = count()

print f1()
print f2()
print f3()


def count():
	fs = []
	for i in range(1,4):
		def f(j):
			def g():
				return j * j 
			return g 
		fs.append(f(i))
	return fs

f1,f2,f3 = count()


print f1()
print f2()
print f3()
 
f = lambda x: x*x
print f
print f(5)

def build(x,y):
	return lambda: x * x + y * y





def log(func):
	def warpper(*args,**kw):
		print 'call %s():' % func.__name__
		return func(*args ,**kw)
	return warpper

def log(text):
	def decorator(func):
		def wrapper(*args,**kw):
			print '%s %s():' % (text,func.__name__)
			return func(*args,**kw)
		return wrapper
	return decorator


@log
def now():
	print '2017-02-15'


@log('hello')
def now():
	print '2017-02-15'


print now.__name__

now()


def test():
	args = sys.argv
	if len(args)==1:
		print 'hello,world'
	elif len(args)==2:
		print 'Hello,%s!' %args[1]
	else:
		print 'Too many arguments!'

if __name__ == '__main__':
	test()


im = Image.open('/Users/yangdan/Downloads/me.jpg')
print im.format,im.size,im.mode

im.thumbnail((200,100))
im.save('/Users/yangdan/Downloads/thumb.jpg','JPEG')











