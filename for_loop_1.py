def loop1():
    for  i in range(11):
        print(i)

def loop2():
    for  i in range(1,11):
        print(i)

def loop3():
    for  i in range(1,11,2):
        print(i)
        print("---------")
    print("bye")

def loop_str():
    s ="over the rainbow"
    for c in s: #for each
        print(c.upper())

def loop_tuple():
    fx= "eu","gu","uj","uc"
    for f in fx:
        print(fx.capitalize())

def loop_tuple2():
    fx= "eu","gu","uj","uc"
    for i in range(len(fx)):
        print(i+1,fx[i].capitalize(),sep=".")
loop_tuple2()