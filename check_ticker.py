import requests
import urllib3
import pandas as pd
import json
import time
import hashlib
from urllib.parse import urlencode

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_ticker(market,coin):
    headers = {'Content-type': 'text/html; charset=UTF-8',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
            }

    url = 'https://api.aex.zone/v3/ticker.php?mk_type={}&coinname={}'.format(market,coin)
    result = requests.get(url, headers=headers)
    market_list = result.json()['data']['ticker']
    high = market_list['high']
    low = market_list['low']
    last = market_list['last']
    last24 = market_list['last24']
    vol = market_list['vol']
    money = market_list['money']
    buy = market_list['buy']
    sell = market_list['sell']
    range = market_list['range']


    grades = {"24小时最高价":high,
              "24小时最低价":low,
              "最新成交价":last,
              "最近24小时的第一笔价格":last24,
              "24小时成交量，按交易货币统计":vol,
              "24小时成交量，按计价货币统计":money,
              "盘口买一档价格":buy,
              "盘口卖一档价格":sell,
              "24小时涨跌幅":range
              }
    data = pd.Series(data=grades)
    df = data.reset_index()
    df.columns = ["Market","行情"]
    print(df)

if __name__ == '__main__':
    # 以usdt交易来计算btc行情
    get_ticker('usdt','btc')

