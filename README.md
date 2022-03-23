# AexApi

## 常用链接

* 所有REST接口的: https://api.aex.zone
* 所有接口的响应都是 JSON 格式
* POST 方法的接口参数以内容形式为 application/json 发送

```
"https://api.aex.zone/v3/getMyBalance.php",  # 账户余额API
"https://api.aex.zone/v3/ticker.php",        # 获取交易对行情数据
"https://api.aex.zone/v3/getOrderList.php",  # 通过 Tag 查询我的挂单
"https://api.aex.zone/v3/cancelOrder.php",   # 撤单
"https://api.aex.zone/v3/submitOrder.php",   # 挂单
"https://api.aex.zone/v3/depth.php",         # 获取选定市场挂单深度，asks是卖方, bids是买方
"https://api.aex.zone/v3/trades.php",        # 获取交易对历史成交数据,默认30条
"https://api.aex.zone/v3/getMyTradeList.php",# 我的成交记录,默认每页30条
"https://api.aex.zone/v3/allpair.php         # 获取所有交易对信息
```

更多信息请参考:

[https://www.aex.com/page/doc/zh/coin/coin.html](https://www.aex.com/page/doc/zh/coin/coin.html)

## 实现功能

* 查询单个币行情
* 查询aex所有币行情
* 查询个人账号余额
* 挂单（购买）



## **APIKey**

关于使用APIkey的，可以申请两个：（参考 https://www.aex.com/page/doc/zh/problem/problem.html）

（1）只读权限：读取权限用于对数据的查询接口，例如：查余额、订单查询、成交查询等。

（2）交易权限：交易权限用于币币下单、撤单。



## 常见问题

> REST经常返回request connection to many

ip可能被限频了，当前是每个ip只支持两秒内40次访问

> 交易key 设置白名单了，但是 我挂着vpn呢 IP地址还准吗

可以访问 https://www.ipaddress.com/  核对下；获取深度出错的话可能有程序问题

> {'code': 50004, 'msg': 'Incorrect information', 'data': []}

解决方式：

```
'Content-Type': 'application/json' 
```

> {'data': 'response error | '}  

request 请求返回值不一定是json格式的，所以你在打印返回时使用

```
print(result.text) # 以text 或者其他content试试
```

