temperature = input("enter temperature:")
temperature = int(temperature)
if temperature >= 100:
    print("boiling")
if temperature >= 32 and temperature <= 99:
    print("liquid")
if temperature <= 32:
    print("freezing")