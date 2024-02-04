import hashlib
import json
import time
import requests

def md5(s):
    m = hashlib.md5(s.encode('utf-8'))
    return m.hexdigest()

# 替换成你的对应值
appkey = 'YOUR APP KEY'
app_master_secret = 'YOUR APP MASTER SECRET'
timestamp = int(time.time())

method = 'POST'
url = 'http://msg.umeng.com/api/imglist'
params = {"appKey":appkey,"timestamp":timestamp,"page_index":1,"page_size":5,"img_type":"large_icon"}
post_body = json.dumps(params)

# 生成签名
temp = method+url+post_body+app_master_secret
## print(temp)
sign = md5('{}{}{}{}'.format(method, url, post_body, app_master_secret))
# print(sign)  # 打印生成的签名

header = {"Content-Type": "application/json",}

r = requests.post(url+"?sign="+sign, data=post_body, headers=header)
print("响应报文如下，如存在SUCCESS为key有效：")
print(r.text)
