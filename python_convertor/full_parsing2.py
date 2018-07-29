# -*- coding: utf-8 -*-
from lxml import etree
#f = open('t_os.mediawiki', 'r+')
f = open('out.mediawiki', 'r+')
#for line in f:
#    print line
#aString = f.read()
bString = f.read()
a = type(bString)
print (a)
#bString.decode("utf-8")
#print (aString)
#list = aString.split('{',1)
#print (list)
#bString = list[1]
#print ("----------------------------------------------------------------------------------------------------------------")
#print (bString)
hList = [] #лист заголовков
#Создание заголовка xml файла
#page = etree.Element('table')
#headElt = etree.SubElement(page, 'tbody')
#Header xml
#tr = etree.SubElement(headElt, 'tr')
begin_pos = bString.find('{')
if begin_pos!= -1:
    end_pos = bString.find('}')
    if end_pos!= -1:
        trunc_string = bString[begin_pos:end_pos+1]
        print ("Truncated string:",trunc_string)
        #Создание заголовка xml файла
        page = etree.Element('table')
        headElt = etree.SubElement(page, 'tbody')
        #Header xml
        tr = etree.SubElement(headElt, 'tr')
        if trunc_string.find('class="wikitable"')!= -1:
            #обработка заголовка таблицы
            pos = trunc_string.find('!')
            #print (bString[pos:])
            cString = trunc_string[pos+1:]
            #print (cString)
            pos2 = cString.find('!!')
            hList.append(cString[:pos2].strip())
            #th = etree.SubElement(tr, 'th')
            #th.text = cString[:pos2].strip()
            while pos2!=-1:
                cString = cString[pos2+2:]
                #print ("--------------------Changed------------------------------------------------------------------------------------")
                #print (cString)
                pos2 = cString.find('!!')
                if pos2 == -1:
                    pos2 = cString.find('|-')
                    pos3 = pos2
                #print ("pos2 =", pos2)
                #print (cString[:pos2])
                hList.append(cString[:pos2].strip())
                th = etree.SubElement(tr, 'th')
                th.text = cString[:pos2].strip()
                pos2 = cString.find('!!')
                #print (pos2)
                #print (hList)
            #print ("--------------------After header------------------------------------------------------------------------------------")
            cString = cString[pos3+2:]
            #print (cString)
            #обработка тела таблицы
            List = [] #лист тела таблицы
            pos = cString.find('|')
            while cString[pos+1]!='}':
                #print (cString[pos:])
                cString = cString[pos+1:]
                #print ("--------------------New------------------------------------------------------------------------------------")
                #print (cString)
                pos = cString.find('\n')
                line = cString[:pos]
                cString = cString[pos+1:]
                #print ("line:", line)
                pos_line = 0
                tr = etree.SubElement(headElt, 'tr')
                while pos_line!=-1:
                    pos_line = line.find('||')
                    List.append(line[:pos_line].strip())
                    td = etree.SubElement(tr, 'td')
                    td.text = line[:pos_line].strip()
                    line = line[pos_line+2:]
                pos = cString.find('|')
                if cString[pos+1] == '-':
                    cString = cString[pos+1:]
                    pos = cString.find('|')
            #print (List)
        else:
            print ("Not mediawiki data type")
    else:
        print("End of structure wasn't found")
else:
    print("End of structure wasn't found")
#f_pos = bString.find('{')
f.seek(begin_pos)
#f.write("X")
list = etree.tostringlist(page)
for item in list:
    f.write("%s\r\n" % item)

#doc = etree.ElementTree(page)
#doc.write('out.mediawiki',pretty_print=True, xml_declaration=True,   encoding="utf-8")

f.close();
