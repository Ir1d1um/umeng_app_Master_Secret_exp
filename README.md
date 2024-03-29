# umeng_app_Master_Secret_exp
友盟+消息推送密钥泄露验证工具
运行环境：python3

# 0x01 脚本说明
友盟+开放平台的API文档中提供了生成签名的python2脚本，但是拉到本地后一直无法利用成功，之后分析了下官方的代码调用示例，重构了这个简单的python3的验证脚本;
所使用的是提供的/api/imglist接口，该接口为单纯的查询功能，无任何危害;

# 0x02 使用说明
需要手动替换代码中`appkey`和`app_master_secret`的值，保存后`python3 exp.py`即可;

# 0x03 输出说明
由于不同环境下查询的回包不一定相同，所以直接输出了回包内容
如果无法利用的话，应该是会直接返回
```
{"ret":"FAIL","data":{"error_msg":"签名不正确","error_code":"2027"}}
```
密钥可用的话，应该是
```
{"ret":"SUCCESS","data":{.....}}
```

# 0x04 免责声明
本工具仅能在取得足够合法授权的企业安全建设中使用，在使用本工具过程中，您应确保自己所有行为符合当地的法律法规。

如您在使用本工具的过程中存在任何非法行为，您将自行承担所有后果，本工具所有开发者和所有贡献者不承担任何法律及连带责任。

除非您已充分阅读、完全理解并接受本协议所有条款，否则，请您不要使用本工具。

您的使用行为或者您以其他任何明示或者默示方式表示接受本协议的，即视为您已阅读并同意本协议的约束。
