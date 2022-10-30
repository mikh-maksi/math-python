import random

while True:
    a = random.randint(1, 10)
    strn = ''
    for i in range (a):
        strn +='.'
    si = input("Please, enter number of points. For stop enter .\n"+strn+"\n")
    if si == '.':
        break
    if a==int(si):
        print("true")
    else:
        print("false")
