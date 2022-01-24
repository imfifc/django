'''
class Paginator:
    def __init__(self, object_list, per_page, orphans=0,
                 allow_empty_first_page=True)
其中每个参数的含义如下所示：
object_list， 对象列表即查询到的数据。
per_page， 每一页展示的内容，即每页的数据条数。
orphans=0， 为避免最后一页数据过少时设置，若最后一页的数据小于这个值，会合并到上一页，可省略。
allow_empty_first_page=True， 允许首页为空 ，默认为 True。


# 2) Paginator对象的属性

In [1]: from django.core.paginator import Paginator
#待分页的数据
In [2]: objects=['a','b','c','d','e','f','g']
#获取分页器对象
In [3]: p = Paginator(objects, 2)
#需要分类数据的对象总数
In [4]: p.count
Out[4]: 7
#分页后的页面总数
In [5]: p.num_pages
Out[5]: 4
#每一页的数据个数
In [6]: p.per_page
Out[6]: 2
#分页后的页码范围从1开始，不包括5,左闭右开
In [7]: p.page_range
Out[7]: range(1, 5)


# 3) Paginator对象的方法 page()

In [9]: p.page()
#不提供页码返回错误类型
TypeError
TypeError: page() missing 1 required positional argument: 'number'
#获取第2页的page对象
In [10]: pag2=p.page(2)
#返回当前页对象
In [11]: pag2
Out[11]: <Page 2 of 4>
#使用list进行实例化
In [12]: list(pag2)
Out[12]: ['c', 'd']

# 1) Page对象属性
#当前页上所有数据对象的列表
In [14]: pag2.object_list
Out[14]: ['c', 'd']
#当前页的序号，从1开始，第几页
In [15]: pag2.number
Out[15]: 2
#当前page对象相关的Paginator对象，可通它可调用原有的Paginator属性
In [16]: pag2.paginator
Out[16]: <django.core.paginator.Paginator at 0x63b2090>


2) Page对象方法
Page 对象的适应方法也非常的简单在这里就不进行实例讲解了，有兴趣的小伙伴可以自己试一试，如下所示：
len()：返回当前页面对象的个数。
has_next()：如果有下一页返回 True。
has_previous()：如果有上一页返回 True。
has_other_pages()：如果有上一页或下一页返回 True。
previous_page_number()：返回上一页的页码，如果上一页不存在，抛出 InvalidPage 异常。
next_page_number()：返回下一页的页码，如果下一页不存在，抛出 InvalidPage 异常。
start_index()：返回当前页相对于整个列表来说的起始的对象序号，从 1 开始，上例所示将返回 3。
end_index()：返回当前页相对于整个列表来说的结束的对象序号，从 1 开始，上例所示将返回 4。
注意：Page 对象是可迭代对象，可以用 for 语句来 访问当前页面中的每个对象


'''
