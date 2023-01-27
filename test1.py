import ansur_functions as funcs

cords = funcs.cords_gen("shouldercircumference", "waistcircumference", "ansur2_male.csv")

list1 = funcs.ratio_gen(cords)

list1 = funcs.list_gen("Heightin", "ansur2_female.csv")

sd, avg = funcs.avg_and_sd_calc(list1)
avg *= 2.54
sd *= 2.54
print(f"\nAverage: {round(avg, 2)}, SD: {round(sd, 2)}. This means that 68% of people fall within a range of {round((avg - sd), 2)} - {round((avg + sd), 2)}")
