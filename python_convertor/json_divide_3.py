# coding=utf-8
import re
import json
import io

#s = "dflgksdflgk"
f= open('double_n.mediawiki', 'r+')
line = f.readline()
n = 0
k = 0
p_flag = 0
flag=0
mark = 0
c = ''
p_word = ''
number = ''
p_number = ''
a = 0
b = 0
d = 0
e = 0
while line:
    if not line: break
    if line.startswith('='):
        k = k+1
        flag = flag+1
        if line[1] == '=':
            flag = flag+1
            if line[2] == '=':
                flag = flag+1
                if line[3] == '=':
                    flag = flag+1
                    if line[4] == '=':
                        flag = flag+1
                        print (flag)
                        print ("String",n,":",line)
        i = flag
        print(line)
        print (flag)
        print(line[flag])
        word = ''
        while line[i] != '=':
            word = word + line[i]
            i=i+1
        word = word.strip()
        print (word)
        if flag == 2:
            a = a+1
            b = 0
            d = 0
            e = 0
            number =number + str(a)
        if flag == 3:
            b = b+1
            d = 0
            e = 0
            number =number + str(a) + str(b)
        if flag == 4:
            d = d+1
            e = 0
            number =number + str(a) + str(b) + str(d)
        if flag == 5:
            e = e+1
            number =number + str(a) + str(b) + str(d) + str(e)
        print("Number:",number)
        if mark == 0:
            mark = 1
            p_word = word
            p_flag=flag
            p_number = number
            number = ''
            #s = "freework/%d-%s-%d"%(k,word,flag)
            #end = open(s, 'w+')
        else:
            #mark = 0
            #end.close()
            frame = {
                      "type": "page",
                      "title": "%s"%p_word,
                      "ancestors": [
                        {
                          "id": "%d"
                        }
                      ],
                      "space": {
                        "key": "%s"
                      },
                      "body": {
                        "storage": {
                          "value": "%s"%c,
                          "representation": "storage"
                        }
                      }
                    }
            print("Number name:",number)
            s = "test/%s-%s-%d"%(p_number,p_word,p_flag)

            json_str = json.dumps(frame, ensure_ascii=False).encode('utf8')

            with io.open(s,'w+', encoding='utf8') as json_file:
                json_file.write(json_str.decode('utf8'))

            c = ''
            p_flag=flag
            p_word = word
            p_number = number
            number = ''
            #end = open(s, 'w+')
    if k!=0:
        #end.write(line)
        c = c + line
    n = n+1
    line = f.readline()

    flag = 0


frame = {
          "type": "page",
          "title": "%s"%p_word,
          "ancestors": [
            {
              "id": "%d"
            }
          ],
          "space": {
            "key": "%s"
          },
          "body": {
            "storage": {
              "value": "%s"%c,
              "representation": "storage"
            }
          }
        }
s = "test/%s-%s-%d"%(p_number,p_word,p_flag)

json_str = json.dumps(frame, ensure_ascii=False).encode('utf8')

with io.open(s,'w+', encoding='utf8') as json_file:
    json_file.write(json_str.decode('utf8'))

#end.close()
