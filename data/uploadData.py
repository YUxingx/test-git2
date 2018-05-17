#coding=utf-8
import requests,unittest,json
class TestUploadDataAPI(unittest.TestCase):
    '''测试 data?action=upload&owneruuid=&type=&body= 接口'''
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
    def test_uploadData1(self):
        '''测试upload data接口用例1'''
        data={
            'action':'upload','owneruuid':'914c232b18442c8de2946969227095c6',
              'type':'rawscan','body':r'D:\design\rawscan.tar.gz'}
        r=sess.post(url=url,data=data,verify=r'D:\com.meidaitech.developer.0x05.1.p12')
        text=json.dumps(r.json(),indent=3,ensure_ascii=False)
        code=r.status_code
        print('upload data接口测试用例1：')
        print('响应文本：\n',text)
        print('返回状态码：\n',code)
        print('-------------------------------------------------------------------')
        self.assertEqual(code,200)
        self.assertTrue('true' in text)
    def test_uploadData2(self):
        '''测试upload data接口用例2'''
        data={
            'action':'upload','owneruuid':'914c232b18442c8de2946969227095c6',
              'type':'config','body':r'D:\design\a.config'}
        r=sess.post(url=url,data=data,verify=r'D:\com.meidaitech.developer.0x05.1.p12')
        text=json.dumps(r.json(),indent=3,ensure_ascii=False)
        code=r.status_code
        print('upload data接口测试用例2：')
        print('响应文本：\n',text)
        print('返回状态码：\n',code)
        print('-------------------------------------------------------------------')
        self.assertEqual(code,200)
        self.assertTrue('true' in text)





