__author__ = 'Administrator'
#coding=utf8

import pymssql
import xlrd
import os

class MSSQL:
    def __init__(self,host,user,pwd,db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    def __GetConnect(self):
        """
        得到连接信息
        返回: conn.cursor()
        """
        if not self.db:
            raise(NameError,"没有设置数据库信息")
        self.conn = pymssql.connect(host=self.host,user=self.user,password=self.pwd,database=self.db,charset="utf8")
        cur = self.conn.cursor()
        if not cur:
            raise(NameError,"连接数据库失败")
        else:
            return cur

    def ExecQuery(self,sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()

        #查询完毕后必须关闭连接
        self.conn.close()
        return resList

    def ExecNonQuery(self,sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()

def getline(path,ms):
    xlsfile = xlrd.open_workbook(path)
    sheet_name = xlsfile.sheet_names()
    mysheet = xlsfile.sheet_by_name(str(sheet_name[0]))
    head_name = mysheet.row_values(0)
    head_len = len(head_name)
    create_string = "CREATE TABLE %s (" % (str(sheet_name[0]).upper())
    for i in head_name:
        if i != str(head_name[head_len-1]):
            create_string +="%s VARCHAR(MAX),"%(str(i))
        else:
            create_string += "%s VARCHAR(MAX))"%(str(i))
    ms.ExecNonQuery(create_string)
    col = mysheet.ncols
    row = mysheet.nrows
    for j in range(1,row):
        insert_string = "insert into %s values (" %(str(sheet_name[0]).upper())
        for k in range(0,col):
            if k != col-1:
                insert_string += "'%s'," % (str(mysheet.cell(j,k).value))
            else:
                insert_string += "'%s')" % (str(mysheet.cell(j,k).value))
        print(insert_string)
        ms.ExecNonQuery(insert_string)

def getfile(path,ms):
    abspath = os.path.abspath(path)
    dirlist = os.listdir(abspath)
    for x in dirlist:
        curpath = os.path.join(abspath,x)
        if os.path.isfile(curpath):
            if os.path.splitext(curpath)[1] == '.xls':
                getline(curpath,ms)
        else:
            getfile(curpath,ms)


def main():
    ms = MSSQL(host="localhost",user="sa",pwd="*****",db="Database")
    getfile('D:\PycharmProjects\Python_execises\excel',ms)

if __name__ == '__main__':
    main()