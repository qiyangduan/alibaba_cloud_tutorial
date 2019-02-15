# This program referred to this sample code: 
# https://blog.csdn.net/w5688414/article/details/79317534

import base64
import urllib.parse
import hmac
from hashlib import sha1
import requests
import uuid
import time
import hmac,ssl
import sys



import os
ALIYUN_ACCESS_KEY_ID= os.environ['ALIME_BOT_ACCESS_ID']
ALIYUN_ACCESS_KEY_SECRET= os.environ['ALIME_BOT_ACCESS_KEY_SECRET']


# To bypass SSL problem
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context
 
D = {
    'Format':'JSON',
    'Version':'2017-10-11',
    'SignatureMethod':'HMAC-SHA1'
    }

timestamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
D['SignatureNonce']=str(uuid.uuid1())
D['SignatureVersion']=1.0
D['AccessKeyId']=ALIYUN_ACCESS_KEY_ID
D['Timestamp']=timestamp
 
 
def percent_encode(encodeStr):
    encodeStr = str(encodeStr)
    res = urllib.parse.quote(encodeStr)
    res = res.replace('+', '%20')
    res = res.replace('*', '%2A')
    res = res.replace('%7E', '~')
    return res
 
def sign(parameters):
    sortedParameters = sorted(parameters.items(), key=lambda parameters: parameters[0])
    # print(sortedParameters)
    canonicalizedQueryString = ''
    for (k, v) in sortedParameters:
        canonicalizedQueryString += '&' + percent_encode(k) + '=' + percent_encode(v)
    stringToSign = 'GET&%2F&' + percent_encode(canonicalizedQueryString[1:])   
    bs = ALIYUN_ACCESS_KEY_SECRET + '&'
    bs = bytes(bs, encoding='utf8')
    stringToSign = bytes(stringToSign, encoding='utf8')
    h = hmac.new(bs, stringToSign, sha1)
    #  
    signature = base64.b64encode(h.digest()).strip()
    return signature
 


D['Action']="Chat"
D['InstanceId']="chatbot-cn-0pp0yi58q0001x"  
# D['Utterance']="I want to check my pension balance" 
D['Utterance']="I want to transfer money to my bank in UK"
# D['Signature'] = sign(D)



if __name__ == "__main__": 
    if len (sys.argv) == 1 :
        # print("Usage: python chat.py message")
        # sys.exit (1)
        chat1 ="I want to transfer money to my bank in UK"
    else: 
        chat1 = sys.argv[1]  
    # print("message:  " , chat1)
    D['Utterance'] = chat1
    D['Signature'] = sign(D)
    sortedParameters = sorted(D.items(), key=lambda D: D[0])
    # print(D["Signature"])
    # print(sortedParameters)
    
    url = 'https://chatbot.cn-shanghai.aliyuncs.com/?' + urllib.parse.urlencode(sortedParameters)
    # print(url)
    r = requests.get(url)
    print(r.text)
    
