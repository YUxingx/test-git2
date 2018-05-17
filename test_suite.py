#coding=utf-8
import unittest,time
import time
from test_mathfunc import TestMathFunc
from HTMLTestRunner import HTMLTestRunner
if __name__=='__main__':
    suite=unittest.TestSuite()#创建一个unittest.TestSuite()类的对象suite，测试套件
    #导入测试用例方法一：导入TestMathFunc类的所有测试用例方法到测试套件
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMathFunc))
    #导入测试用例方法二：要执行的测试方法放在tests列表中
    #tests=[TestMathFunc('test_add'),TestMathFunc('test_minus')]  #某类的某方法，逐一加入
    #suite.addTests(tests) #调用addTests方法添加要执行的用例到测试套件中
    now=time.strftime('%Y-%m-%d-%H_%M_%S')
    #测试报告以html格式保存
    filename=r'.\test_report\report-'+now+'.html'#测试报告的保存路径
    with open(filename,'w',encoding='utf-8') as fb:
        runner=HTMLTestRunner(stream=fb,title='接口自动化测试报告',
                              description='接口测试报告：:',verbosity=2)
        runner.run(suite)
        fb.close()
    # 将结果保存在report.txt文件中
    # file=r'.\test_report\report-'+now+'.txt'
    # with open(file,'a')as f:
    #     runner=unittest.TextTestRunner(stream=f,verbosity=2)#创建unittest.TextTestRunner()类的runner对象
    #     runner.run(suite)#运行测试套件
    #     f.close()



