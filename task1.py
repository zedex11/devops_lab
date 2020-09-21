# create a function that will convert 2 lists into a dictionary
def create_diction():
    while True:
        # check input on a given condition
        try:
            keys = list(map(int, input("Enter numeric keys separate by space: ").split()))
            values = list(map(int, input("Enter numeric values separate by space: ").split()))
        # error handling
        except ValueError:
            print("Error! Wrong input, please input only numbers separate by space...")

        else:
            # check key list for uniqueness of elements
            if len(keys) == len(set(keys)):
                diction = {}
                # if key list more than value list, value list equalizes by add value "None"
                if len(keys) > len(values):
                    for i in range((len(keys) - len(values))):
                        values.append('None')
                # fill the dictionary
                for n in range(len(keys)):
                    diction[keys[n]] = values[n]
                print(diction)
                break
            else:
                print("keys values must be unique and not repeated")


create_diction()
