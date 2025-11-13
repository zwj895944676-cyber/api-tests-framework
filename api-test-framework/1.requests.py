import requests

# url = "http://116.62.63.211/shop/api.php?application=app&application_client_type=weixin"


### 1.方法
# # GET方法
# requests.get(url)
# # POST方法
# requests.post(url)
#
# # 任意方法
# requests.request("MOVE",url)
#
#
#
# ### 2.头
# method="post"
# url = "https://restcountries.com/v3.1/name/china"
#
# requests.request(
#     method,url,
#     headers={ # 字符串字典
#         "1": "a",
#         "2": "b",
#
#     }
# )

### 3. 参数
method="post"
url = "http://116.62.63.211/shop/api.php?application=app&application_client_type=weixin"

# 对象
resp = requests.request(
    method,url,
    json={
        "a": 1,
        "b": [1,2,3],
        "c": {},
    }
)

# resp是对象
# print(type(resp))
# print("-"*70)
# print(resp.status_code) # 状态码
# print("-"*70)
# print(resp.headers) # 响应头
# print("-"*70)
# # print(resp.text) # 响应正文
# print("-"*70)
print(resp.json()) # 响应正文转成JSON

# assert resp.status_code == 200
# assert 'msg' in resp.text
# assert resp.json()['data']['navigation'][0]['name'] == '分类'

# 断言全部的内容
from responses_validator import validator

validator(
    resp,
    status_code=200,
    text='*success*',
    json={'data':
              {'navigation':
               [{'name':'分类'}]}}
)

from commons.extract_utils import extract

# var = extract(resp,'json','$..data.navigation[0].name')
var = extract(resp,'json','$...navigation[0].name')

print(var)

