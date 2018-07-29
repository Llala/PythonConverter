# coding=utf-8
import sys
import re
import json
import io
import os
import requests
import codecs
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class Replacement(object):
    def __init__(self, replacement):
        self.replacement = replacement
        self.matched = None
        self.replaced = None

    def __call__(self, match):
        self.matched = match.group(0)
        self.replaced = match.expand(self.replacement)
        return self.replaced

print("Confluence TOC uploader")

if len(sys.argv) != 2:
    print("Syntax: uploader.py [TOC-directory]")
    sys.exit(1)

baseaddr = "https://confluence.experium.ru/rest/api/content/?os_authType=basic"
id = 3277113
key = "INTEG"

username = "jira"
password = "jira"

for file in os.listdir(sys.argv[1]):
        fn = os.path.join(sys.argv[1], file)
        print('Uploading file: ' + fn)

        file = open(fn, "r")
        fmtcontent = file.read()
        fmtcontent = fmtcontent.replace('%%KEY%%', key)
        fmtcontent = fmtcontent.replace('%%ID%%', str(id))
        fmtcontent = fmtcontent.replace('\n', '<br/>')
        fmtcontent = fmtcontent.replace('<syntaxhighlight lang=\\\"html5\\\">', '<ac:structured-macro ac:macro-id=\\"536312fc-b54c-4991-9a17-144bb8245867\\" ac:name=\\"code\\" ac:schema-version=\\"1\\"><ac:parameter ac:name=\\"language\\">cpp</ac:parameter><ac:parameter ac:name=\\"theme\\">Eclipse</ac:parameter><ac:parameter ac:name=\\"title\\">test</ac:parameter><ac:parameter ac:name=\\"linenumbers\\">true</ac:parameter><ac:plain-text-body><![CDATA[')
        fmtcontent = fmtcontent.replace('<syntaxhighlight lang=\\\"javascript\\\">', '<ac:structured-macro ac:macro-id=\\"536312fc-b54c-4991-9a17-144bb8245867\\" ac:name=\\"code\\" ac:schema-version=\\"1\\"><ac:parameter ac:name=\\"language\\">cpp</ac:parameter><ac:parameter ac:name=\\"theme\\">Eclipse</ac:parameter><ac:parameter ac:name=\\"title\\">test</ac:parameter><ac:parameter ac:name=\\"linenumbers\\">true</ac:parameter><ac:plain-text-body><![CDATA[')
        fmtcontent = fmtcontent.replace('</syntaxhighlight>', ']]></ac:plain-text-body></ac:structured-macro>')
        file.close()

        #print(fmtcontent)
        #break

        j = json.loads(fmtcontent)
        value = str(j['body']['storage']['value'])
        rpl = value.replace('<br/>', '')
        j['body']['storage']['value'] = rpl

        fmtcontent = json.dumps(j, indent=4, ensure_ascii=False)

#        print(fmtcontent)
#        break

        headers = {'Content-type': 'application/json', 'X-Atlassian-Token': 'no-check'}
        r = requests.post(baseaddr, auth=(username, password), data=fmtcontent.encode('utf-8'), verify=False, headers=headers)

        print(r.status_code, r.reason)
        if r.status_code != 200:
            print("Failed to create page!")
            print(r.text)
            sys.exit(1)


        break
