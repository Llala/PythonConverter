from lxml import etree

page = etree.Element('html')
doc = etree.ElementTree(page)
headElt = etree.SubElement(page, 'head')
bodyElt = etree.SubElement(page, 'body')
title = etree.SubElement(headElt, 'title')
title.text = 'Your page title here'
#<link rel='stylesheet' href='mystyle.css' type='text/css'>
linkElt = etree.SubElement(headElt, 'link', rel='stylesheet',
    href='mystyle.css', type='text/css')
outFile = open('homemade.xml', 'w')
doc.write(outFile)
