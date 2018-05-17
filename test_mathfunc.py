#coding=utf-8
import unittest
from mathfunc import *
class TestMathFunc(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('准备环境\n')

    def test_add(self):
        '''测试 add(a,b)函数'''
        print('add')
        self.assertEqual(10,add(4,6))
    def test_minus(self):
        '''测试 minus(a,b)函数'''
        print('minus')
        self.assertEqual(50,minus(100,50))
    def test_multi(self):
        '''测试 multi(a,b)函数'''
        print('multi')
        self.assertEqual(63,multi(7,9))
    def test_divide(self):
        '''测试 divide(a,b)函数'''
        print('divide')
        self.assertEqual(1,divide(6,6))

    @classmethod
    def tearDownClass(cls):
        print('环境清理')



