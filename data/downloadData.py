#coding=utf-8
import requests,unittest,json
class TestDownloadDataAPI(unittest.TestCase):
    '''测试 /data?action=download&uuid=&type= 接口'''
    global url,sess
    url = 'http://10.10.10.233:7767/data'
    sess=requests.session()
    @classmethod
    def setUpClass(self):
        pass
    @classmethod
    def tearDownClass(self):
        pass
    #测试该接口的所有用例
    def test_downloadData1(self):
        '''测试 download data 接口用例1'''
        data={
            'action':'download','uuid':'1b4c59a08774d854ef815a439dca7db2',
              'type':'rawscan'}
        r=sess.post(url=url,data=data)
        text=json.dumps(r.text)
        code=r.status_code
        print('download data接口测试用例1：')
        #print('响应文本：\n',text)
        print('返回状态码：\n',code)
        print('-------------------------------------------------------------------')
        self.assertEqual(code,200)
        self.assertFalse('false' in text)
    def test_downloadData2(self):
        '''测试 download data 接口用例2'''
        data={
            'action':'download','uuid':'9fc7dd2e388d0e6de0de2703021b785b',
              'type':'config'}
        r=sess.post(url=url,data=data)
        text=json.dumps(r.text)
        code=r.status_code
        print('download data接口测试用例2：')
        print('响应文本：\n',text)
        print('返回状态码：\n',code)
        print('-------------------------------------------------------------------')
        self.assertEqual(code,200)




