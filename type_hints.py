from datetime import  date

def alpha(a,b):
    c = a+b
    print(c)

def beta(a: str,b: int ,c):
    # print(a.upper())
    print(a,b,c)

def gamma(a: date, b):
    print(a.year)
    print(b.year)

    alpha(5,3)
    alpha("rain","bow")
    beta(3,'a',44)
    t1 =date(2020,1,20)
    t2 = date(2019, 1, 9)
    gamma(t1,t2)

