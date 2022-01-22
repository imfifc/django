from django.db.models import Count
from django import forms
from django.shortcuts import render

# Create your views here.
# 方式一
from django.template import loader  # 导入loader方法
from django.shortcuts import render  # 导入render 方法
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Template, Context  # 调用template、以及上下文处理器方法
from django.urls import reverse
from django.views import View

from index.models import Book, Author, UserInfo, PubName
from index.forms import TitleSearch  # 引入forms.py中定义的TitleSearch类


def test_html(request):
    t = loader.get_template('test.html')
    html = t.render({'name': 'c语言中文网'})  # 以字典形式传递数据并生成html
    return HttpResponse(html)  # 以 HttpResponse方式响应html


# 方式二
# from django.shortcuts import render  # 导入reder方法


def test2_html(request):
    return render(request, 'test.html', {'name': '大大胸'})  # 根据字典数据生成动态模板


def test3_html(request):
    a = {'name': 'C语言中文网',
         'course': ["Python", "C", "C++", "Java"],
         'b': {'name': 'C语言中文网', 'address': 'http://c.biancheng.net/'},
         'test_hello': test_hello,
         'class_obj': Website()
         }  # 创建空字典，模板必须以字典的形式进行传参
    return render(request, 'test3.html', a)


def test_hello():
    return '欢迎来到C语言中文网'


class Website:
    def Web_name(self):
        return 'Hello，C语言中文网!'

    # Web_name.alters_data = True  # 不让Website()方法被模板调用

    """
    注意：在模板中访问对象方法的时候，方法调用不需要加括号，而且只能够调用不带参数的方法；如果不希望自定义的方法被模板调用可以使用 alters_data=Ture 属性，放在方法的结束位置即可
    """


def test_if(request):
    dic = {'x': 2 ** 4}
    return render(request, 'test_if_for.html', dic)


def test_if2(request):
    # 调用template()方法生成模板
    t = Template("""
                        {% if web.name == 'C语言中文网'  %}
                              {% if printable %}
                                     <h1>Hello C语言中文网</h1>
                              {% else %}
                                      <h2>欢迎您下次访问，C语言中文网</h2>
                              {% endif %}
                        {% endif %}
                                      """)
    c = Context({'web': {'name': 'C语言中文网', 'sex': 'man'}, 'printable': False})  # Context必须是字典类型的对象，用来给模板传递数据
    html = t.render(c)
    return HttpResponse(html)


def test_for(request):
    # 调用template()方法生成模板
    t1 = Template("""
                    {% for item in list %}
                        {% if item == "Python" %}
                            <li> {{ item }} is best </li>
                        {% endif %}
                        <li>{{ item }}</li>
                    {% empty %}
                        <h1>如果找不到你想要，可以来C语言中文网(网址：http://httpbin.org/)</h1>
                    {% endfor %}
                              """)
    # 调用 Context()方法
    c1 = Context({'list': ['Python', 'Java', 'C', 'Javascript', 'C++']})
    # c1 = Context({'list': []})
    html = t1.render(c1)
    return HttpResponse(html)


def test_for2(request):
    # 使用嵌套for标签依次遍历列表取值
    website = Template("""
     {% for course in list01 %}
     <div>
        {% for coursename in course %}
        <p><b>{{ forloop.first }}:{{ coursename }}</b></p>
        <p><b>{{ forloop.last }}:{{ coursename }}</b></p>

        <p><b>{{ forloop.counter0 }}:{{ coursename }}</b></p>
        <p><b>{{ forloop.counter }}:{{ coursename }}</b></p>
            
        <p><b>{{ forloop.parentloop }}:{{ coursename }}</b></p>

        {% endfor %}
     </div>
     {% endfor %}
     """)
    webname = Context({'list01': [['Django', 'Flask', 'Tornado'], ['c语言中网', 'Django官网', 'Pytho官网']]})
    html = website.render(webname)
    return HttpResponse(html)


def test_filter(request):
    t = Template("""
    <p>hello:{{value|truncatewords:2}}
    <p>v1 :{{value|length}}
    <p>value2:{{value2|dictsort:"num"}} 空
    
    <p>value3: {{value3|add:2}}
    <p>value4: {{value4|add:list}}
    
     {% for book in books|dictsort:"author.age" %}
        <div><b>{{ book.title }} ({{ book.author.name }})
     {% endfor %}
    """)
    html = t.render(Context({
        'value': "hhe hhh 222 333",
        'books': [
            {'title': 'C语言教程', 'author': {'name': 'ycs', 'age': 14}},
            {'title': 'Python教程', 'author': {'name': 'xxw', 'age': 17}},
            {'title': 'Django教程', 'author': {'name': 'ccs', 'age': 16}}],
        'value3': 3,
        'value4': [1],
        "list": [2, 4],
    }))

    return HttpResponse(html)


def test_url(request):
    return render(request, 'test_url.html')


def Hello_MyWeb(request, id):
    t = Template(
        """
        <p>  id： {{ id }} {{ str }}</p>
        """
    )
    html = t.render(Context({"id": id}))
    return HttpResponse(html)


def user_define_lable(request):
    t = Template("""
        {% load index_tags %}
        {% addstr_tag 'Django BookStore' %}
        """)
    html = t.render(Context())
    return HttpResponse(html)


def inclusion_lable(request):
    # 实际就是去改引用模板的变量
    t = Template("""
    {% load index_tags %}
    {% add_webname_tag 'C 语言中文网——XXX' %}
    """)
    html = t.render(Context({'varible': 'Hello'}))
    return HttpResponse(html)


def assignment_tag(request):
    # 直接赋值
    t = Template("""
    {% load index_tags %}
    {% test_as_tag '语言中文网欢迎你' as test %}   
    <p>{{ test }}</p>
    """)
    html = t.render(Context())
    return HttpResponse(html)


def equal_lable(request):
    t = Template("""
      {% ifequal n1 n2 %}
        <p>{{ n1 }} equal {{ n2 }}</p>
      {% else %}
        <p>{{ n1 }} not equal {{ n2 }} </p>
      {% endifequal %}
       """)
    html = t.render(Context({'n1': 'python', 'n2': 'python'}))
    return HttpResponse(html)


def ifchanged_lable(request):
    t = Template("""
         {% for name in webnames %}
             {% ifchanged %}
             {{name.1|add:'xxxxx'}}
             {% endifchanged %}
         {% endfor %}    
         """)
    html = t.render(Context({'webnames': [['Python', 'Flask'], 'java', 'c语言']}))
    return HttpResponse(html)


def cycle_lable(request):
    # cycle的参数为字符串，用引号引起来
    # cycle参数为变量，需要用字典为其赋值
    """cycle 标签也可与 resetcycle 标签配合使用，resetcycle 表示重置上一个循环，遇到此标签时，将从 cycle 标签的第一个参数重新开始，
     cycle 还提供了关键字 silent，正如它英语含义一样，它表示不输入参数值，只显示循环周期的内容，即不会给 class 属性赋值
    """
    t = Template("""
     {% for i in some_list %}
       <tr>
            <td class="{% cycle v1 v2 %}">...</td>
            <td class="{% cycle 'row1' 'row2' as rowcolors  silent %}">...</td>
            <td class="{{ rowcolors }}">111</td>
        </tr>
        <tr>
            <td class="{% cycle rowcolors %}">...</td>
            <td class="{{ rowcolors }}">222</td>
        </tr>
             <p>{{ i }}</p>
         </tr>^M
     {% endfor %}
     
     {% comment %}
     多行注释  
     {% endcomment %}
     
     {# 单行注释 #}
     """)
    html = t.render(Context({'some_list': ['Python', 'Flask'], "v1": "v1", "v2": "v2"}, autoescape=False))
    return HttpResponse(html)


# 定义父模板视图函数
def base_html(request):
    return render(request, 'index/base.html')


# 定义子模板视图函数
def index_html(request):
    name = 'xiaoming'
    course = ['python', 'django', 'flask']
    return render(request, 'index/test.html', locals())
    # locals() 获取当前环境的局部变量


def user_define_filter(request):
    t = Template("""
        {% load index_tags %}
        <h1> : {{ Web|hello_my_filter }}</h1>
       使用过滤器排序 values|sorted ： {{ values|sorted }}
        """)
    html = t.render(Context({'Web': 'Web django Django', 'values': [9, 1, 4, 3]}))
    return HttpResponse(html)


def redict_url(request):
    return render(request, 'index/newtest.html')


# reverse函数实现反向解析重定向到我们想要的有页面
def test_to_reverse(request):
    """
        上面我们使用 reverse 函数完成了视图函数的重定向，但是这里还要给大家简单介绍一下 reverse() 函数。在 Django中 reverse() 的定义如下所示：
    reverse(viewname,urlconf=None,args=None,kwargs=None,current_app=None)

    它只有一个必填参数，其他都是可选参数。其中 viewname 参数除了可以接受 url 路由 name 的别名以外，还可以接受可调用视图函数对象作为参数。示例如下：
    from BookStore import views
    def test_to_reverse(request):
        return HttpResponseRedirect(reverse(views.test_url))
    其他参数说明如下：
    urlconf：这个属性用于决定当前的反向解析使用哪个 URLconf 模块,默认是根 URLconf；
    args：它用于传递参数，可以是元组或者列表，顺序填充 url 中的位置参数；
    kwargs：字典类型的传参，和 args 作用一样；
    current_app:它指定当前视图函数所在的 app，本例中是 index 应用。
    """
    # return HttpResponseRedirect(reverse('index:detail_hello'))  # 应用名:url 别名
    return HttpResponseRedirect(
        reverse('index:detail_hello', current_app=request.resolver_match.namespace))  # 命令空间 可以满足不同的app 下 相同的path
    # return HttpResponseRedirect(reverse(test_url))  # 应用名:url 别名


# 原生sql
def BookName(request):
    books = Book.objects.raw("select * from index_book")  # 书写sql语句
    return render(request, "index/all_book.html", locals())


# params  %s 传参防注入
def authorname(request):
    authors = Author.objects.raw("select id from index_author where name= %s", ['Tom'])
    t = Template("""
        {% for author in authors %}
        <h1>  {{ author.name }} : {{ author.email}}</h1>
        {% endfor %}
        """)
    html = t.render(Context({"authors": authors}))
    return HttpResponse(html)


# 游标 cursor 对数据库进行增删改操作


def test_annotate(request):
    # 得到所有出版社的查询集合QuerySet
    bk_set = Book.objects.values('price')
    bk = Book.objects.get(id=1)
    print('书名:', bk.title, '出版社是:', bk.pub.pubname)
    # 根据出版社QuerySet查询分组，出版社和Count的分组聚合查询集合
    bk_count_set = bk_set.annotate(myCount=Count('price'))  # 返回查询集合
    for item in bk_count_set:  # 通过外键关联进行查询bk_set.pub.pubname
        print("价格是:", item['price'], "同等价格书籍数量：", item['myCount'])
    return HttpResponse('请在CMD命令行控制台查看结果')


# SELECT `index_book`.`price`, COUNT(`index_book`.`price`) AS `myCount` FROM `index_book` GROUP BY `index_book`.`price` ORDER BY NULL
#          (                  )
# Book.objects.annotate(t=Max('price')).values('id','t')
#  <QuerySet [{'id': 1, 't': Decimal('59.00')}, {'id': 2, 't': Decimal('25.00')}, {'id': 3, 't': Decimal('45.00')}, {'id': 4, 't': Decimal('65.00')}, {'id': 5, 't': Decimal('45.00')}]>#按照values提供的参数分别作为键和值。

# 使用FBV方式
def login_fbv(request):
    if request.method == "GET":
        return HttpResponse("登录成功")
    elif request.method == "POST":
        pass


# 使用CBV方式
class LoginView(View):  # 需要继承自View类
    username = 'xiaoli'

    def get(self, request):
        return HttpResponse("登录成功")

    def post(self, request):
        pass


class LoginViewChild(LoginView):
    # 继承后重写类属性
    username = 'xiaowang'


"""
#第二种方法也可以
urlpatterns = [
   path(r'logincbv/', LoginView.as_view(name="xiaowang"))
]
"""


# 第一步index/views.py 创建Form对象。
class LoginForm(forms.Form):  # 继承自Form类，
    user_name = forms.CharField(label="用户名", min_length=6, max_length=12)  # 新建表单字段
    user_password = forms.CharField(label="用户密码", min_length=8)


# 第二步围绕form对象完成表单。
def login(request):  # 定义登录处理函数login()
    # print(111,request,type(request),"dir_request",dir(request))
    # print("222 r.post",type(request.POST),dir(request.POST))
    if request.method == "POST":  # request是 HttpRequest的对象，利用它的的method属性，判断请求方法。
        form = LoginForm(request.POST)  # 实例化对象，post提交数据是QuerySet类型的字典，GET方法与其一样。
        # print("dir (form)",dir(form))
        # print("form",form)  # html表单
        if form.is_valid():  # 提供验证判断是否有效，成立则返回是Ture
            print(HttpResponse)
            return HttpResponse("登录成功")
    else:
        form = LoginForm()
    # print("local()",locals())  # {'request': <WSGIRequest: GET '/login/'>, 'form': <LoginForm bound=False, valid=Unknown, fields=(user_name;user_password)>}

    return render(request, "index/login.html", locals())


# 设置添加cookie
def set_cookie_view(request):
    resp = HttpResponse()
    resp.set_cookie('username', 'jack', 3600)
    return resp


# 得到cookie的值使用get方法
def get_cookie_view(request):
    value = request.COOKIES.get('username')
    return HttpResponse('--MY COOKIE is--%s' % value)


# 用来显示查询页面
def search_ttile_form(request):
    return render(request, 'index/search_title.html')


# 用来显示查询结果
def search_title(request):
    # 查询title忽略大小写,所得类型为QuerySet
    if not request.GET.get('title', ''):
        errors = ['输入的书名是无效']  # 在这里使用列表的原因，是因为随着表单功能的修改可能需要传递多个字段，这时可能会有多个不同的错误信息需要展示。
        return render(request, 'index/search_title.html', locals())

    title = Book.objects.filter(title__icontains=request.GET['title'])
    title = list(title.all().values())
    return render(request, 'index/book_list.html', locals())


def book_table(request):
    try:
        all_book = Book.objects.all().order_by('-price')
        if not all_book:
            return HttpResponse('书籍信息表为空，请录入！')
    except Exception as e:
        print(e)
    return render(request, 'index/book_table.html', locals())


def add_book(request):
    if request.method == 'GET':
        return render(request, 'index/add_book.html')
    elif request.method == 'POST':
        # 添加书籍
        title = request.POST.get('title')
        if not title:
            return HttpResponse('请给出一个正确的title')
        pub = request.POST.get('pub')
        price = float(request.POST.get('price', '999.99'))
        if not price:
            return HttpResponse('请输入价格')
        try:
            retail_price = float(request.POST.get('retail_price'))
            if not retail_price:
                return HttpResponse('请输入市场价')
        except Exception as e:
            print(e)
        # 判断title是不是已经存在了
        old_book = Book.objects.filter(title=title)
        if old_book:
            return HttpResponse('你输入的书籍系统已经存在 !')
        try:
            pub1 = PubName.objects.get_or_create(pubname=str(pub))  # 不存在就创建
            # print(pub1[0])
            Book.objects.create(title=title, price=price, retail_price=retail_price, pub=pub1[0])
        except Exception as e:
            print('Add ErrorReason is %s' % e)
        return HttpResponseRedirect('/index/book_table/')
    return HttpResponse('请使用正确Http请求方法 !')


def search_ttile_form2(request):
    return render(request, 'index/search_title2.html', context={'form': TitleSearch()})  # 实例化表单对象


def search_title2(request):
    form = TitleSearch(request.GET)
    if form.is_valid():  # 第一步验证成功
        print('title',form.cleaned_data["title"])
        books = Book.objects.filter(title__icontains=form.cleaned_data["title"])  # 调用cleaned_data属性获取清理后的数据
        if not books:
            return HttpResponseRedirect("/index/book_not_list/")
        return render(request, 'index/book_list2.html', locals())
        # 查看返回结果
    else:
        # 将带有错误信息的表单实例作为上下文传递到需要渲染的模板中
        return render(request, 'index/search_title2.html', {'form': form})


def book_not_list(request):
    return render(request, "index/book_not_list.html")
