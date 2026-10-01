print("welcome to the pattern jenerator and number analyzer")

while True:
    print("select an optiion")
    print("1.generate a patten")
    print("2.analyze a number")
    print("3.exit")


    choice=int(input("enter your choice"))

    if choice == 1:
        rows = int(input("enter the number of rows for the pattern"))
        print("pattern:")
        for i in range(1,rows+1):
            print("*" * i)
