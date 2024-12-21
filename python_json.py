# import json
# #json to python
# json_obj='[1,true,false,null]'
# python_obj=json.loads(json_obj)
# print(python_obj)
# #python to json
# a={
#     'full_name':'akbar',
#     'age':30,
#     'check1':False,
#     'check_2':True
# }
# j_obj=json.dumps(a)
# print(j_obj)

# #json file to object
# from pprint import pprint
# f= open('counties.json')
# a=json.load(f)
# pprint(a,indent=2)
import json
# a={
#      'full_name':'akbar',
#      'age':30,
#      'check1':False,
#      'check_2':True
#  }
# f= open('test.json',mode='w')
# json.dump(a,f,indent=4)
# a='{ "Name":"David", "Class":"I", "Age":6 }'
# python_obj=json.loads(a)
# print(python_obj)
#4
# import json
# from pprint import pprint

# with open('counties.json') as f:
#     a = json.load(f)
#     for item in a:
#             pprint(item["nationality"], indent=2)
#5
# import json
# from pprint import pprint
# counties = {}

# with open('counties.json') as f:
#     a = json.load(f)  
#     for country in a:
#         country_name = country.get("en_short_name")  
#         area_code = country.get("num_code")          
#         if country_name and area_code:
#             counties[country_name] = area_code  

# pprint(counties) 
#json NBU
data=open()





