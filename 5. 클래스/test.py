class human():
    def __init__(self, age):
        self.age = age

    def say_hello(self):
        print('hello')

    def say_age(self):
        print(self.age)


이규준 = human(17)
이규준.say_hello()
이규준.say_age()