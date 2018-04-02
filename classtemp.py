class Myclass:
    number = 123456

    def __init__(self):
        self.data = []

    def f(self):
        return 'hello,world'

x = Myclass()

print("Myclass类的属性number为：",x.number )
print("Myclass类的方法f的输出为:",x.f())

