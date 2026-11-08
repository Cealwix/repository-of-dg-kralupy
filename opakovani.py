print("Hello, world")

pokus = 1

while pokus <= 5 :


        spravnavyska = 158
        vyska = int(input("zadejte výšku"))
        text = "tvůj tip"

        print (f"{text} {vyska} {type(vyska)}")

        print (type(text))



        if vyska == spravnavyska:
            print ("good job")

        elif vyska < spravnavyska:
            print ("víc")

        elif vyska > spravnavyska:
            print ("míň")

        print (f"počet pokusů: {pokus}")
        pokus += 1







