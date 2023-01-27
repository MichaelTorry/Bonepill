import ansur_functions as funcs

cords = funcs.cordsgen("waistcircumference", "buttockcircumference")


whrlist = []
total = 0
for item in cords[0]:
    whrlist.append(int(item[0])/int(item[1]))
    total+=1

whrtotal = 0
for item in whrlist:
    whrtotal += item



whrlist.sort()
print("\n\n")
whraverage = whrtotal/total
whrSD = funcs.SDcalc(whrlist)
print(f"Average: {round(whraverage, 3)}, SD: {round(whrSD, 3)}. This means that 68% of people fall within a range of {round((whraverage - whrSD), 2)} - {round((whraverage + whrSD), 2)}")
