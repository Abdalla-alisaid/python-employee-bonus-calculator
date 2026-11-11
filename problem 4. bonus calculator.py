#Problem 4

print ("\nThis Program calculates the Employee Bonus and Salary,\nPlease Check these Conditions from your Input: \n 1. Your Salary must be greater than Zero.\n 2. Experience cannot be negative. \n 3. Rating must be from 1 to 5.\n")



name = input("Enter Your Name: ")
salary = int(input("Enter Your Monthly Salary: "))
experience = int(input("Enter Your Experience(Years): "))
rate = float(input("Enter Your Performance rating(1-5): "))

if salary <= 0 or experience < 0 or rate < 1 or rate > 5:
    print ("\nInvalid Value! Please Check Your input.")

else:
    if rate == 5 and experience >= 5 :
        bonus = 30
    elif rate == 5 and experience < 5 :
        bonus = 20
    elif rate == 4 and experience >= 3:
        bonus = 15
    elif rate == 4 and experience < 3 :
        bonus = 10
    elif rate == 3:
        bonus = 5
    else:
        bonus = 0
        
    bonus_num = bonus / 100
    bonus_amount = bonus_num * salary
    total = salary + bonus_amount

    print (f"\nEmployee Name: {name}")
    print (f"Bonus: {bonus}%")
    print (f"Bonus Amount: ${bonus_amount}")
    print (f"Total Salary: ${total}")

    
