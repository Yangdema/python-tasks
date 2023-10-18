month = input("enter month:")

if month in ["january" or "february" or "march" or "april" or "may"]:
    print("spring")
elif month in ["june" or "july" or "august"]:
    print("summer")
elif month in ["september" or "october" or "november"]:
    print("fall")
elif month in ["december"]:
    print("winter")
else:
    print("invalid input")

