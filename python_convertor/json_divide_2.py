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
        #
        if mark == 0:
            mark = 1
            #s = "freework/%d-%s-%d"%(k,word,flag)
            #end = open(s, 'w+')
        else:
            #mark = 0
            #end.close()
            frame = {"type":"page",
                    "title":"new page",
                    "space":
                        {"key":"INTEG"
                        },
                    "body":
                        {"value":"%s"%c,"representation":"storage"
                        }
                        }
            s = "test/%d-%s-%d"%((k-1),word,flag)

            json_str = json.dumps(frame, ensure_ascii=False).encode('utf8')

            with io.open(s,'w+', encoding='utf8') as json_file:
                json_file.write(json_str.decode('utf8'))

            c = ''
            p_flag=flag
            #end = open(s, 'w+')
    if k!=0:
        #end.write(line)
        c = c + line
    n = n+1
    line = f.readline()

    flag = 0


frame = {"type":"page",
        "title":"new page",
        "space":
            {"key":"INTEG"
            },
        "body":
            {"value":"%s"%c,"representation":"storage"
            }
            }
s = "test/%d-%s-%d"%((k),word,p_flag)

json_str = json.dumps(frame, ensure_ascii=False).encode('utf8')

with io.open(s,'w+', encoding='utf8') as json_file:
    json_file.write(json_str.decode('utf8'))

#end.close()
