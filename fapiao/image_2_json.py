# https://duguang.aliyun.com/document/%E9%AB%98%E7%B2%BE%E7%89%88.html
import urllib.request
import urllib.parse
import json
import time
import base64

import os


with open('/Users/qiyangduan/alibaba/projects/Workshops_Others/otis/Round-1/ocr_result/餐饮普票/餐饮普票-1.jpg', 'rb') as f:  # 以二进制读取本地图片
    data = f.read()
    encodestr = str(base64.b64encode(data),'utf-8')
#请求头
# 请修改为你自己的appcode，可从云市场订单或者api网关处获得
AppCode =  os.environ['DUGUANG_APPCODE']
print(AppCode)
headers = {
    'Authorization': 'APPCODE ' + AppCode,
    'Content-Type': 'application/json; charset=UTF-8'
}
def posturl(url,data={}):
  try:
    params=json.dumps(dict).encode(encoding='UTF8')
    req = urllib.request.Request(url, params, headers)
    r = urllib.request.urlopen(req)
    html =r.read()
    r.close();
    return html.decode("utf8")
  except urllib.error.HTTPError as e:
      print(e.code)
      print(e.read().decode("utf8"))
  time.sleep(1)
if __name__=="__main__":
    # url_request="https://ocrapi-estate-cert.taobao.com/ocrservice/estateCert"
    url_request="https://ocrapi-mixed-multi-invoice.taobao.com/ocrservice/mixedMultiInvoice"
    dict = {'img': encodestr}

    html = posturl(url_request, data=dict)
    print(html)