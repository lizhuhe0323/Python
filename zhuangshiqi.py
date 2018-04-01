def color(func):
    def color_font(*args):
        return "\033[1;31m%s\033[0m" % func(*args)
    return color_font

@color
def say_hi():
    return "Hello world."

@color
def greet(name):
    return "Welcome %s" % name

if __name__ == '__main__':
    print (say_hi())
    print (greet("bob"))