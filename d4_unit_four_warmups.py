age = int(input("How old are you?"))

if age <= 2:
    print("Your ticket is free!")
elif age >= 3 and age <= 12:
    print("Your ticket cost is $8")
else:
    print("Your ticket cost is $10")
