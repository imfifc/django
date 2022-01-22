from django import forms


class TitleSearch(forms.Form):
    error_css_class = "error"  # 实现错误信息添加CSS样式
    required_css_class = "required"
    title = forms.CharField(label='书名', widget=forms.Textarea, initial="C语言中文网",
                            error_messages={"required": "请输入正确的title"})  # 文本域
    user = forms.CharField(label="用户名")
    # title = forms.CharField(label='书名', required=True默认,empty_value=''/None/False ，disabled=False)
    # title.clean('')  # “清理”和校验 对数据进行验证和测试。
    # email = forms.EmailField(label="邮箱", widget=forms.EmailField)
    # email.clean('123@qq.com')


t1 = TitleSearch({"title": "python",'user':"11@qq.com"}, initial={'title': 'Django','user':"22@qq.com"})
if t1.has_changed():
    print('-'.join(t1.changed_data))

t1.fields.values()
t1.is_valid()
t1.fields['title']
# t1.cleaned_data # is_valid() 方法对输入数据的合法性进行验证，然后再使用该属性得到干净的数据，若验证时存在不合法的数据，cleaned_data 方法将会自动清洗掉不它们，只显示合法的数据。
print(t1) # 显示html as_table
t1.as_p()
t1.as_ul()
#通过label_tag(attrs={})设置属性名
t1['title'].label_tag(attrs={'class': 'bar'})
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
