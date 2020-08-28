print("1"+("0"*100))

# str.format
print("1{0}".format("0" *100))

# f-str
print(f'1{"0"*100}')

def demo2():
    print("1",end='')
    for i in range(100):
        print("0",end='')

def repeat(ch,times):
    for i in range(100):
        print(ch,end='')

def repeat2(ch,times):
    s=''
    for i in range(times)
        s+=ch
        return s

