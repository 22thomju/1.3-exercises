import random

yn = input("Use the 8ball? (y/n) ")

while yn != 'y':
    if yn == 'n':
        print("ok.")
        break

    else:
        print("y or n")
        yn = input("Use the 8ball? (y/n) ")
        
while yn == 'y':
    q = input("'exit' to leave\nWhat is your question? ")
    print()

    choice = (random.randint(1,9))
    if q == 'exit':
        print("exiting...")
        break

    if choice == 1:
        print("yes.")
    elif choice == 2:
        print("most likely.")
    elif choice == 3:
        print("it is certain.")
    if choice == 4:
        print("focus and ask again.")
    if choice == 5:
        print("the answer is unclear, try again.")
    if choice == 6:
        print("cannot predict now.")
    if choice == 7:
        print("no.")
    if choice == 8:
        print("it is doubtful.")
    if choice == 9:
        print("don't count on it.")

    print()
    continue


    
    