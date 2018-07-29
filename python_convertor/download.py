# coding=utf-8
#!/usr/bin/python
import sys
import json
import requests
import codecs
from io import open
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class Replacement(object):



    def __init__(self, replacement):

        self.replacement = replacement

        self.matched = None

        self.replaced = None



    def __call__(self, match):

        self.matched = match.group(0)

        self.replaced = match.expand(self.replacement)

        return self.replaced

repl = Replacement("<strong>\\1</strong>")

url = 'https://integdocs.experium.ru/index.php/Experium_RESTful_Web_Service'
url1 = 'https://integdocs.experium.ru/api.php?action=query&prop=revisions&rvprop=content&format=jsonfm&titles=Experium_RESTful_Web_Service'
r = requests.get(url1, verify=False)
#r = requests.get('https://integdocs.experium.ru/api.php?action=query&prop=revisions&rvprop=content&format=jsonfm&titles=Experium_RESTful_Web_Service')
#r = requests.get(‘https://integdocs.experium.ru/api.php?action=query&prop=revisions&rvprop=content&format=jsonfm&titles=Experium_RESTful_Web_Service’)
print ("Result:",r.status_code)
#print ("Result:",r.text)
try:
    f = open('/tmp/load_html.txt', 'w+')
except IOError:
    print("Error opening file /tmp/load_html.txt")
    sys.exit(1)
f.write(r.text)
f.close()
try:
    f = open('/tmp/load_html.txt', 'r+')
except IOError:
    print("Error opening file /tmp/load_html.txt read")
    sys.exit(1)

try:
    f_json = open('/tmp/load_json.json', 'wb')
except IOError:
    print("Error opening file /tmp/load_json.json")
    sys.exit(1)

j_data = ''
while True:
    line = f.readline()
    if not line: break
    #if line.startswith('{| class="wikitable"'):
    if line.startswith('<pre'):
        line = f.readline()
        while not line.startswith('</pre>'):
            j_data = j_data + line
            line = f.readline()
#print(j_data)
#jsonDate = json.loads(j_data)
#print(jsonDate['query'])
q_data = j_data.replace('&quot;','"')

#print(q_data)
#e_data = q_data.encode()
#d_data = e_data.decode()
#jsonDate = json.loads(e_data)
#print (d_data)

#json.dump(q_data, f_json)
#f_json.write(e_data)
#print(json_data["query"]["pages"]["5"]["revisions"]["*"])
#f_json.close()
#json_data = json.loads(q_data)
'''
with open('/tmp/load_json.json','r') as jsonfile:
    #contents = jsonfile.read().decode("UTF-8")
    data = json.load(jsonfile)
print (type(data))
'''
'''
jsonfile = open('/tmp/load_json.json','rb')
contents = jsonfile.read().decode("UTF-8")
print (contents)
'''
#data = json.loads(contents)
#print (type(data))
#print (data)
#j = json.loads(data)
#print (type(j))
#final_data = json.loads(data['query']['pages']['5']['revisions']['*'])
#print("Data:",data)
#print(data['query']['pages']['5']['revisions']['*'])
'''
str = '{"key":["python", "py", 2]}'
jsonDate = json.loads(str)
print(jsonDate)
'''
'''
вывод:
{'key': ['python', 'py', 2]}
'''
#print(jsonDate['key'])
'''
вывод:
['python', 'py', 2]
'''
