# coding=utf-8

from lxml import etree
import lxml.html
import re

f = open('out.mediawiki', 'r+')
res = open('result.mediawiki', 'w+')
line = f.readline()
pattern = re.compile(r"('''[a-zA-Z\s]+''')")
n = 0
while line:
    line = f.readline()
    if not line: break
    m = pattern.findall(line)
    n = n+1
    print("String",n,":",m)
