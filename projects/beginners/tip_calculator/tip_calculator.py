# This is a tip calculator program in python. 

# Global variables
tip = 0
total_price = 0
meal_cost = 0
people = 0

# Function to calculate tip
def tip_calculator():
    global tip, meal_cost, total_price
    try: 
        meal_cost = float(input("What was the cost of the meal: "))
        tip = float(input("What percent tip did you want to give? "))
        tip = (tip/100)
        tip = (tip * meal_cost)
        total_price = (tip + meal_cost)
    except ValueError: 
        print("Not a Valid Input.")
        exit()
    return tip, total_price

# Function to split tip
def split_amount(meal_cost):
    check_people = input("Do you have other people with you(who are not family)? Yes or No: ")
    check_people = check_people.lower().title()
    if check_people == "Yes": 
        people = int(input("How many are there? "))
        meal_cost = ("{:.2f}".format(meal_cost/people))
        print("Amount Per Person: ", meal_cost)
    elif check_people == "No":
        exit()
    else:
        print("Invalid Input")

        
# Code Execution Begins
if __name__=="__main__":

    tip, total_price = tip_calculator()
    print("The cost for each person is", meal_cost)
    print("Tip:", tip)
    print("Total Cost:", total_price)

    split_amount(total_price)
    
