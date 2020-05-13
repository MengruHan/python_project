

import requests
import json

url = 'https://faria.devel-02.openapply.com//api/v1/students?auth_token=3e9249b6369374c0f9790f1d5a817d9b&per_page=10'
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

for s in students:
    if s['id'] == 7:
        print(s)

for s in students:
    if s['first_name'] == 'Terry':
        print(s['name'], s['id'], s['email'])



















