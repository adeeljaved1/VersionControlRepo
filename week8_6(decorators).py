# this is week 8's example, demonstrating decorators
def my_decoractor(func):
    print("this is test decorator feature")
    def wrapper():
        print("something is happening before hello")
        func()
        print("something is happening after hello")
    return wrapper

@my_decoractor
def greetings():
    print("hello!")

greetings()