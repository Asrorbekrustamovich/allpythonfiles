# f=open("example.txt",mode="r")#read mode
# print(f.read(3))c
# print(f.read())
# f1=open("example.txt",mode="w")#read mode
# print(f.readline())








# data=open("example.txt",mode="a")##avvalgisiga qoshish
# data.write("hello\n")
# data=open("example.txt",mode="a+")##avvalgisiga qoshish va o`qish`
# data.write("assalamualeykum\n")
# data.seek(0)##pointerni 0 ga olib kelib qo`yadi`
# print(data.read())
#1
# f=open("example.txt")
# print(f.read())
#2
# f=open("example.txt")
# print(f.readline())
#3
# data=open("new_file.txt",mode="a+")
# data.write("bu birinchi qator\n")
# data.write("bu ikkinchi qator")
# data.seek(0)
# print(data.readlines())
#5
# data=open("new_file.txt",mode="a+")
# data.seek(0)
# print(len(data.readlines()))
#6
# color = ['Red', 'Green', 'White', 'Black', 'Pink',
# 'Yellow']
# data=open("new_file.txt",mode="a+")
# for i in color:
#     data.write(f"{i}\n")
#7
# data=open("new_file.txt")
# result1=data.readlines()
# for i in result1:
#     for x in i:
#         if(x.isalnum()):
#          print(f"{x}")
#8
# import random
# data=open("new_file.txt")
# result=data.readlines()
# random_line = random.choice(result).strip()
# print(random_line)
#9
# file=open("new_file.txt")
# result=file.read().split()
# print(result)
# dictionary={}
# for word in result:
#     count=0
#     for i in range(len(result)):
#         if(word.lower()==result[i].lower()):
#             count+=1
#     dictionary[word.lower()]=count
# print(dictionary)
#10
# import os
# import string


# for letter in string.ascii_uppercase:
#     filename = f"{letter}.txt"
    

#     if not os.path.exists(filename):
#         with open(filename, "w") as file:
#             file.write("")

# print("Files A.txt to Z.txt have been created.")
#