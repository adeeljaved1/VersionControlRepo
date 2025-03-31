def my_decoractor(func):
    def wrapper():
        print("something is happening before hello")
        func()
        print("something is happening after hello")
    return wrapper

@my_decoractor
def greetings():
    print("hello!")

greetings()