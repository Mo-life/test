import os
# print(os.path.abspath(__file__))                    #获得当前文件的完整路径
# print(f'{os.path.basename(__file__)}1 ')            #获得当前文件名称
# print(os.path.dirname(__file__))                    #获得以/形式的当前文件的目录路径
# print(os.path.dirname(os.path.abspath(__file__)))   #获得以\形式的当前文件的目录路径   Windows系统路径

#get project dir
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#get common dir
COMMONDIR = os.path.join(BASEDIR,'common')
#get config dir
CONFIGDIR = os.path.join(BASEDIR,'config')
#get data dir
DATADIR = os.path.join(BASEDIR,'data')
#get kemel dir
KEMELDIR = os.path.join(BASEDIR,'kemel')
#get library dir
LIBRARYDIR = os.path.join(BASEDIR,'libaray')
#get log dir
LOGDIR = os.path.join(BASEDIR,'log')
#get report dir
REPORTDIR = os.path.join(BASEDIR,'report')
#get testcase dir
TESTCASEDIR = os.path.join(BASEDIR,'testcase')