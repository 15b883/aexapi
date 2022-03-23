import hashlib
import time
import requests
import json

headers = {'Content-type': 'application/json; charset=UTF-8',
           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
           }

timestamp = int(time.time())
# str_key='xxx'              # 请替换您的公钥
# str_id='12345678'          # 请替换您的用户ID
# str_skey='asorgnaerognar'  # 请替换您的私钥


def getmd5():
    m = hashlib.md5()  # 生成一个md5对象
    mdt = "%s_%s_%s_%s" % (str_key, str_id, str_skey, timestamp)  # 生成需要加密的字串
    m.update(mdt.encode("utf8"))  # 使用update进行加密
    _md55=m.hexdigest()
    return _md55  # 将加密结果，显示成16进制字串，并返回

def get_MyBalance(_md55):
    data = {
        'key': str_key,
        'time': timestamp,
        'md5': _md55,
        'coins': 'btc,eos,shib,usdt',   # 输入你拥有的币
    }
    url = 'https://api.aex.zone/v3/getMyBalance.php'
    result = requests.post(url,json=data,headers=headers)
    balance = result.json()['data']
    for b in balance:
        print(b,":" + balance[b])

'''
结果展示：
btc_balance :0.0000000
btc_balance_lock :0
eos_balance :0.0000000
eos_balance_lock :0
shib_balance :0.0000000
shib_balance_lock :0.0000000
usdt_balance :0.0000000
usdt_balance_lock :0
'''

if __name__ == '__main__':
    # 生产md5
    _md55=getmd5()
    # 检查账号余额
    get_MyBalance(_md55)