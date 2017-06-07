speed = int(input("What is your speed?"))


if speed < 0:
    print("that doesnt make sense!")
elif speed <= 55:
    print("no fine")
elif speed < 60:
    print("warning")
elif speed < 70:
    print("$50 fine")
else:
    print("$200 fine")
