#coding=utf-8
import requests,unittest,json
class TestQueryDataInfoAPI(unittest.TestCase):
    '''测试 data?action=query&uuid=&type= 接口'''
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
    def test_queryDataInfo1(self):
        '''测试query data information接口用例1'''
        data={
            'action':'query','uuid':'1b4c59a08774d854ef815a439dca7db2',
              'type':'rawscan','chunk':''}
        r=sess.post(url=url,data=data)
        text=json.dumps(r.json(),indent=3,ensure_ascii=False)
        code=r.status_code
        print('query data information接口测试用例1：')
        print('响应文本：\n',text)
        print('返回状态码：\n',code)
        print('-------------------------------------------------------------------')
        self.assertEqual(code,200)
        self.assertTrue('true' in text)
    def test_queryDataInfo2(self):
        '''测试query data information接口用例2'''
        data={
            'action':'query','uuid':'9fc7dd2e388d0e6de0de2703021b785b',
              'type':'config','chunk':''}
        r=sess.post(url=url,data=data)
        text=json.dumps(r.json(),indent=3,ensure_ascii=False)
        code=r.status_code
        print('query data information接口测试用例2：')
        print('响应文本：\n',text)
        print('返回状态码：\n',code)
        print('-------------------------------------------------------------------')
        self.assertEqual(code,200)
        self.assertTrue('true' in text)



