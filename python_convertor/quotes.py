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



#s = "fdsfsdfsd '''jj 232''' hhh '''Пример fff-ggg'''"

repl = Replacement("<strong>\\1</strong>")
repl2 = Replacement("<em>\\1</em>")

f = open('result_reg.mediawiki', 'r+')
res = open('quotes_n.mediawiki', 'w+')
line = f.readline()
#Поиск тройных кавычек
while line:
    if not line: break
    #m = re.sub("'''([\wа-яА-Я\s\d\-]+)'''", repl,line)
    m = re.sub("'''([\wа-яА-Я\s\d\-,:,=\/]+)'''", repl,line)
    #print(m)
    res.write(m)
    line = f.readline()
f.close()
res.close()
#Поиск двойных кавычек
res = open('quotes_n.mediawiki', 'r+')
fin= open('double_n.mediawiki', 'w+')
line = res.readline()
while line:
    if not line: break
    #m = re.sub("'''([\wа-яА-Я\s\d\-]+)'''", repl,line)
    b = re.sub("''([\wа-яА-Я\s\d\-,:,=\/]+)''", repl2,line)
    print(b)
    fin.write(b)
    line = res.readline()
res.close()
fin.close()
