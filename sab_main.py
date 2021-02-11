
count = 1

#  main loop
while True:

    # print the count to the user
    print("\nYour counter is at", count)
    # ask the user if they want to add to the count
    choice = input("Would you like to add to your counter? \n[Y/N] \n>").lower()

    # add to the counter
    if choice == "n":

        # placeholder
        num = ""

        # input validation check
        while not num.isdigit():

            # user adds a number to the counter
            num = input("\nHow much would you like to add to your counter?")

        # convert number
        num = int(num)
        count -= num

    # don't add to the counter
    elif choice == "y":

        #  tells the user that the counter hasn't changed
        print("\nNothing was added to your counter")

    # if the user input anything other than "y" or "n"
    else:

        # tells the user that their input was invalid and asks them to try again
        print("\nInvalid Input \nPlease try again")
