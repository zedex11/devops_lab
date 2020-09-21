# create a function that will calculate and print the factorial
def factorial():
    while True:
        try:
            n = int(input("Enter the number to calculate the factorial: "))
        except ValueError:
            print("Error! Wrong input, please try again...")
        else:
            fac = 1
            for i in range(2, n + 1):
                fac = fac * i
            print(fac)
            break


factorial()
