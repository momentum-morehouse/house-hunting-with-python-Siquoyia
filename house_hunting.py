annual_salary = input("Enter your annual salary: ")
portion_saved = input("Enter your percent of your salry to save,as a decimal: ")
monthly_salary_saved = (int(annual_salary)/12) * float(portion_saved)
total_cost = input("Enter the cost of your dream home: ")
portion_down_payment = .25 * int(total_cost)

current_savings = 0

i = 1
while current_savings < portion_down_payment:
   current_savings += monthly_salary_saved
   investment_return = current_savings * (.04/12)
   current_savings += investment_return
   i += 1
print("It will take you",i, "months to save up for the downpayment!" )   

