from xiaobai_API.common.initPath import DATADIR
from xiaobai_API.common.getConfig import myCof
import pandas as pd
from openpyxl import load_workbook
import os

filename = myCof.getValue('case','testCase')
path = os.path.abspath(filename)
caseFile_path = os.path.join(DATADIR,filename)

def append_to_excel(caseFile_path,dataframe)->None:
    writer=pandas.ExcelWriter(caseFile_path,mode='w')#这里的mode需要用w模式，a模式会产生新的sheet
    data=pandas.read_excel(writer,index_col=None,header=None)
    data.to_excel(writer,startrow=0,index=None,header=None,sheet_name='Sheet3')
    dataframe.to_excel(writer,startrow=data.shape[0],index=None,header=None,sheet_name='Sheet3')
    writer.save()

def test():
    result2=[('a','2','ss'),('b','2','33'),('c','4','bbb')]#列表数据
    writer = pd.ExcelWriter(caseFile_path,engine='openpyxl',mode='a')#可以向不同的sheet写入数据,engine='openpyxl'追加模式
    book=load_workbook(caseFile_path)
    writer.book = book
    df = pd.DataFrame(result2,columns=['xuhao','id','name'])#列表数据转为数据框
    df.to_excel(writer, sheet_name='Sheet5')#将数据写入excel中的Sheet3表,sheet_name改变后即是新增一个sheet
    writer.save()#保存


if __name__ == '__main__':
    # df = pandas.DataFrame([['dedasd', '3','223']], columns=None, index=None)
    # append_to_excel('a.xlsx',df)
    #test()
    