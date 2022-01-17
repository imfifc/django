from django.db import models

"""
#定义该model在数据库中的表名称
　　db_table = 'Students'
#使用自定义的表名，可以通过以下属性
　　table_name = 'my_owner_table'
"""


# Create your models here.
class Book(models.Model):  # 创建 book 表
    title = models.CharField(max_length=30, unique=True, verbose_name='书名')
    public = models.CharField(max_length=50, verbose_name='出版社')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='定价')

    def default_price(self):
        return '￥30'

    retail_price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='零售价', default=default_price)

    def __str__(self):
        return "title:%s pub:%s price:%s" % (self.title, self.public, self.price)


class Author(models.Model):  # 创建作者表
    name = models.CharField(max_length=30, verbose_name='姓名')
    email = models.EmailField(verbose_name='邮箱')

    def __str__(self):
        return '作者：%s' % (self.name)


class UserInfo(models.Model):  # 创建用户信息表
    username = models.CharField(max_length=24, verbose_name='用户注册')
    password = models.CharField(max_length=24, verbose_name='密码')

# python .\manage.py makemigrations
# python .\manage.py migrate
# python .\manage.py shell

# 创建Book实例化对象
book = Book(title="Python", public="a", price="59.00", retail_price="59.00")
book.save()  # 调用save方法进行保存
book = Book(title="Flask", public="b", price="39.00", retail_price="39.00")
book.save()  # 调用save方法进行保存
book = Book(title="Django", public="b", price="40.00", retail_price="40.00")
book.save()  #

Book.objects.create(title="Java",public="a",price="30.00",retail_price="30.00")
Book.objects.create(title="MySQL",public="c",price="35.00",retail_price="35.00")
Book.objects.create(title="C#",public="a",price="45.00",retail_price="40.00")
Book.objects.create(title="Redis", public="c", price="25.00", retail_price="25.00")
# 1) 抽象基类
"""
关于 Model 的元数据继承关系，遵循以下几个规则：
抽象基类中定义的元数据，子类中没有定义，子类会继承基类中的元数据；
抽象基类中定义的元数据，子类也定义了，子类优先级更高；
子类可以定义自己的元数据，即不出现在抽象基类中的元数据。

"""
"""

class AbstractBase(models.Model):
    id = models.AutoField()
    content = models.CharField(max_length=100)
    username = models.CharField(max_length=80)
    nowday = models.DateTimeField()

    class Meta:
        abstract = True


# 继承
class SomeThing(AbstractBase):
    testexams = models.CharField(max_length=50)


class SomeComment(AbstractBase):
    level = models.CharField(max_length=20)

"""
# 2) 多表继承

# class a(A):
#     testname = models.CharField(max_length=255, help_text="测试")


"""
多表继承与抽象基类有一个显著的不同点是 Meta 内部类的继承：子类不会继承父类的 Meta 定义。但是，有两个 Meta 元数据项比较例，它们分别是 ordering 和 get_latest_by，
它们是会被子类继承的，所以，如果不想让它们影响子类的行为，应该覆盖这两个元选项。比如父类有了排序设置，而你并不想让子类有任何排序设置，你可以使用如下方式来禁用子类的排序："""


# class ChildModelName(ParentModelName):
#     class Meta:
#         ordering = []  # 子表将不会排序
#         get_latest_by = None


# 3) 代理继承  代理模型用来给父 Model 添加一些方法或者修改其 Meta 选项，但是父 Model 的字段定义不会被修改。
# 这里需要注意的是代理模型不会在数据库中创建新的数据表，它将使用父 Model 的数据表，即对代理模型的 CURD 操作将会作用到原始的 Model 中。

class BookExtend(Book):
    """
    BOOK代理模型
    """

    class Meta:
        ordering = ['id']  # 定义Meta选项顺序排序按照id字段
        proxy = True  # 设置代理模型  提示：最后需要注意的是代理只能继承自一个非抽象的基类，并且不能同时继承多个非抽象基类。

    def __str__(self):
        return "title:%s pub:%s price:%s" % (self.title, self.pub, self.price)  # 定义方法
