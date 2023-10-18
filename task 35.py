day = input("enter day:")

if day == "monday" or "tuesday" or "wednesday" or "thursday":
    print("weekdays")
if day == "friday":
    print("TGIF")
if day == "saturday" and "sunday":
    print("weekend")
else:
    print("invalid input")