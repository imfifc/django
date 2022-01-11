from django.test import TestCase


# Create your tests here.
# 直接print打印
class TestClass:
    def __init__(self):
        self.name = 'testcase'


t = TestClass()  # 实例化对象
print(t)  # 结果显示：<__main__.TestClass object at 0x8f5c27b42367>
# __str__方法
class TestClass:
    def __init__(self):
        self.name = '小明'

    def __str__(self):
        return self.name


t = TestClass()  # 实例化对象
print(t) # 结果显示：小明
