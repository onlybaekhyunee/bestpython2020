import json
""" 
2020-4-3
JSON反序列化、序列化 
json.load json.dump与文件有关
"""
name = input('请输入姓名：')
age = input('请输入年龄：')
hobby = input('请输入爱好：')
json_str = '[{"name":"'+str(name)+'","age":'+str(age)+',"hobby":"'+str(hobby)+'"},{"name":"Willbur","age":3,"hobby":"sleep"}]'
get_json = json.loads(json_str)
print(type(get_json))
for j in get_json:
    print(type(j))
    print('Name is '+j['name']+'.Age is '+str(j['age'])+'.Hobby is '+j['hobby']+'.')
    j['cansing?'] = False
    print(j)
    create_json = json.dumps(j)
    print(create_json)
c_json = json.dumps(get_json)
print(c_json)


