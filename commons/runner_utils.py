import requests
import responses_validator
from commons.extract_utils import extract
import logging

logger = logging.getLogger("api_logger")

def runner(k, v, my_var):

    match k:
        # 发送请求
        case 'request':
            logger.info('1. 正在发送请求')
            logger.info(f'{v}')
            # 创建空字典中的键值对，输入的参数是字典，用**v，返回响应数据。'resp'为key，返回响应数据为value，组成key:value
            my_var['resp'] = requests.request(**v) # 字典使用

        # 断言响应
        case 'response':
            logger.info('2. 正在断言响应')
            logger.info(f'{v}')
            # 在发送请求中得到响应数据，通过响应断言工具，输入test_api.yaml中的'response'中的参数，参数是字典，用**v
            responses_validator.validator(my_var['resp'],**v) # 字典使用

        # 变量提取
        case 'extract':
            logger.info('3. 正在提取变量')
            # test_api.yaml中的'extract'字典，v为字典，key为token，value为列表[ json, $data.token]，再将列表[ json, $data.token]通过封装函数extract，最后就是value = extract(my_var['resp'], json, $data.token)
            for var_name,var_exp in v.items():
                value = extract(my_var['resp'],*var_exp) # 列表使用
                logger.info(f'{var_name}     = {value}')
        # 查询数据库。。。等
