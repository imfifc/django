from django.db import models
from django.db import connection

"""
#定义该model在数据库中的表名称
　　db_table = 'Students'
#使用自定义的表名，可以通过以下属性
　　table_name = 'my_owner_table'
"""


# 新建出版社表 ：  一个出版社可以出版多本书
class PubName(models.Model):
    pubname = models.CharField('名称', max_length=255, unique=True)


# Create your models here.
class Book(models.Model):  # 创建 book 表
    title = models.CharField(max_length=30, unique=True, verbose_name='书名')
    # public = models.CharField(max_length=50, verbose_name='出版社')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='定价')

    def default_price(self):
        return '￥30'

    retail_price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='零售价', default=default_price)
    pub = models.ForeignKey(to=PubName, on_delete=models.CASCADE, null=True)  # 创建Foreign外键关联pub,以pub_id关联

    def __str__(self):
        return "title:%s pub:%s price:%s" % (self.title, self.pub, self.price)


class Author(models.Model):  # 创建作者表
    name = models.CharField(max_length=30, verbose_name='姓名')
    email = models.EmailField(verbose_name='邮箱')

    def __str__(self):
        return '作者：%s' % (self.name)


class UserInfo(models.Model):  # 创建用户信息表
    username = models.CharField(max_length=24, verbose_name='用户注册')
    password = models.CharField(max_length=24, verbose_name='密码')
    # 定义chocies参数的对应关系，以元组（或者列表）的形式进行表述：
    # choices = (
    #     (male, '男性'),
    #     (female, '女性'),
    # )
    # gender = models.CharField(max_length=2, choices=choices, default='male')


# python .\manage.py makemigrations
# python .\manage.py migrate
# python .\manage.py shell

"""
# 创建Book实例化对象
book = Book(title="Python", public="a", price="59.00", retail_price="59.00")
book.save()  # 调用save方法进行保存
book = Book(title="Flask", public="b", price="39.00", retail_price="39.00")
book.save()  # 调用save方法进行保存
book = Book(title="Django", public="b", price="40.00", retail_price="40.00")
book.save()  #

Book.objects.create(title="Java", public="a", price="30.00", retail_price="30.00")
Book.objects.create(title="MySQL", public="c", price="35.00", retail_price="35.00")
Book.objects.create(title="C#", public="a", price="45.00", retail_price="40.00")
Book.objects.create(title="Redis", public="c", price="25.00", retail_price="25.00")

"""

# 创建PubName实例化对象pub1并插入书籍信息
pub1 = PubName.objects.create(pubname="清华出版社")
Book.objects.create(title="Python", price="59.00", retail_price="59.00", pub=pub1)
Book.objects.create(title="Redis", price="25.00", retail_price="25.00", pub=pub1)
Book.objects.create(title="Java", price="45.00", retail_price="45.00", pub=pub1)
# 创建PubName实例化对象pub2并插入书籍信息
pub2 = PubName.objects.create(pubname="c语言中文网出版")
Book.objects.create(title="Django", price="65.00", retail_price="65.00", pub=pub2)
Book.objects.create(title="Flask", price="45.00", retail_price="45.00", pub=pub2)
Book.objects.create(title="Tornado", price="35.00", retail_price="35.00", pub=pub2)

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
        ordering = ["add_time"]  # 按照升序排序
        # ordering = ["-add_time"]  # 按照降序
        # ordering = ["?add_time"]  # 随机排序
        # # 同时指定多个字段来进行排序
        # ordering = ['add_time', '-last_login_time']  # 先按升序，在按降序
        verbose_name_plural = None  # 模型类的复数名
        # 定义该model在数据库中的表名称
        db_table = 'Students'
        # 使用自定义的表名，可以通过以下属性
        table_name = 'my_owner_table'
        app_label = 'app_name'  # 你的模型不在默认的应用程序包下的 models.py 文件中，这时候需要指定你
        managed = True  # 自动创建多对多的 中间表
        indexs = None  # 索引
        default_permissions = ('add', 'change', 'delete', 'view')
        permissions = [('have_read_permission', '有读的权限')]  # permissions=[(权限代码，权限名称)]
        unique_together = (("first_name", "last_name"),)  # 一个 ManyToManyField 不能包含在 unique_together 中。如果你需要验证 ManyToManyField 字段的唯一验证，尝试使用 through 属性进行关联。
        db_tablespace = None  # 常用于 Oracle、PostgerSQL 数据库。MySQL 数据库不支持表空间,忽略
        get_latest_by = "order_date"  # model 的属性名字, 这个设置让你在使用模型管理器的 lastest() 方法时，默认使用order_date指定字段来排序。
        order_with_respect_to = None #  这个选项一般用于多对多的关系中，它指向一个关联对象并将该对象进行排序，使用元数据项后你会得到一个 get_xxx_order() 和set_xxx_order() 的方法，通过它们你可以设置或者得到排序的对象。


# 继承
class SomeThing(AbstractBase):
    testexams = models.CharField(max_length=50)


class SomeComment(AbstractBase):
    level = models.CharField(max_length=20)

"""
# 2) 多表继承

# class a(A):
#     testname = models.CharField(max_length=255, help_text="测试")

# 如果你想指定链接父类的属性名称，你可以创建你自己的 OneToOneField 字段,并且设置 parent_link=True 从而使用该字段链接父类

"""
多表继承与抽象基类有一个显著的不同点是 Meta 内部类的继承：子类不会继承父类的 Meta 定义。但是，有两个 Meta 元数据项比较例，它们分别是 ordering 和 get_latest_by，
它们是会被子类继承的，所以，如果不想让它们影响子类的行为，应该覆盖这两个元选项。比如父类有了排序设置，而你并不想让子类有任何排序设置，你可以使用如下方式来禁用子类的排序："""


# class ChildModelName(ParentModelName):
#     class Meta:
#         ordering = []  # 子表会继承这个字段 ，覆盖后将不会排序
#         get_latest_by = None  # 子表会继承这个字段


# 3) 代理继承  代理模型用来给父 Model 添加一些方法或者修改其 Meta 选项，但是父 Model 的字段定义不会被修改。
# 这里需要注意的是代理模型不会在数据库中创建新的数据表，它将使用父 Model 的数据表，即对代理模型的 CURD 操作将会作用到原始的 Model 中。

class BookExtend(Book):
    """
    BOOK代理模型
    """

    class Meta:
        ordering = ['id']  # 定义Meta选项顺序排序按照id字段
        proxy = True  # 设置代理模型  代理只能继承自一个非抽象的基类，并且不能同时继承多个非抽象基类。

    def __str__(self):
        return "title:%s pub:%s price:%s" % (self.title, self.pub, self.price)  # 定义方法


# Author.objects.create(name="Tom",email="456789@163.com") #添加 Tom 此时数据表有两个Tom
# Author.objects.get_or_create(name="Xiaolong")
"""
#使用 Django shell
Author.objects.create(name="Tom",email="456789@163.com") #添加 Tom 此时数据表有两个Tom
Author.objects.get(name="Tom") #查询 name="Tom",就会报错
#报错信息如下
MultipleObjectsReturned: get() returned more than one Author -- it returned 2!
#查询不存在数据
Author.objects.get(id=4)
#报错信息如下：
DoesNotExist：Traceback (most recent call last)

get_or_create方法和 get 区别在于，当被查询数据不存在的时候，get_or_create 方法会创建新的实例对象，而 get 方法会抛出DoesNotExist异常。而当这两个方法的查询条件都能够匹配多条数据记录时，都会抛出MultipleObjectsReturned异常。
提示：这两个方法都只能返回一条数据。
"""

# 原生数据库操作
#  raw 方法的返回值是一个 RawQuerySet 对象，该对象支持索引和切片，同样也可以对它进行迭代得到 Model 实例对象。但是，与 QuerySet 不同的是，它不能执行 fillter、exclude 等方法。

with connection.cursor() as cur:
    # 调用游标对象的execute方法，更新author的名字
    cur.execute('update index_author set name="Jack"  where id=4;')
    # 删除id为3的一条author记录
    cur.execute('delete from index_author where id=3;')
