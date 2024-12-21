import re
# pattern=re.compile("^[A-Z]+$")
# print(pattern.search("HELLO WORD"))
# print(pattern.search("hello word"))
# print(pattern.search("HELLOWORLD"))
# pattern=re.compile("^[a-z]{3}[0-9]{3,5}.{1}[A-Z]{0,2}")
# print(pattern.search("abs4232@A"))

# pattern="[a-z]"
# matn="bosh joylarni yoqotish"
# replace="_"
# re.sub(pattern,replace,matn)
# print(re.sub(pattern,replace,matn))
# pattern="[a-zA-Z]+"
# matn="bosh joylarni yoqotish"
# result=re.findall(pattern,matn)
# result=''.join(result)
# print(result)
#1
# pattern=re.compile("^[A-za-z0-9]+$")
# print(pattern.search('dadasdasdaq34232'))
#2
# pattern=re.compile("^[a]{1}[b]*$")
# print(pattern.search('abbbb'))
#3
# pattern=re.compile("^[a]{1}[b]*")
# print(pattern.search('abbbbsfsdf'))
#4
# pattern=re.compile("^[a]{1}[b]{0,1}*")
# print(pattern.search('abbbbsfsdf'))
#5
# pattern=re.compile("^[a]{1}[b]{3}")
# print(pattern.search('abbbbsfsdf'))
#6
# pattern=re.compile("^[a]{1}[b]{2,3}*")
# print(pattern.search('abbbbsfsdf'))
#7
# pattern=re.compile("^[A-Z]+[a-z]$")
# print(pattern.search('AZDDSDz'))
#8
# pattern=re.compile("...[@gmail.com]$")
# print(pattern.search("asrorrustamovich007@gmail.com"))
#9
# pattern = re.compile("^\+998\d{9}$")
# print(pattern.search("+998900914478"))
