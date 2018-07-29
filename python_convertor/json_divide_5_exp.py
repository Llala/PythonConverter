# coding=utf-8
import re
import json
import io
import sys
import os
#s = "dflgksdflgk"
#f= open('double_n.mediawiki', 'r+')
print ('Number of arguments:', len(sys.argv), 'arguments.')
if len(sys.argv) < 3:
    print ("Wrong argument number: input file name and catalog name!")
else:
    f_name = sys.argv[1]
    if f_name != '':
        f= open( f_name, 'r+')
    else:
        print ("Empty line arguments")
        f= open('double_n.mediawiki', 'r+')
    catalog = sys.argv[2]
    print("Catalog:", catalog)
    if catalog != '':
        from os.path import expanduser
        home = expanduser("~")
        print(home)
        path = home+'/'+ sys.argv[2]
        print(path)
        try:
            os.mkdir(path)
        except OSError:
            print("Directory", catalog , "already exists.")
    else:
        print ("Second line argument is absent")
        catalog = 'test'

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
    l = 0
    h_Line = ''
    while line:
        if not line: break
        if line.startswith('='):
            k = k+1
            flag = flag+1
            length = len(line)
            #line = '<h1>'+line[1:(length-1)]+'<\h1>'
            if line[1] == '=':
                h_line = '<h2>'+line[2:(length-3)]+'</h2>'
                flag = flag+1
                if line[2] == '=':
                    h_line = '<h3>'+line[3:(length-4)]+'</h3>'
                    flag = flag+1
                    #line = '<h3>'+line[3:(length-3)]+'<\h3>'
                    if line[3] == '=':
                        h_line = '<h4>'+line[4:(length-5)]+'</h4>'
                        flag = flag+1
                        if line[4] == '=':
                            flag = flag+1
                            h_line = '<h5>'+line[5:(length-6)]+'</h5>'
                            #print (flag)
                            #print ("String",n,":",line)
            i = flag
            print(line)
            print(h_line)
            print (flag)
            print(line[flag])
            word = ''
            while line[i] != '=':
                word = word + line[i]
                i=i+1
            word = word.strip()
            #print (word)
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
                             "id": "%%ID%%"
                           }
                         ],
                         "space": {
                           "key": "%%KEY%%"
                         },
                          "body": {
                            "storage": {
                              "value": "%s"%c,
                              "representation": "storage"
                            }
                          }
                        }
                print("Number name:",number)
                s = "%s/%s-%s-%d"%(path, p_number,p_word,p_flag)

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
            if h_line != '':
                c = c + h_line
                h_line = ''
            else:
                c = c + line
        n = n+1
        line = f.readline()

        flag = 0


    frame = {
              "type": "page",
              "title": "%s"%p_word,
              "ancestors": [
               {
                 "id": "%%ID%%"
               }
             ],
             "space": {
               "key": "%%KEY%%"
             },
              "body": {
                "storage": {
                  "value": "%s"%c,
                  "representation": "storage"
                }
              }
            }
    s = "%s/%s-%s-%d"%(path, p_number,p_word,p_flag)

    json_str = json.dumps(frame, ensure_ascii=False).encode('utf8')

    with io.open(s,'w+', encoding='utf8') as json_file:
        json_file.write(json_str.decode('utf8'))

#end.close()
