#coding=utf-8
import requests,unittest,json
class TestQueryDealAPI(unittest.TestCase):
    '''测试 deal?action=query&uuid= 接口'''
    global url,sess
    url = 'http://10.10.10.233:7767/deal'
    sess=requests.session()
    @classmethod
    def setUpClass(self):
        pass
    @classmethod
    def tearDownClass(self):
        pass
    #测试该接口的所有用例
    def test_queryDeal1(self):
        '''测试query deal接口用例1'''
        data={'action':'query','uuid':'97f1a71835ecbeb6f675dde7a7a8e600',
             'createdate':'','config':'','owneruuid':''}
        r=sess.post(url=url,data=data)
        text=json.dumps(r.json(),indent=3,ensure_ascii=False)
        code=r.status_code
        print('query deal接口测试用例1：')
        print('响应文本：\n',text)
        print('返回状态码：\n',code)
        print('-------------------------------------------------------------------')
        self.assertEqual(code,200)
        self.assertFalse('false' in text)




