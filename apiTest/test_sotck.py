import json
import pytest
import requests
from filelock import FileLock

### 用锁的方法 实现pytest.fixture(scope='session') 仅运行一次功能
def get_token():
    params = {
        "corpid": "ww44051ca7a74ae8e3",
        "corpsecret": "uhSqBpzjxIvpbfPaXuPH574dfKwPUcLzlnqOGEklghc"
    }
    res = requests.get(url="https://qyapi.weixin.qq.com/cgi-bin/gettoken", params=params)
    return res.json()['access_token']


class TestTag:
    # @pytest.fixture(scope='session')
    def token(self, tmp_path_factory, worker_id):
        if not worker_id:
            # not executing in with multiple workers, just produce the data and let
            # pytest's fixture caching do its job
            return get_token()

        # get the temp directory shared by all workers
        root_tmp_dir = tmp_path_factory.getbasetemp().parent
        # root_tmp_dir=C:\Users\WBPC0154\AppData\Local\Temp\pytest-of-WBPC0154\pytest-19
        print (root_tmp_dir)

        fn = root_tmp_dir / "data.json"
        with FileLock(str(fn) + ".lock"):
            if fn.is_file():
                data = json.loads(fn.read_text())
            else:
                data = get_token()
                fn.write_text(json.dumps(data))
        return data

    def test_getMember(self, token, userid="Candice"):
        params = {
            "access_token": token,
            "userid": userid
        }
        res = requests.get("https://qyapi.weixin.qq.com/cgi-bin/user/get", params=params)
        return res.json()