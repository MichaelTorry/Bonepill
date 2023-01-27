import ansur_functions as funcs

cords = funcs.cords_gen("bideltoidbreadth", "hipbreadth", "ansur2_male.csv")


whrlist = []
for item in cords:
    whrlist.append(int(item[0])/int(item[1]))

sd, avg = funcs.avg_and_sd_calc(whrlist)
print(f"Average: {round(avg, 3)}, SD: {round(sd, 3)}. This means that 68% of people fall within a range of {round((avg - sd), 3)} - {round((avg + sd), 3)}")
