# -*- coding: utf-8 -*-
print ("Hello, world!")
#with open('t_os.mediawiki', 'rb') as f:
    #content = f.readlines()
f = open('t_os.mediawiki', 'rb')
s = f.read()
print (s)
#print (content)
#aString = content

#print (aString[0])

#list = aString.split('{',1)

f.close()
#with open('out.mediawiki', encoding='utf-8', mode='w+') as f:
#    f.write('\u4500 blah blah blah\n')
#    f.seek(5)
#    print(repr(f.readline()[:1]))

with open('out.mediawiki', encoding='utf-8', mode='w+') as f:
    #for line in f:
    #    print(repr(line))
     f.seek(5)
     f.write('\uX')
