import hashlib
import time
import requests
import configparser
config = configparser.ConfigParser()

path = 'config.ini'
config.read(path)

timestamp = int(time.time())
time1=time.time()
print(timestamp)
print(time1)
# str_key='xdsferwfewrf'      # 公钥
# str_id='2349324534'         # 用户ID
# str_skey='340rijwejfwe'     # 私钥

def getmd5():
    m = hashlib.md5()   # 生成一个md5对象
    mdt = "%s_%s_%s_%s" % (str_key, str_id, str_skey, timestamp)  # 生成需要加密的字串
    m.update(mdt.encode("utf8"))  # 使用update进行加密
    _md55=m.hexdigest()
    print(_md55)
    return _md55  # 将加密结果，显示成16进制字串，并返回


if __name__ == '__main__':
    # 生产md5
    _md55=getmd5()