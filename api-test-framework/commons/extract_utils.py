# -*- coding:utf-8 -*-

"""
将返回的json()进行提取变量
"""

import jsonpath

def extract(resp,attr_name,exp):
    """

    :param resp: 响应
    :param attr_name: 用什么格式
    :param exp: 按照什么表达式进行提取
    :return: 提取的变量
    """

    try:
        resp.json = resp.json()
    except Exception:
        resp.json = {}


    attr = getattr(resp,attr_name)
    res = jsonpath.jsonpath(attr,exp)
    return res[0]


