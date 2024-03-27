def say_hi():
    print('Hi!')

say_hi()

#define functions before we call a function

def say_hello(greeting):
    print('Hi {}!'.format(greeting))

say_hello('Jason')
say_hello('Emily')


def say_hello2(greeting = 'there'):
    """Say Hello"""
    print('Hi {}!'.format(greeting))

help(say_hello)

say_hello2()
say_hello2('Emily')

def say_hello2(name1, name2):
    print('Hi {} and {}!'.format(name1, name2))


def odd_or_even(number):
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

print(odd_or_even(4))
