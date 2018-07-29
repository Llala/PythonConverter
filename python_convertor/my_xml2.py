from lxml import etree

page = etree.Element('table')
doc = etree.ElementTree(page)
headElt = etree.SubElement(page, 'tbody')
#Header
tr = etree.SubElement(headElt, 'tr')
th = etree.SubElement(tr, 'th')
th.text = 'Type'
th = etree.SubElement(tr, 'th')
th.text = 'Server'
#Body
tr = etree.SubElement(headElt, 'tr')
td = etree.SubElement(tr, 'td')
td.text = 'Element1'
outFile = open('homemade2.xml', 'w')
#doc.write(outFile)
#doc.write(outFile,pretty_print=True, xml_declaration=True,   encoding="utf-8")
print etree.dump(page)
#outFile.seek(10)
list = etree.tostringlist(page)
for item in list:
    outFile.write("%s\n" % item)
#outFile.write("\n".join(list).join("\n"))
