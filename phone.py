#! home/student/Documents Pyhton3

pwrd = (input("Enter passcode to unlock: "))
while pwrd != '155':
    print("Incorrect passcode")
    pwrd = (input("Enter passcode to unlock: "))
while pwrd == '155':
    print("---------------\nUnlocked, select an app\n---------------")
    print("Calculator \nSchedule \nPikachu \n8ball \nLock")
    print()
    app = (input("open app: "))
    if app.lower() == 'calculator':
        #calculator
        print("**using letters as a number entry will cause a crash")
        calcu = (input("Use a calculator? (y/n) "))
        while calcu.lower() == 'y':
            func = (input("\n'close' to close calculator.\nmultiply, divide, add, or subtract? "))
            if func.lower() == 'multiply':
                mn1= int(input("Number 1: "))
                mn2= int(input("Number 2: "))
                ans = mn1 * mn2
                print(mn1, "*", mn2, "=", ans)
            elif func.lower() == 'divide':
                dn1= int(input("Number 1: "))
                dn2= int(input("Number 2: "))
                ans = dn1 / dn2
                print(dn1, "/", dn2, "=", ans)
            elif func.lower() == 'add':
                an1= int(input("Number 1: "))
                an2= int(input("Number 2: "))
                ans = an1 + an2
                print(an1, "+", an2, "=", ans)
            elif func.lower() == 'subtract':
                sn1= int(input("Number 1: "))
                sn2= int(input("Number 2: "))
                ans = sn1 - sn2
                print(sn1, "-", sn2, "=", ans)
            elif func.lower() == 'close':
                print("closing...")
                break
            elif func.lower() != 'multiply' or 'divide' or 'add' or 'subtract' or 'close':
                print("**That is not an option, try again ")
        else:
            print("Ok.")
    #schedule
    if app.lower() == 'schedule':
        weekab = input("View a schedule? (y/n) ")
        while weekab.lower() == 'y':
            sa = input("\n'close' to exit\nShop or Academic? ")
            if sa.lower() == 'shop':    
                print("\n=Shop Schedule=\nBreak from 8:45-9:00\nLunch at 11:18\nBell rings at 1:56")
            elif sa.lower() == 'academic':
                print("\n=Academic Schedule=\nP1  : gym\nP2/3: ela\nP4/5: biology\n===Lunch===\nP6/7: history\nP8/9: algebra II")
            elif sa.lower() == 'close':
                print("returning to homescreen...")
                break
            else:
                print("\nInvalid option")
                
            
    #pikachu meme
    if app.lower() == 'pikachu':
        print("\nWhen you realize you can make \nmemes in Visual Studio Code\n")
        print("⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⣠⣤⣶⣶ \n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⢰⣿⣿⣿⣿ \n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣀⣀⣾⣿⣿⣿⣿ \n⣿⣿⣿⣿⣿⡏⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿ \n⣿⣿⣿⣿⣿⣿⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠁⠀⣿ \n⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠙⠿⠿⠿⠻⠿⠿⠟⠿⠛⠉⠀⠀⠀⠀⠀⣸⣿ \n⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿ \n⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣴⣿⣿⣿⣿ \n⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⢰⣹⡆⠀⠀⠀⠀⠀⠀⣭⣷⠀⠀⠀⠸⣿⣿⣿⣿ \n⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠈⠉⠀⠀⠤⠄⠀⠀⠀⠉⠁⠀⠀⠀⠀⢿⣿⣿⣿ \n⣿⣿⣿⣿⣿⣿⣿⣿⢾⣿⣷⠀⠀⠀⠀⡠⠤⢄⠀⠀⠀⠠⣿⣿⣷⠀⢸⣿⣿⣿ \n⣿⣿⣿⣿⣿⣿⣿⣿⡀⠉⠀⠀⠀⠀⠀⢄⠀⢀⠀⠀⠀⠀⠉⠉⠁⠀⠀⣿⣿⣿ \n⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿ \n⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿")
            
    #8ball game
    if app.lower() == '8ball':
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


    
    #lock
    if app.lower() == 'lock':
        print("locked")
        pwrd = 5

   

