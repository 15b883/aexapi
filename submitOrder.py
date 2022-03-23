import hashlib
import json
import time

import requests

headers = {'Content-type': 'application/json; charset=UTF-8',
           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
           }

timestamp = int(time.time())
# str_key='xxx'              # 请替换您的公钥
# str_id='12345678'          # 请替换您的用户ID
# str_skey='asorgnaerognar'  # 请替换您的私钥

def getmd5():
    # timestamp = int(time.time()) 当前时间
    m = hashlib.md5()  # 生成一个md5对象
    mdt = "%s_%s_%s_%s" % (str_key, str_id, str_skey, timestamp)  # 生成需要加密的字串
    m.update(mdt.encode("utf8"))  # 使用update进行加密
    _md55 = m.hexdigest()
    return _md55  # 将加密结果，显示成16进制字串，并返回


def get_MyBalance(_md55):
    data = {
        'key': str_key,
        'time': timestamp,
        'md5': _md55,
        'mk_type': 'usdt',
        'coinname': 'shib',  # 输入你拥有的币
        'type': 2,  # 1 买入挂单，2卖出挂单，不可为空
        'price': 0.00003323,  # 价格
        'amount': str(100000)  # 挂单数量
    }
    url = 'https://api.aex.zone/v3/submitOrder.php'
    try:
        result = requests.post(url, json=data, headers=headers)
        print(result.content)
        print(result.status_code)
    except Exception as err:
        print("发送挂单时出现: ",err)


if __name__ == '__main__':
    # 生产md5
    _md55 = getmd5()
    # 检查账号余额
    get_MyBalance(_md55)
