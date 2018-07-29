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

    print ("Syntax: print_cont.py arg[1]:source file name arg[2]:result catalog name.")

    print("Using default: arg[1]:double_n.mediawiki arg[2]:test")

    f = open('double_n.mediawiki', 'r+')

    from os.path import expanduser

    home = expanduser("~")

    print(home)

    path = home + '/' + 'test'

    print(path)

    try:

        os.mkdir(path)

    except OSError:

        print("Directory test already exists.")

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

uid = 1

h_Line = ''

space = ''

p_space = ''

cont = set()

way = "%s/%s"%(path, 'contents.mediawiki')

contents = open(way, 'w+')

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

        #print(line)

        #print(h_line)

        #print (flag)

        #print(line[flag])

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

            space = ''

            number =number + str(a)

        if flag == 3:

            b = b+1

            d = 0

            e = 0

            space = '_'

            number =number + str(a) + str(b)

        if flag == 4:

            d = d+1

            e = 0

            space = '__'

            number =number + str(a) + str(b) + str(d)

        if flag == 5:

            e = e+1

            space = '___'

            number =number + str(a) + str(b) + str(d) + str(e)

        #print("Number:",number)

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

            if p_word not in cont:

                cont.add(p_word)

            else:

                print("File name conflict:", p_word)

                temp = p_word + ' ' + str(uid)

                uid = uid + 1

                p_word = temp

                cont.add(temp)

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

            #print("Number name:",number)



            w = p_space + p_word

            s = "%s/%s"%(path,w)

            wr_s = p_space + p_word + '\n'

            contents.write(wr_s)

            json_str = json.dumps(frame, ensure_ascii=False).encode('utf8')



            with io.open(s,'w+', encoding='utf8') as json_file:

                json_file.write(json_str.decode('utf8'))



            c = ''

            p_flag=flag

            p_word = word

            p_number = number

            p_space = space

            number = ''

        #end = open(s, 'w+')

    if k!=0:

        if h_line != '':

            c = c + h_line

            h_line = ''

        elif re.match(r'\s*<syntaxhighlight', line):

            #print("Inside:",line)

            c = c + line

            while not line.startswith('</syntaxhighlight>'):

                line = f.readline()

                #print("Inside:",line)

                c = c + line

        elif re.match(r'\s*<table>', line):

            #print("Inside:",line)

            c = c + line

            while not line.startswith('</table>'):

                line = f.readline()

                #print("Inside:",line)

                c = c + line

        else:

            s_line = line[:-1]+'<br/>'

            c = c + s_line

    n = n+1

    line = f.readline()



    flag = 0

if p_word not in cont:

    cont.add(p_word)

else:

    print("File name conflict:", p_word)

    temp = p_word + ' ' + str(uid)

    uid = uid + 1

    p_word = temp

    cont.add(temp)



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

w = p_space + p_word

s = "%s/%s"%(path,w)



wr_s = p_space + p_word + '\n'

contents.write(wr_s)

json_str = json.dumps(frame, ensure_ascii=False).encode('utf8')



with io.open(s,'w+', encoding='utf8') as json_file:

    json_file.write(json_str.decode('utf8'))

contents.close()

contents = open(way, 'r+')

line = contents.read()

print('---------------------Contents listing------------------------------------------')

while line:

    if not line: break

    print(line)

    line = contents.read()
