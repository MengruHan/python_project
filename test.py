

import requests
import json

url = 'https://faria.openapply.cn/api/v1/students?auth_token=xxxxx'
response = requests.get(url)
print(response) #<Response [200]>
res = response.text
print(res)

students = json.loads(res)
print(students)
students = students.get('students')
print(students)

for s in students:
    print (s['name'],',',s['id'],',',s['email'],',',s['status'])



















