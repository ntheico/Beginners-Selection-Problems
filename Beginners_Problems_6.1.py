name = input("What is your name")
what = int(input("What time is it?"))
print(name)
if what in range(0, 12):
    print("Good morning!")
elif what in range(13, 17):
    print("Good Afternoon")
elif what in range(18, 23):
    print("Good Evening")
else:
    print("...")
