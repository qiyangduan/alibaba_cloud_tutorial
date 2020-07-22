# https://market.aliyun.com/products/56928005/cmapi025075.html?spm=5176.2020520132.101.9.658d7218Ydd21H#sku=yuncode1907500007
# I have converted it by 2to3
# 
import urllib.request, urllib.parse, urllib.error, urllib.request, urllib.error, urllib.parse, sys
import ssl
import os

host = 'https://fapiao.market.alicloudapi.com'
path = '/v2/invoice/query'
method = 'POST'
appcode =  os.environ['DUGUANG_APPCODE']
querys = ''
bodys = {}
url = host + path
'''
      "发票代码": "3200194130",
      "发票号码": "xxx",
      "开票日期": "2020年6月17日",
      "不含税金额": "377.36",

'''
bodys['fpdm'] = '''123123123123'''
bodys['fphm'] = '''123123'''
bodys['kprq'] = '''20200601'''
bodys['noTaxAmount'] = '''484.91'''
bodys['checkCode'] = '''123123'''
post_data = urllib.parse.urlencode(bodys).encode("utf-8")
request = urllib.request.Request(url, post_data)
request.add_header('Authorization', 'APPCODE ' + appcode)
#根据API的要求，定义相对应的Content-Type
request.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
response = urllib.request.urlopen(request, context=ctx)
content = response.read()
if (content):
    print(content)