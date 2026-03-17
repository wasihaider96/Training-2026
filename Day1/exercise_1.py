# Variables
name = "Wasi Haider"
age = 24
drinks_coffee = True
salary = 80000 # monthly salary in Rs

#Coffee details
cups_per_day = 3
price_per_cup = 150

#Print formatted sentence
print(f"My name is {name}, I am {age} years old, Coffee drinker: {drinks_coffee}. My salary is Rs. {salary}.")

#Years until retirement
retirement_age = 60
years_left = retirement_age - age
print(f"I have {years_left} years left until retirement.")

#weekly coffee budget
days_per_week = 7
weekly_coffee_budget = 0

if drinks_coffee:
    weekly_coffee_budget = cups_per_day * price_per_cup * days_per_week

# Output results
print(f"My Weekly coffee budget: Rs. {weekly_coffee_budget}")