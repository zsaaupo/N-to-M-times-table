"""
Times table from N to M
"""
print(__doc__)


UserInput1 = int(input("Enter a first int num = "))
UserInput2 = int(input("Enter a second int num = "))

if UserInput1 < UserInput2 or UserInput1 == UserInput2:
    for i in range(UserInput1, UserInput2+1):
        for Multiplier in range(1, 11):
            print(i, "x", Multiplier, " = ", Multiplier*i)
        print()
else:
    print("N > M")