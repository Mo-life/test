import os
from xiaobai_API.common.initPath import CONFIGDIR
from configparser import ConfigParser


# conPath = os.path.join(CONFIGDIR,'baseCon.ini')
# print(conPath)
# cnf = ConfigParser()
# cnf.read(conPath,encoding='utf-8')  #第一个参数是被读出文件的路径，第二个是读取参数的编码格式
#
#
# print(f'baseCon.ini里的所有节点{cnf.sections()}')
# print(f'db下所有的参数{cnf.options("db")}')
# print(f'db下所有item：{cnf.items("db")}')
# print(type(cnf.items("db")[0]))
# print(f'db下所有的value:{cnf.get("db","host")}')


class Config(ConfigParser):

    def __init__(self):
        """
        初始化
        将配置文件读出出来
        super().    调用父类
        """
        self.conf_Path = os.path.join(CONFIGDIR,'baseCon.ini')
        super().__init__()
        super().read(self.conf_Path,encoding='utf-8')

    def getAllsections(self):
        """返回所有节点名称"""
        return super().sections()

    def getOptions(self,sectionName):
        """
        options 返回节点所有参数
        sectionName 节点名称
        """
        return super().options(sectionName)

    def getItems(self,sectionName):
        """
        以列表嵌套元组的形式返回节点的参数与值
        :return:
        """
        return super().items(sectionName)

    def getValue(self,sectionName,key):
        """
        :param sectionName: 节点名称
        :param key: 节点的键
        :return: 节点的值
        """
        return super().get(sectionName,key)

    def appendData(self,sectionName,key,value):
        """
        添加配置
        :param sectionName: 节点名称
        :param key: 节点的键
        :param value: 节点的值
        """
        super().set(section = sectionName,option = key,value = value)
        super().write(self.conf_Path,'w')


myCof = Config()