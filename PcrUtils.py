
import os
import requests
import json
import yaml
import logging

"""
    基本的request请求封装了一些必要的参数
"""


pcrconfig = os.path.join(os.path.dirname(__file__), 'pcrconfig.yaml')

_log = logging.getLogger(__name__)

def read_yaml(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)

class BaseRequest:
    def __init__(self):
        self.config = read_yaml(pcrconfig)
        self.name = self.config.get('name')
        self.ts = self.config.get('ts')
        self.nonce = self.config.get('nonce')
        self.appkey = self.config.get('appkey')
        self.sign = self.config.get('sign')
        self.params = {
            "name":self.name,
            "ts":self.ts,
            "nonce":self.nonce,
            "appkey":self.appkey,
            "sign":self.sign,
        }
        self.headers = {
            "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
            'Connection':'keep-alive',
            "Cookie": "SESSDATA=319e5dce%2C1738400231%2C56351%2A81CjAnUuFMIECEgHodX-upHeHVz89LnN0pSNSrSwaKuFdqz72JazQXoSvZd9cMT4oZrw8SVlhwT0pwam9yUE8xd0FUOTllNC1BWVNUeUlEYVMzY3ExS1B2dHRTTEllUEcyUW5lQVllcndvWFJydDE2Z2h2aW00VEY5X09SZUhIN0wtaGd5bVhtODV3IIEC",
            "Bili-Status-Code":"0",
            "X-Bili-Trace-Id":'1b72650df6ab5d64211db1174066b185',
            'X-Ticket-Status':'1',
            'X-Cache-Webcdn':'BYPASS from blzone01',
            'Content-Encoding':'br'
        }
    def fetch_data(self):
        session = requests.Session()
        r = session.get('https://api.game.bilibili.com/game/player/tools/pcr/search_clan', headers=self.headers,
                            params=self.params, allow_redirects=True)
         # 尝试使用 utf-8 解码
        print(r.url)
        decoded_data = r.content.decode('utf-8', errors='replace')

        # 尝试解析为 JSON
        json_data = json.loads(decoded_data)
        # print("JSON 解析成功")
        return json_data
class rank:
    def fetch_data(self):
        str = requests.get('http://localhost:8099/pcr/getPcrRank')
        return str.text.__str__()
class updateParam():
    def fetch_data(self,param):
        str = requests.post('http://localhost:8099/pcr/updateParam',param)
        return str.text.__str__()


# if __name__ == "__main__":
#     # s = BaseRequest().fetch_data()
#     # s = test()
#     # print(s.fetch_data())
#     # print(s.get('data',[]))

