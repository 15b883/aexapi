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
    m = hashlib.md5()
    mdt = "%s_%s_%s_%s" % (str_key, str_id, str_skey, timestamp)
    m.update(mdt.encode("utf8"))
    _md55 = m.hexdigest()
    return _md55

def getMyTradeList(_md55):
    data = {
        'key': str_key,
        'time': timestamp,
        'md5': _md55,
        'mk_type': 'usdt',
        'coinname': 'shib',  # 输入你查询的币
        'page': 0            # 默认page是0，即查询第 1 页的数据
    }
    url = 'https://api.aex.zone/v3/getMyTradeList.php'
    try:
        result = requests.post(url, json=data, headers=headers).json()
        for i in result['data']:
            print(i)
    except Exception as err:
        print("查询成交明细时出错: ",err)


if __name__ == '__main__':
    _md55 = getmd5()
    getMyTradeList(_md55)

'''
## 输出结果
trade_id	int	成交 ID
type	int	挂单类型 1 buy 2 sell
tab_id	int	挂单响应的流水 ID
price	string	成交价格
amount	string	成交数量
time	string	成交时间
fee	string	成交手续费
fee_coin	string	成交手续费币种
exec_type	string	流动性方向 t-taker m-maker
'''