# if, else, elif

number = 16

if number > 0:
    print("Number is positive")
elif number == 0:
    print("Number is zero")
else:
    print("Number is negative")


# nested if-else

age = 23

if age >= 18:
    print("You are eligible to vote")
    if age >= 21:
        print("You are allowed to drive a car")
    else:
        print("You are not 18 years old")
else:
    print("You are not eligible to vote")


# elif

score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# if-else with logical operators

user_logged_in = True
is_admin = False

if user_logged_in and is_admin:
    print("Admin dashboard")
elif user_logged_in and not is_admin:
    print("User dashboard")
else:
    print("Login page")

# Ternary Operator

tempature = 30
weather = "hot" if tempature > 20 else "cold"
print(f'The weather is {weather}')

# check existence 

fruit = "apple"
favorite_fruits = ["apple","banana","mango"]

if fruit in favorite_fruits:
    print(f"You like {fruit}")
else:
    print(f"You don't like {fruit}")

# Match case (just like switch case)

status_code = 200

match status_code:
    case 200:
        print("Success")
    case 400:
        print("Bad request")
    case 404:
        print("Not found")
    case _:
        print("Something went wrong")