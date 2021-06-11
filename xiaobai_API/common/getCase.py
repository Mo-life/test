import os
import pandas as pd
from xiaobai_API.common.initPath import DATADIR
from xiaobai_API.common.getConfig import myCof
from pprint import pprint



#casefile = os.path.join(DATADIR,'testcase.xlsx')
# print(casefile)
#testcol = pd.read_excel(casefile,sheet_name='Sheet1')
# testcol1 = pd.read_excel(casefile,sheet_name = None)

# tc =  pd.read_excel(casefile,sheet_name='Sheet1')
# header = list(tc)
# datas = tc.values
# Tcases = []
# for data in datas:
#     data = list(data)
#     Tcase = {}
#     count = 0
#     for bt in header:
#         value = data[count]
#         Tcase[bt] = value
#         count += 1
#     print('='*30)
#     Tcases.append(Tcase)
# pprint(Tcases)



#print('testcol = ',testcol)
#print(list(testcol)) #获取所有表头
#print(list(testcol1))  #获取所有sheet页名
#print(f'所有表头：{testcol.columns.values}')

# for i in testcol.columns.values:
#     print(i)



class Getcase():
    def __init__(self):
        """
        初始化文件名称，sheet名称,excel对像
        :param sheet_name: 传入的sheet名称 ，可以为空，默认为0。
        Config()，继承父类，并实例化
        """
        filename = myCof.getValue('case','testCase')
        self.note = myCof.getValue('identifier','note')
        self.caseFile = os.path.join(DATADIR,filename)
        self.wksheet = False

    def getSheetname(self,sheet_name = None):
        """
        打开excel文件
        如果sheet名称存在，定位到对应的sheet页
        :return:self.wksheet 判断是否有效
        """

        if sheet_name in pd.ExcelFile(self.caseFile).sheet_names:
            self.sheet_name = sheet_name
            sh = pd.read_excel(self.caseFile,sheet_name=self.sheet_name)#定位到sheet页
            if sh.empty is True:    #sheet页为空时，True 为空，False为非空
                return print(sheet_name,'为空'),self.wksheet is False
            #elif sh.keys != sheetkey:  留一个判断表头的接口
            #    pass
            else:
                self.sh = pd.read_excel(self.caseFile,sheet_name=sheet_name)     #定位到sheet页，self.sh 获得的内容
                self.header = list(self.sh)                                      #获得表头
                self.wksheet = True
                return print('不为空')
        elif sheet_name is None:
            self.sheet_name = pd.ExcelFile(self.caseFile).sheet_names
            return print('一群',self.sheet_name)
        else:
           return print(sheet_name,'不存在'),self.wksheet is False

        #header = list(sh) 用法等于 list(sh.keys()))  获得sheet页面名列表，或者sheet页内表头列表
        # print('====',list(sh.keys()))
        # print(type(self.sheet_name))
        # if self.sheet_name in list(sh.keys()):
        #     sh = pd.read_excel(self.caseFile,sheet_name=self.sheet_name) #定位到sheet页
        #     print(sh)
        #     for sheet_name in sh:
        #         if 'Empty DataFrame' in str(sh[sheet_name]):
        #             print(sheet_name, '为空')
        #             continue
        #         else:
        #             self.sh = sh
        #             self.wksheet = True
        #             return f'{self.sheet_name} 为空',self.wksheet is False
        #
        # else:
        #     return print(f'{self.sheet_name} 不存在'),self.wksheet is False

    def read_excels(self,sheet_name):   #读取单个sheet页必须输入名称
        """
        格式化用例集
        用例JSON格式化
        过滤掉#注释的用例
        :return:指定sheet页上的所有测试用例（json格式）
        """
        self.getSheetname(sheet_name)   #定位Sheet页
        if self.wksheet == True:
            Tcases = []
            for value in self.sh.values:
                Tcase = dict(zip(self.header,value))
                try:
                    if str(Tcase['case_id'])[0] is not self.note:   # 过滤掉note符号开头的用例，注释掉不收集、不执行
                        Tcase['sheet'] = self.sheet_name
                        Tcases.append(Tcase)                        #将数据格式化中JSON串
                except KeyError:
                    Tcases.append(Tcase)                            #将数据格式化中JSON串
            return Tcases
        else:
            return print('用例json格式化失败')

    def read_all_excels(self):  #读取全部sheet用例
        """
        遍历所有的sheet页
        取得所有用例集，再格式下一次，
        过滤掉#注释的sheet页
        :return:以列表的形式返回json格式的所有sheet页用例
        """
        self.getSheetname()
        Tcases = []
        for sheet in self.sheet_name:
            Tcases += self.read_excels(sheet)
        return Tcases

    def wirter_excels(self,sheet_name ,rows, column, value):
        self.getSheetname(sheet_name)
        wirter_sh = pd.ExcelWriter


# if __name__ == '__main__':
#     try:
#         getC = Getcase()
#         sheet = getC.read_excels('Sheet7')
#         print('sheet = ', sheet)
#     except Exception as e:
#         print(e)
