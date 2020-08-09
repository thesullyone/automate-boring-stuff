def spam(divisor):
    try:
        return 42 / divisor
    except ZeroDivisionError:
        print('Error: can not divide by 0')
print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))