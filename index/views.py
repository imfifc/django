from django.shortcuts import render

# Create your views here.
# 方式一
from django.template import loader  # 导入loader方法
from django.shortcuts import render  # 导入render 方法
from django.http import HttpResponse
from django.template import Template, Context  # 调用template、以及上下文处理器方法


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
