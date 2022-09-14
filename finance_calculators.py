import math

# the user is allowed to choose which calculation they want to do.
user_calculation=input("\n choose either 'investment' or 'bond' from the menu below to proceed:?").lower( )

# defination of bond and investment
            
print("\n investment-to calculate the amount of interest you'll earn on interest:")
print("\n bond-to calculate the amount you'll pay on a home loan:")

# from printed user calculation if selected investment

if user_calculation == "investment" :

    # ask the user for their /deposit
    user_deposit = float(input("\n please enter the amount of your deposit"))
    # ask the user for their interest rate
    user_interest_rate=float(input(" please enter your interest rate(as a percentange):?"))
 
    # ask the user for number of years
    user_years = float(input("please enter years you plan on investing for?:"))

    # ask the user for their interest either simple or compound
    user_interest = input("\n please enter interest  you want either 'simple' or 'compound'.")

    # if the user choose simple interest
    if user_interest == "simple":

        simple_interest = user_deposit * (1 + (user_interest_rate/100) * user_years)
        print("your simple interest is", round(simple_interest))

    # if the user choose compound interest
    elif user_interest == "compound":
        # formular for compound interest
        # A=P(1 + r )^t

        compound_interest = user_deposit * math.pow((1+(user_interest_rate/100)), user_years)
        print("your compound interest is", round(compound_interest))



#if the user choose bond
elif user_calculation== "bond":
        
#bond repayment formular
#x=(i.P)/(1-i)^(-n)
#p-is for the present value of the house
#i-is for the monthly interest rate,calculated by dividing the anual rate by 12
#n-is the number of months over which the bond will be repaid
        
        #ask the user the present value of a house

        user_present_value_house=float(input("please enter the present value of the house"))

        #ask for interest rate
        user_interest_rate=float(input("please enter your interest rate(percentage)"))

        #ask for number of months they plan to take to repay the bond
        user_months_to_pay=float(input("please enter number of months to repay:?"))

        #formula to calculate the bond
        bond_amount = ((user_interest_rate/100/12)*user_present_value_house)/(1-(1+user_interest_rate/100/12)**(-user_months_to_pay))
        print("your bond repayement is","R",round(bond_amount))
 