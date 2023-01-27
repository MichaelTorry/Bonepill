import ansur_functions as funcs

cords = funcs.cordsgen("waistcircumference", "buttockcircumference")

print(cords)
whrlist = []
total = 0
for item in cords:
    whrlist.append(int(item[0][0])/int(item[0][1]))
    total+=1
whrtotal = 0
for item in whrlist:
    whrtotal += item

whrlist.sort()
print(whrlist)
print("\n\n")
print(whrtotal/total)

