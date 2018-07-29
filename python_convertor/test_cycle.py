# coding=utf-8
from lxml import etree

f = open('out.mediawiki', 'r+')
res = open('result.mediawiki', 'w+')
line = f.readline()
#while not line.endswith('|}'):
while line:
    line = f.readline()
    if not line: break
    if line.endswith('}'):
        print(line)
    #if line.endswith('}'): break
