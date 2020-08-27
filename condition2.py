def ticket(age):
    if age <= 5:
        return 0
    else:
        return 100



def ticket2(age):
    if age <= 5 or age >= 60 :
        return 0
    else:
        return 100

def ticket3(age,is_local):
    if (age <= 5 or age >= 60) and is_local:
        return 0
    else:
        return 100

def ticket2(age):
    return 0 if age <= 5 or age >= 60 else 100 # ternary

print(ticket(70))
print(ticket2(35))
print(ticket2(60))
print(ticket3(3,False))