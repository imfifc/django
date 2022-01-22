from django.http.request import QueryDict
# 一个键对应多个值
# request.POST 和 request.GET 的 QueryDict 在一个正常的请求/响应循环中是不可变的。若要使其改变，需要使用 copy() 方法。
from django.http.request import QueryDict
from django.utils.datastructures import MultiValueDict

d = MultiValueDict({'name': ['Adrian', 'Simon'], 'position': ['Developer']})

print(d['name'])
print( d.getlist('name'))
print( d.getlist('doesnotexist'))
print( d.getlist('doesnotexist', ['Adrian', 'Simon']))  # default
print( d.get('lastname', 'nonexistent'))
print( d.setlist('lastname', ['Holovaty', 'Willison']))
print( d.get('lastname', 'nonexistent'))

"""shell
QueryDict("a=1&b=2&c=3")
<QueryDict: {'a': ['1'], 'b': ['2'], 'c': ['3']}>

QueryDict.fromkeys(['a','b','c'],value="1")
<QueryDict: {'a': ['1'], 'b': ['1'], 'c': ['1']}>

QueryDict('a=1&b=2&c=3', mutable=True).pop("a")
['1']

q = QueryDict('a=1&a=2&c=3', mutable=True) # mutable 表示 q可变
q.popitem()
('c', ['3'])

q = QueryDict('a=1&a=2&a=3')  # 重复值，只返回最后一个
q.items()
<generator object MultiValueDict.items at 0x0000017832913970>
list(q.items())
[('a', '3')]

q.values()                  # 重复值，只返回最后一个
<generator object MultiValueDict.values at 0x0000017832913970>
list(q.values())
['3']

q = QueryDict('a=2&b=3&b=中国')
q.urlencode()
'a=2&b=3&b=%E4%B8%AD%E5%9B%BD'

q = QueryDict('?a=2&b=3&b=中国')
q.urlencode(safe="?")    # 使用 safe 参数传递不需要编码的字符
'?a=2&b=3&b=%E4%B8%AD%E5%9B%BD'


q = QueryDict('a=1',mutable=True)  # updata 仅 追加
q.update({"a":2})
q.getlist('a')
['1', 2]
"""