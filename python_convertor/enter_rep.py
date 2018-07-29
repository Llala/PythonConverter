# coding=utf-8

f = open('double_n.mediawiki', 'r+')
res = open('final_n.mediawiki', 'w+')
line = f.readline()
while line:
    if not line: break
    line.replace('\\n','<br\>')
    res.write(line)
    line = f.readline()
f.close()
res.close()
