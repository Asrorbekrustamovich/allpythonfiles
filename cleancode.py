#1
# y=8
# x=lambda a:a*y
# print(x(6))
#2
# sum(2,4,6)
# print(sum([1,2,3]))
#3
# def foo(k):
#     k=[1]
# q=[0]
# print(foo(q))
# print(q)
#4
# a={1:"A",2:"B",3:"C"}
# print(a.get(1,4))
#5
# def m(f,v):
#     return f(f(v))
# def func(n):
#     return n*n
# print(m(func,3))
#6
# def foo(fname,value):
#     print(fname(value))
# foo(max,[1,2,3])
# foo(min,[1,2,3])
#7
# def func(value1,list1=[]):
#     list1.append(value1)
#     return list1
# a=func(1)
# b=func(2,[])
# c=func(3)
# print(a,b,c)
#8
# fruits=["apple","banana","cherry"]
# newlist=[x for x in fruits if "a" in x]
# print(newlist)
#9
# def generator(num,power):
#     for i in range(num):
#         yield i**power
# a=generator(3,4)
# for i in a:
#    print(i)
#10
numbers=[-1,-2,3,4,5,-5]
has_positives=any(n>0 for n in numbers)
print(has_positives)
