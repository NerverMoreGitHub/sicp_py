# 1.2
value = (5+4+(2-(3-(6+4/5))))/(3*(6-2)*(2-7))
print(value)

#1.3
def get_big2_sum1(a,b,c):
    if a==b and b==c:
        return a+b
    if a > b:
        if b > c:
            return a+b
        else:
            return a+c
    else:
        if a > c:
            return b+a
        else:
            return b+c
print(get_big2_sum1(15,13,11))

#1.4
def a_plus_abs_b(a,b):
    if b<0:
        b = -b
    return  a + b
print(a_plus_abs_b(10,-10))

#1.5 Ben Bitdiddle
#正则序求值 vs 应用序求值
def square(x):
    return  x**2
def sum_of_square(x,y):
    return  square(x) + square(y)
def f(a):
    return sum_of_square(a+1,a*2)
print(f(10))


