import sys, weakref

"""
观察者模式它定义了对象之间一对多的依赖关系，当一对象的状态发生改变的时候，所有依赖于它的对象都获取到通知并发生相应的改变。观察者模式还有一个别名叫做发布订阅模式，
这个名字就非常的形象的说明了这种设计模式的理念，当订阅者订阅了某系列杂志，当杂志有了新的状态即发布者，比如更新了，
那么此时就会给所有的订阅者发送一条消息，那么所有的订阅者就会收到此消息做出购买或不购买的选择。

比如在微博或者论坛中，你发布了一个话题，那么关注你的粉丝就会收到一个通知，粉丝收到通知后可以相应的做出回馈。这也是观察者模式的适应场景。

种模式的优点非常明显，它在目标与观察者之间建立了轻度的关联关系，对于它们各自的扩展就会非常容易。在运行时，观察者可以动态地添加或删除（取关操作），
对目标（话题发布者）不会有任何影响，反过来也是一样，所以它们是抽象耦合的。
"""

"""
学习过 Python 语言的小伙伴知道，Python 的垃圾回收由引用计数、标记清理和分代回收等方式构成。其中大部分对象的生命周期由对象的引用计数来管理。
在 Python 语言中一切皆对象（还是 Python 好从不缺对象），每一个对象都会维护一个叫做 obrefcnt 的属性，也就是引用计数，当一个对象有了新的引用时，obrefcnt 就会加 1 ；
当对象的引用被删除时就会就会减 1；当其为 0 的时候表示当前对象没有被使用，
"""

# Python语言特性弱引用
# 因为弱引用不会改变对象的引用计数，所以，Django 信号机制采用弱引用的方式对信号回调函数进行引用，以此来避免内存泄露的问题
a = 1
sys.getrefcount(a)  # 接受一个参数对象


class A():
    def hello(self):
        return "hahah"


def func(obj):
    print("%s被删除" % obj)


a = A()
sys.getrefcount(a)
# 2
ref = weakref.ref(a)
sys.getrefcount(a)
# 2
ref().hello()
# 'hahah'

weakref.finalize(a, func, str(hex(id(a))))  # 引用对象被删除时执行的清理函数
sys.getrefcount(a)
# 2
del a
# 0x170d8edee80被删除


# 引用对象a的hello方法
a = A()
ref = weakref.WeakMethod(a.hello)  # 引用对象a的hello方法
ref()
# <bound method A.hello of <__main__.A object at 0x00000170D8EFDC40>>
ref()()
# 'hahah'
