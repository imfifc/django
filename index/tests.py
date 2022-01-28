import unittest

from index.models import Book, PubName

from django.test import TestCase, tag


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
print(t)  # 结果显示：小明

# 基础功能测试、模型测试、视图测试。
' django.test.TestCase 是 unittest.TestCase 的一个子类，实现了数据库访问以及 HTTP 请求等测试功能。 test_models.py、test_views.py '
"""
 python manage.py test 对所有测试
 python manage.py test -v 3 index.tests

执行 index 应用下的所有测试用例： python manage.py test index。
执行 index应用下 tests 模块下定义的测试用例：  python manage.py test.index.tests。
直接执行 tests.py 文件下测试类：python manage.py test index.tests.ExampleTest。
直接执行测试类下某个测试方法：python manage.py test index.tests.ExampleTest.test_view。
可以使用数字 0、1、2、3 来指定详细程度，数字越大表示输出越详细，只有这 4 个级别可选则
"""


# 1) 标记测试  python manage.py test --tag=tagone --tag=tagsecond --exclude-tag=tagsecond  index.tests.ExampleTest
# python manage.py test index.tests.ExampleTest

class ExampleTest(TestCase):
    def setUp(self):
        print('我负责测试环境初始化')
        self.pub1 = PubName.objects.create(pubname="编程帮出版")

    @tag('tagone')  # 添加标记
    def test_model(self):
        print('执行test_model测试')
        book = Book.objects.create(title='Servlet', price='35.00', retail_price='35.00', pub=self.pub1)
        self.assertTrue(book is not None)
        self.assertNotEqual(Book.objects.count(), 8)
        self.assertEqual(Book.objects.count(), 1)

    @tag('tagsecond')  # 添加标记
    def test_view(self):
        print('执行test_view测试')
        book = Book.objects.create(title='Jsp', price='25.00', retail_price='25.00', pub=self.pub1)
        response = self.client.get('/index/update_book/%d/' % book.id)  # 视图访问获取response
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        print('我负责清理测试环境')


class ExampleTest2(TestCase):
    def test_addition(self):
        def addition(x, y):
            return x + y

        self.assertEqual(addition(1, 1), 2, 'ass is failed')  # 断言函数加和运算


# 虽然这里涉及到了数据库操作，但是该操作并不会影响数据库中原有数据。这些测试用例是相互隔离的，每一个测试用例都运行在一个事务中。
def test_model(self):
    pub1 = PubName.objects.create(pubname="程序帮出版社")  # 创建pubname实例，
    book = Book.objects.create(title='Servlet', price='35.00', retail_price='35.00', pub=pub1)
    self.assertTrue(book is not None)
    self.assertNotEqual(Book.objects.count(), 8)  # 使用断言判断
    self.assertEqual(Book.objects.count(), 9)


def test_view(self):
    pub1 = PubName.objects.create(pubname="机械工业出版社")
    book = Book.objects.create(title='Jsp', price='25.00', retail_price='25.00', pub=pub1)
    response = self.client.get('/index/update_book/%d/' % book.id)
    response['X-Token'] = 'C语言中文网'  # 自定义响应头
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response['X-Token'], 'C语言中文网', 'it is not same')


# 2) Django内置断言方法
# python manage.py test -v 1 index.tests.ExampleTest3


class ExampleTest3(TestCase):
    def test_assert1(self):
        """
        django内置断言的方法测试
        """
        # 用来断言可执行对象的调用引发了异常，且在异常中发现了对应的信息
        with self.assertRaisesMessage(ValueError, 'invalid literal for int()'):
            int('a')

    def test_assert2(self):
        # 判断HTML是否相等基于HTML语义，常用来检验返回模板的视图
        self.assertHTMLEqual("<p>hello c.biancheng.net</p>", " <p>hello c.biancheng.net</p>")
        self.assertHTMLNotEqual("<p>hello c.biancheng.net</p>", "<p>hello c.biancheng.net</p>")

    def test_assert3(self):
        # 用来断言JSON字符串是否相等，校验JsonResponse视图返回对象
        self.assertJSONEqual('{"name":"John","age":15}', '{"age":15,"name":"John"}')
        self.assertJSONNotEqual('{"a":1,"b":2}', '{"a":2,"c":1}')

    def test_asseret4(self):
        # 断言查询集合是否与给定的列表内容相等，给定列表也可包含多个元素
        self.pub1 = PubName.objects.create(pubname="编程帮出版")
        book = Book.objects.create(title='Servlet', price='35.00', retail_price='35.00', pub=self.pub1)
        # repr(a)将对象a转换为字符串格式
        self.assertQuerysetEqual(Book.objects.all(), [repr(book)])


# coverage统计测试代码覆盖率, 它不能说明代码的质量高
# coverage run --source='.' manage.py test
#  htmlcov 的文件夹，使用浏览器打开其中的 index.html

# PS C:\Users\Administrator\Desktop\book\BookStore> coverage report --skip-covered
# Name                               Stmts   Miss  Cover
# ------------------------------------------------------
# BookStore\asgi.py                      4      4     0%
# BookStore\wsgi.py                      4      4     0%
# index\admin.py                        16      1    94%
# index\auth.py                         34     34     0%
# index\forms.py                        59     21    64%
# index\models.py                       49      5    90%
# index\query.py                        12     12     0%
# index\templatetags\index_tags.py      17      5    71%
# index\test.py                         31      7    77%
# index\tests.py                        66     11    83%
# index\views.py                       312    218    30%
# manage.py                             12      2    83%
# middleware\mymiddleware.py            32     10    69%
# mysql.py                              14     14     0%
# user\backends.py                      17     17     0%
# user\models.py                        10      1    90%
# user\signal.py                         7      1    86%
# user\views.py                         89     79    11%
# 账单.py                                 13     13     0%
# ------------------------------------------------------
# TOTAL                                920    459    50%
#
# Stmts：代表语句总数；
# Miss：代表未执行到的语句数；
# Cover：代表测试代码覆盖率，计算公式 Cover=(Stmts-Miss)/Stmts。
#
# '''
