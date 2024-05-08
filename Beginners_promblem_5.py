count = 0 
stringsList = ["abc", "123", "2332", "aBBA", "heelloo", "1212", "DcEfD"]

for x in stringsList:
    if x[0].lower() == x[-1].lower():
        count += 1

print(count)
