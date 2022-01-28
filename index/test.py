import unittest


def score_grade(score):
    if not isinstance(score, int):
        raise TypeError("你应该输入一个整数类型")
    if not (0 <= score <= 100):
        raise Exception("你输入的整数范围应该在0-100之间")
    if 0 <= score < 60:
        return "D"
    elif 60 <= score <= 75:
        return 'C'
    elif 75 < score <= 85:
        return 'B'
    else:
        return 'A'


class TestScore(unittest.TestCase):
    def test_exception(self):
        with self.assertRaises(TypeError):
            score_grade('x')

    def test_score(self):
        self.assertEqual(score_grade(86), 'A')
        self.assertNotEqual(score_grade(86), 'B')
        self.assertTrue(score_grade(86) == 'C')


# PS C:\Users\Administrator\Desktop\book\BookStore> python -m unittest index.test
# PS C:\Users\Administrator\Desktop\book\BookStore> python -m unittest index.test.TestScore

'''
unittest 包含了4 个核心概念，给大家总结如下：
test fixture：它代表的是初始化和清理测试环境，它最常见的使用场景，比如数据库连接的创建与销毁。
test case：它代表的是 unittest.TestCase 类实例，一个完整的测试单元，通过运行这个测试单元实现最终的测试验证。
test suite：它代表的是 test case 的集合，同时 test suite 之间可以进行嵌套，从而达到多个测试任务一起执行的目的。
test runner：它代表的是运行测试用例，然后给用户最终的测试结果。

1) 跳过测试装饰器
跳过测试的功能可以使用装饰器实现，这类装饰器有以下三个：
unittest.skip(reason)：无条件跳过，其中 reason 用来表示跳过测试的原因；
unittest.skipIf(condition,reason)：当条件（condition）成立的时候，跳过测试；
unittestUnless(condition,reason)：与 skipIf 相反，当条件（condition）不成立的时候，跳过测试。


2) 跳过预期失败装饰器
使用unittest.expectedFailure处理预期失败的用例，使用方法和上面的跳过装饰器一样，不过这里有一点需要注意，不管是标注了该装饰器的方法可以通过测试，还是标注了该装饰器的类中有通过测试的方法，它们都会被认为是测试失败即 FAILED，它提供了两个参数，如下所示：
FAILED (expected failures=1, unexpected successes=1)

含义可想而知， expected failures=1 表示使用改装饰器的方法确实测试不通过；unexpected successes=1 表示该方法中某些断言可以测试通过，但并不代表所有断言都通过测试
'''


class SkipTest(unittest.TestCase):
    @unittest.skip('不用测试A用例')
    def test_A(self):
        print('测试A')

    @unittest.skipIf(True, '跳过B')
    def test_B(self):
        print('测试B')

    @unittest.skipUnless(False, '跳过C')
    def test_C(self):
        print('测试C')

    # @unittest.expectedFailure()
    # def test_D(self):
    #     print('测试D')

# python manage.py test -v 3 index.test.SkipTest
#