def is_leap_year(year):
    # Leap years are divisible by 4
    divisible_by_4 = (year % 4 == 0)
    
    # Leap years that are divisible by 100 are not leap years, except those divisible by 400
    divisible_by_100 = (year % 100 == 0)
    
    # Leap years that are divisible by 400 are leap years
    divisible_by_400 = (year % 400 == 0)
    
    # A year is a leap year if it's divisible by 4 and not divisible by 100, or divisible by 400
    return divisible_by_4 and (not divisible_by_100 or divisible_by_400)

# Get user input
year = int(input("Enter a year: "))

# Check if it's a leap year and print the result
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")