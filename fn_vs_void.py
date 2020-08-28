def celsius_to_fah(celsius):

    return (celsius * 9/5)+32

def temp_table():
    for c in range(0,101,5):
        f = celsius_to_fah(c)
        print("{}c= {}F".format(c,f))
#
# f = celsius_to_fah(100)
# print(f)
temp_table()