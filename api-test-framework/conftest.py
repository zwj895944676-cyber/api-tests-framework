import pytest
from datetime import datetime


# @pytest.fixture(scope="session")
# def ff():
#     print("大框架开始准备")
#     yield 123
#     print("大框架准备结束")

@pytest.fixture(autouse=True,scope="session")
def f():
    print("用例前置操作：链接数据库、启动浏览器、生成测试数据")

    print(datetime.now(),"开始执行用例")
    # 前置操作
    yield 456

    # 后置操作
    print(datetime.now(),"用例执行结束")

    print("用例后置操作：关闭数据库、退出浏览器、删除测试数据")