# coding=utf-8
import re

class Replacement(object):

    def __init__(self, replacement):
        self.replacement = replacement
        self.matched = None
        self.replaced = None

    def __call__(self, match):
        self.matched = match.group(0)
        self.replaced = match.expand(self.replacement)
        return self.replaced


f = open('out.mediawiki', 'r+')
res = open('quotes3.mediawiki', 'w+')
line = f.readline()
repl = Replacement("<b>\\1</b>")
n = 0
while line:
    line = f.readline()
    if not line: break
    #m = re.sub("'''([\wа-яА-Я\s\d\-]+)'''", repl, line)
    m = re.sub("'''([a-zA-Z\s]+)'''", repl, line)
    res.write(m)
    n = n+1
    print("String",n,":",m)
f.close()
res.close()
