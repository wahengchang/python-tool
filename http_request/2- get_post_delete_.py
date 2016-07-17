import requests

r = requests.put('http://httpbin.org/put', data = {'key':'value'})
print "#########   put   ###########"
# print r.text
print r.content
r = requests.delete('http://httpbin.org/delete')
print "#########   delete   ###########"
print r.text
r = requests.head('http://httpbin.org/get')
print "#########   head   ###########"
print r.text
r = requests.options('http://httpbin.org/get')
print "#########   options   ###########"
print r.text