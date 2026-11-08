attemps = 3
x = input(f"zadejte pin (počet pokusů:{attemps}): ")
pin = "6245"

for i in range(1, attemps):
    print(i)  
    if (str(x)) == pin:
        print ("heslo přijato")
        break
    elif x != pin:
        print ("špatné heslo")
        x = input("zadejte pin: ")
    if i == 2:
        print(f"došel počet pokusů (max {attemps})")
        break


