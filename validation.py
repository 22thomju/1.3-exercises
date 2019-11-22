
#!/usr/bin/env python3

def get_float():
    choice = "y"
    while choice.lower() == "y":
        # get input from the user
        monthly_investment = float(input("Enter monthly investment:\t"))
        while monthly_investment <= 0 or monthly_investment >= 1000:
            print("Entry must be greater then 0 and less than or equal to 1000.")
            monthly_investment = float(input("Enter monthly investment:\t"))
        yearly_interest_rate = float(input("Enter yearly interest rate:\t"))
        while yearly_interest_rate <= 0 or yearly_interest_rate > 15:
            print("Entry must be greater then 0 and less than or equal to 15.")
            yearly_interest_rate = float(input("Enter yearly interest rate:\t"))
        choice = 'n'
    return monthly_investment, yearly_interest_rate 

def get_int():
    years = int(input("Enter number of years:\t\t"))
    while years <= 0 or years >= 50:
        print("Entry must be greater then 0 and less than or equal to 50.")
        years = int(input("Enter number of years:\t"))

    return years


def main():
    choice = "y"
    while choice.lower() == 'y':
        
    

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")
    
if __name__ == "__main__":
    main()
