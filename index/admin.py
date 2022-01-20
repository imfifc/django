from django.contrib import admin

# Register your models here.
from django.contrib import admin  # Django自动在admin.py文件中导入
from index.models import Book, Author, UserInfo, PubName, ExtendUserinfo  # 这个需要我们自己导入相应的模型类（数据表）

# admin.site.register([Book, Author, UserInfo])
admin.site.register([Author, UserInfo, PubName, ExtendUserinfo])
# admin.site.register(Book) #单一模型注册
"""
 python manage.py  createsuperuser

from index.models import MyModel
admin.site.register(MyModel, MyModel_Manager)#使用register注册关联关系

#或者使用装饰器进行注册
@admin.register(MyModel)#在定义的模型管理器类中使用装饰器
class MyModelAdmin(admin.ModelAdmin)

# Django 规定每一个 Model 只可以注册一次，所以再注册同一个 Model 时，需要将之前注册的语句注释（或者删除）
"""


@admin.register(Book)  # 使用admin.register(Model)来注册
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'retail_price', 'pub_name']

    def pub_name(self, obj):  # 显示约束字段pubname
        return u'%s' % obj.pub.pubname  # u会对字符串中的\n等进行转义

    pub_name.admin_order_field = 'pub'  # 字段排序
    pub_name.short_description = '出版社'  # 属性name重命名
    list_display_links = ['title']
    list_filter = ['title', 'pub__pubname']  # 第二个是 ForeignKey字段
    list_editable = ['price', 'retail_price']
    search_fields = ['title', 'pub__pubname']
    raw_id_fields = ['pub']  # 每一个字段必须是 ForeignKey 或 ManyToManyField 类型
