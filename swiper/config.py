"""互亿无限"""

# 接口地址
HY_SMS_URL = 'http://106.ihuyi.com/webservice/sms.php?method=Submit'


# 定义请求的数据
HY_SMS_PARAMS = {
    'account': 'C36604849',
    'password': 'd0274ae9d1e9e262a7688a2218bcb387',
    'mobile': '13619833735',
    'content': '您的验证码是：%s。请不要把验证码泄露给其他人。',
    'format': 'json',
}