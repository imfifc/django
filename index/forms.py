from django import forms
from django.core.exceptions import ValidationError
from django.forms import ComboField, CharField, EmailField, widgets

from index.models import Book, UserInfo


# 可以查看form源码 metaclass=DeclarativeFieldsMetaclass，BaseForm 中定义了生成 HTML 与字段值校验的方法，而 DeclarativeFieldsMetaclass 则定义了创建 Form 对象的过程
class TitleSearch(forms.Form):
    error_css_class = "error"  # 实现错误信息添加CSS样式
    required_css_class = "required"
    title = forms.CharField(label='书名', widget=forms.Textarea, initial="redis",
                            label_suffix='', error_messages={"required": "请输入正确的title"})  # 文本域
    # user = forms.CharField(label="用户名")
    # title = forms.CharField(label='书名', required=True默认,empty_value=''/None/False ，disabled=False)
    # title.clean('')  # “清理”和校验 对数据进行验证和测试。
    # email = forms.EmailField(label="邮箱", widget=forms.EmailField)
    # email.clean('123@qq.com')


""""
t1 = TitleSearch({"title": "python", 'user': "11@qq.com"}, initial={'title': 'Django', 'user': "22@qq.com"})
if t1.has_changed():
    print('-'.join(t1.changed_data))
# 调用是有先后顺序的，即必须使用 is_valid 方法验证通过，才可以把数据存储到 cleaned_data 属性中
t1.fields.values()
t1.is_valid()
t1.fields['title']
# t1.cleaned_data # is_valid() 方法对输入数据的合法性进行验证，然后再使用该属性得到干净的数据，若验证时存在不合法的数据，cleaned_data 方法将会自动清洗掉不它们，只显示合法的数据。
print(t1)  # 显示html as_table  体来说它的主要作用就是解析表单对象中定义的各个 Field，给每个 Field 生成表单 HTML，最后对每个字段的 HTML 拼接得到完整的表单。
t1.as_p()
t1.as_ul()
# 通过label_tag(attrs={})设置属性名
t1['title'].label_tag(attrs={'class': 'bar'})
"""

"""shell
# 如果你有一个绑定的 Form 实例，但是你想更改数据或者你想给一个未绑定的 Form 表单绑定一些数据，此时你需要创建一个新 Form 实例。因为 Form 实例一旦创建，它的数据将不可变。
# 传递空字典会创建具有空数据的绑定形式。
t = TitleSearch()
t.is_bound
t1 = TitleSearch({"title": "python"},initial={'title':'Django'})
t1.is_bound  
t1.is_valid()
t1.has_changed()

t1 = TitleSearch({"title": ""})
t1.is_valid() # False ,required is True

t1.errors.as_json(escape_html=False)
'{"title": [{"message": "\\u8bf7\\u8f93\\u5165\\u6b63\\u786e\\u7684title", "code": "required"}]}'
t1.errors.as_text()
'* title\n  * 请输入正确的title'
t1.errors.as_ul()
'<ul class="errorlist"><li>title<ul class="errorlist"><li>请输入正确的title</li></ul></li></ul>'
t1.errors.as_data()
{'title': [ValidationError(['请输入正确的title'])]}
t1.has_error('title',code="required")
True
t1.has_error('title',code=None) # code =None ,有任何错误都返回True; code="invalid"
True
"""


class ContactForm(forms.Form):
    def clean(self):
        cleaned_data = super().clean()  # 继承clean()方法
        username = cleaned_data.get("username")  # 获取值
        password = cleaned_data.get("password")
        if username and password:  # 两者必须同时满足才可以
            if "Jack" not in username:  # 验证用户名字
                raise forms.ValidationError(
                    "User is  error or password is error "
                )


"""shell
# CharField
title = forms.CharField(empty_value='C语言中文网') # 对空值进行设置
title.clean('')
'C语言中文网'

x = forms.IntegerField(max_value=5, min_value=1)
x.clean(4)

# BooleanField
# 该字段控件默认使用 CheckboxInput。默认为必填字段，若不填则会抛出异常，可以通过它的 required=False 属性来变为可选，即使不提供也不会抛出异常。

Gender=(('M','male'),('F','female'))
sex=forms.ChoiceField(choices=Gender)
# sex sex 字段对应的选择框中有两个可选值即 male 和 fmale。如果表单被提交，那么只有二元组的第一个元素，也就是 M 和 F 会被提交到后台服务器进行处理。
# EmailField UUIDField、GenericIPAddressField、URLField、SlugField 等，它们分别用来验证 UUID（通用唯一识别码）、IP 地址、URL 以及字符串 


# DateTimeField
它是用于表示时间的表单字段，默认的 Widget 控件是 DateTimeInput，它接受一个可选参数 input_formats，这个参数是一个列表，列表中的元素可以转换为 Python 方法 datetime.datetime 的时间格式，默认可以接收的时间格式如下所示：
['%Y-%m-%d %H:%M:%S',   # '2019-1-5 11:15:57'
'%Y-%m-%d %H:%M',       # '2019-3-25 13:30'
'%Y-%m-%d',             # '2019-12-5'
'%m/%d/%Y %H:%M:%S',    # '10/25/2006 14:30:59'
'%m/%d/%Y %H:%M',       # '10/25/2006 14:30'
'%m/%d/%Y',             # '10/25/2006'
'%m/%d/%y %H:%M:%S',    # '1/15/09 14:30:59'
'%m/%d/%y %H:%M',       # '1/15/09 14:30'
'%m/%d/%y']             # '1/15/09'
DateTimeField 的 clean 方法接受的值类型可以是 datetime.datetime、datetime.date 或符合特定格式的字符串，最终会返回 datetime.datetime 对象或抛出异常

x = forms.DateTimeField(input_formats=['2019-1-5 11:12:12'])
x.clean('2019-1-5 11:12:12')
datetime.datetime(2019, 1, 5, 11, 12, 12, tzinfo=zoneinfo.ZoneInfo(key='Asia/Shanghai'))


f = ComboField(fields=[CharField(max_length=10), EmailField()])  
# 验证字段 它默认的 Widget 控件类型为 TextInput，它接收一个必选参数：fields，是一个用于验证字段值的字段列表，并按提供的参数顺序进行验证。
f.clean('123@qq.com')

 # MultipleChoiceField、SplitDateTimeField
"""


class TestForm(forms.Form):
    a = forms.CharField(required=False)  # a不是必填字段，可以不提供
    b = forms.CharField(max_length=20)  # 最大长度为20
    c = forms.IntegerField(max_value=10, min_value=1)  # 最大值为10最小值1


"""
pl = TestForm({"b": "django", "c": 40})
pl.is_valid()
True
pl.errors
pl["c"].errors
print(pl) # 生成html

print(pl['b'])
<input type="text" name="b" value="django" maxlength="20" required id="id_b">
"""


# 实现自定义字段
# 功能是输入书籍的 id 后，可以获取 Book 的实例对象
class BookField(forms.Field):
    default_error_message = {
        'invalid': 'Enter a whole number',
        'not_exist': 'Book Not Exist',
    }

    def to_python(self, num):
        try:
            num = int(str(num).strip())
            return Book.objects.get(id=num)
        except (ValueError, TypeError):
            raise ValidationError(self.error_messages['invalid'], code='invalid')
        except Exception:
            raise ValidationError(self.error_messages['not_exist'], code='not_exist')


# 继承基类 Field 去自定义表单字段可能考虑比较多的问题，所以通常自定义 Field 都会继承自 CharField 或者 IntergerField 等内置字段
class AddstrField(forms.CharField):
    def clean(self, value):
        return 'C语言中文网 %s' % super().clean(value)


"""
x= AddstrField()
x.clean('hahah')
'C语言中文网 hahah'
"""


# 自定义一个验证偶数的 验证器 ，否则抛出异常
def even_validator(value):
    if value % 2 != 0:
        raise ValidationError('%d is not a even number' % value)


# 编写 EvenField字段，只可以接受偶数，否则抛出异常ValidationError
class EvenField(forms.IntegerField):
    # 使用构造函数__init__ 对其进行初始化，并添加验证器规则
    def __init__(self, **kwargs):
        super().__init__(validators=[even_validator], **kwargs)


"""
x=EvenField()
x.clean(2)
2
"""


# 实现自定义校验规则
# 如果只需要对一些表单字段做额外的检验，可以将检验逻辑编写在定义的 Form 类中，以类方法形式存在。
# 表单系统会自动查找以 clean_ 开头，以字段名结尾的方法，它会在验证字段合法性的过程中被调用

class RegForm(forms.Form):
    name = forms.CharField(label='用户名')

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 6:
            raise forms.ValidationError("你注册的用户名字符太短了")
        return name


"""
x = RegForm({'name':"yuanyaun"})
x.is_valid()
True
x.cleaned_data
{'name': 'yuanyaun'}

x = RegForm({'name':"yuan"})
x.is_valid()
False
x.cleaned_data
{}
x.errors
{'name': ['你注册的用户名字符太短了']}
x['name'].errors
['你注册的用户名字符太短了']
"""


class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        labels = {'title': '标题',
                  'price': '零售价格'}  # 表单的名称首先默认使用 Model字段设置的 verbose_name，但是若 Model 字段没有设置该字段选项，则就可以使用 lables 设置的字段名
        exclude = ('retail_price',)
        help_texts = {"title": "书籍的名称", "price": "书籍价格"}
        field_calss = {"title": forms.URLField}  # 对于 title 字段，ModelForm 会将它映射为 fields.CharField 类型。可以根据需要改变这种默认行为
        error_messages = ""  # 用来指定表单字段校验规则，即验证失败时的报错信息。
        # 使用 is_valid 方法来校验字段值的合法性和通过 cleaned_data 属性获取清理后的字段值，另外， ModelForm 也会校验模型字段中设置的限制条件，
        # 比如在 Model 模型的字段中添加了 unique 选项，那么 is_valid 则会查询数据库确认是否存在重复数据。


# save 场景
"""
#  1) 通过页面 Post 提交过来的数据，通过 form 接收 ，然后直接保存到数据库，同时能够产生对应的 models 的一个新对象
f = BookModelForm(request.POST)
new_book = f.save()

# 2) 从数据库中取出 models 的对象，然后通过 form 参数 instance 方法能够实例化该 form，这个主要用来查看具体的信息
a = Book.objects.get(id=1)
f = BookModelForm(instance=a)
f.save()

# 3) 如果既有 Post 又有 instance，则以 Post 提交数据为主，这个主要用来修改具体的信息。如下所示：
a = Book.objects.get(id=1)
f = BookModelForm(request.POST, instance=a)
f.save()
"""


class UserModelForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = "__all__"
        widgets = {'password': widgets.PasswordInput()}  # 控件
