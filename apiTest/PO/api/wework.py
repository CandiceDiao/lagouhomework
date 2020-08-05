import json

import pytest
from filelock import FileLock

from apiTest.PO.api.base_api import BaseApi

### 用锁的方法 实现pytest.fixture(scope='session') 仅运行一次功能
def token():
    data={
           "method": "get",
           "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
           "params":{
               "corpid":"ww44051ca7a74ae8e3",
               "corpsecret":"uhSqBpzjxIvpbfPaXuPH574dfKwPUcLzlnqOGEklghc"
            }
        }
    res = BaseApi.send_api(data)
    return res.json()['access_token']

class WeWork(BaseApi):

    # # 获取token
    # def test_get_token(self):
    #     data={
    #        "method": "get",
    #        "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
    #        "params":{
    #            "corpid":"ww44051ca7a74ae8e3",
    #            "corpsecret":"uhSqBpzjxIvpbfPaXuPH574dfKwPUcLzlnqOGEklghc"
    #         }
    #     }
    #     res = self.send_api(data)
    #     try:
    #         return res['access_token']
    #     except Exception as e:
    #         raise ValueError("requests token error")

    @pytest.fixture(scope='session')
    def get_token(self, tmp_path_factory, worker_id):
        if not worker_id:
            # not executing in with multiple workers, just produce the data and let
            # pytest's fixture caching do its job
            return token()

        # get the temp directory shared by all workers
        root_tmp_dir = tmp_path_factory.getbasetemp().parent
        # root_tmp_dir=C:\Users\WBPC0154\AppData\Local\Temp\pytest-of-WBPC0154\pytest-19
        print (root_tmp_dir)

        fn = root_tmp_dir / "data.json"
        with FileLock(str(fn) + ".lock"):
            if fn.is_file():
                data = json.loads(fn.read_text())
            else:
                data = token()
                fn.write_text(json.dumps(data))
        return data
