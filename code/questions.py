import random


while True:
    a = random.randint(1, 10)
    b = random.randint(1, 10)

    si = input("Please, enter current sign (< or = or >). For stop enter .\n"+str(a)+" "+str(b)+"\n")
    # print(a,b)
    if si == '.':
        break
    if a>b and si == '>':
        print("true")
    elif a<b and si == '<':
        print("true")
    elif a==b and si == '=':
        print("true")
    else:
        print("false")
