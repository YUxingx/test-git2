#coding=utf-8
import requests,unittest,json
class TestCreateDealAPI(unittest.TestCase):
    '''测试 deal?action=create&owneruuid=&config= 接口'''
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
    def test_createDeal1(self):
        '''测试create deal接口用例1'''
        data={'action':'create','owneruuid':'914c232b18442c8de2946969227095c6',
              'config':'9fc7dd2e388d0e6de0de2703021b785b'}
        r=sess.post(url=url,data=data)
        text=json.dumps(r.json(),indent=3,ensure_ascii=False)
        code=r.status_code
        print('create deal接口测试用例1：')
        print('响应文本：\n',text)
        print('返回状态码：\n',code)
        print('-------------------------------------------------------------------')
        self.assertEqual(code,200)
        self.assertTrue('true' in text)




