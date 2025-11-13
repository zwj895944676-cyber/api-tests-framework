import yaml

def load_yaml(path):
    """
    处理加载yaml文件的数据，并返回字典类型数据
    :param path:需要处理的数据文件
    :return:返回字典类型
    """
    # 打开文件
    f = open(path, encoding="utf-8")
    # 读取文件内容
    s = f.read()
    data = yaml.safe_load(s)
    return data

