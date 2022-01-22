from django import forms
from django.forms import ComboField, CharField, EmailField


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
print(t1)  # 显示html as_table
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