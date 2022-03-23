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


def getMyTradeList(_md55):
    data = {
        'key': str_key,
        'time': timestamp,
        'md5': _md55,
        'mk_type': 'usdt',
        'coinname': 'shib',  # 输入你拥有的币
        'page': 0  # 默认 page 是 0，即查询第 1 页的数据
    }
    url = 'https://api.aex.zone/v3/getMyTradeList.php'
    try:
        result = requests.post(url, json=data, headers=headers).json()
        # print(result['data'])
        for i in result['data']:
            print(i)
        # print(result.status_code)
    except Exception as err:
        print("查询成交明细时出错: ",err)


if __name__ == '__main__':
    # 生产md5
    _md55 = getmd5()
    # 检查账号余额
    getMyTradeList(_md55)


'''
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