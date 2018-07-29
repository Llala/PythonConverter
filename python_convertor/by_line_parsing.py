# coding=utf-8
#!/usr/bin/python
import sys
import re
from lxml import etree
import requests
import lxml.html
print("Start!")
f = open('out.mediawiki', 'r+')
res = open('result.mediawiki', 'w+')
hList = [] #лист заголовков
page = etree.Element('table')
doc = etree.ElementTree(page)
#headElt = etree.SubElement(page, 'tbody')
while True:
    line = f.readline()
    if not line: break
    if line.startswith('{| class="wikitable"'):
        #page = etree.Element('table')
        #doc = etree.ElementTree(page)
        headElt = etree.SubElement(page, 'tbody')
        tr = etree.SubElement(headElt, 'tr')
        line = f.readline()
        line = f.readline()
        print (line)
        pos = line.find('!')
        line = line[pos+1:]
        pos2 = line.find('!!')
        hList.append(line[:pos2].strip())
        th = etree.SubElement(tr, 'th')
        th.text = line[:pos2].strip()
        print ("First header:",line[:pos2].strip())
        flag = 0
        while flag == 0:
            line = line[pos2+2:]
            pos2 = line.find('!!')
            if pos2 == -1:
                pos2 = line.find('\n')
                flag = 1
            hList.append(line[:pos2].strip())
            th = etree.SubElement(tr, 'th')
            th.text = line[:pos2].strip()
            print ("Next header:", line[:pos2].strip())
        line = f.readline()
        while not line.startswith('|}'):
            pos = line.find('|')
            if line[pos+1]=='-':
                line = f.readline()
                pos = line.find('|')
            line = line[pos+1:]
            pos_line = 0
            tr = etree.SubElement(headElt, 'tr')
            flag_2 = 0
            while flag_2 == 0:
                pos_line = line.find('||')
                if pos_line == -1:
                    pos_line = line.find('\n')
                    flag_2 = 1
                td = etree.SubElement(tr, 'td')
                td.text = line[:pos_line].strip()
                print ("Add word:",line[:pos_line].strip())
                if flag_2 == 0:
                    line = line[pos_line+2:]
            line = f.readline()
        my_str = my_str = etree.tostring(headElt, pretty_print=True, encoding='utf-8').decode('utf-8')
        print (type(my_str))
        res.write("%s\n" % my_str)
    else:
        res.write(line)
f.close()
res.close()
