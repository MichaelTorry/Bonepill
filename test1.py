#avg *= 2.54
#sd *= 2.54
#list1 = funcs.list_gen("Heightin", "ansur2_female.csv")

import ansur_functions as funcs

'''list1 = funcs.ratio_gen(funcs.cords_gen("bideltoidbreadth", "hipbreadth", "ansur2_male.csv"))

sd, avg = funcs.avg_and_sd_calc(list1)

print(f"\nAverage: {round(avg, 2)}, SD: {round(sd, 2)}. This means that 68% of people fall within a range of {round((avg - sd), 2)} - {round((avg + sd), 2)}")

sd, avg = funcs.avg_and_sd_calc(funcs.ratio_gen(funcs.cords_gen("BIDELTOID_BRTH", "HIP_BRTH", "ansur1_male.csv")))

print(f"\nAverage: {round(avg, 2)}, SD: {round(sd, 2)}. This means that 68% of people fall within a range of {round((avg - sd), 2)} - {round((avg + sd), 2)}")
'''

measurement1 = input("Enter the first measurement that you want to use: ")
measurement2 = input("Enter the second measurement that you want to use: ")
gender = input("Enter your gender (m/f): ")
value1 = float(input("Enter the value for the first measurement: "))
value2 = float(input("Enter the value for the second measurement: "))

if gender == "m":
    dataset = "ansur2_male.csv"
else:
    dataset = "ansur2_female.csv"


ratio = value1/value2

sd, avg = funcs.avg_and_sd_calc(funcs.ratio_gen(funcs.cords_gen(measurement1, measurement2, dataset)))

sd_dif = (ratio - avg)/sd


print(f"\nAverage: {round(avg, 2)}, SD: {round(sd, 2)}. This means that 68% of people fall within a range of {round((avg - sd), 2)} - {round((avg + sd), 2)}")
print(f"You are {round(sd_dif, 2)} standard deviations from the average of this ratio at {round(ratio, 2)}. ")
