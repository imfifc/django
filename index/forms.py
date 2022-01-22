from django import forms


class TitleSearch(forms.Form):
    title = forms.CharField(label='书名', widget=forms.Textarea, initial="C语言中文网",
                            error_messages={"required": "请输入正确的title"})  # 文本域
    # title = forms.CharField(label='书名', required=True默认,empty_value=''/None/False ，disabled=False)
    title.clean('')  # “清理”和校验 对数据进行验证和测试。
    email = forms.EmailField(label="邮箱", widget=forms.EmailField)
    email.clean('123@qq.com')
