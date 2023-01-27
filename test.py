import ansur_functions as funcs

print("\n\n\nPassoide detector, enter your measurements and you will be given a passing score.")
print("The ratios measured are: hips-waist, hips-shoulder, shoulder-waist, and a raw value of height")
print("Closer to zero means closer to the average (passing)")
print("However lower scores are generally more feminine, and higher ones are more masculine")
print("You should also note that score are reletive to cis people of that gender\n\n")

print("All measurements are in cm unless otherwise indicated\n\n")
#gender = input("Enter your gender: (m/f) ")
#bideltoid = int(input("Enter your Bideltoid Shoulder Breadth: "))*10
#hipB = int(input("Enter you Hip Breadth: "))*10
#shoulderC = int(input("Enter your Shoulder Circumference: "))*10
#waistC = int(input("Enter you Waist Circumference: "))*10
#hipsC = int(input("Enter your Hips Circumference: "))*10
#height = int(input("Enter you Height: "))/2.54

#print(gender, bideltoid, hipB, shoulderC, waistC, hipsC, height)

dataset = "ansur2_female.csv"

bideltoid_hipsB_SD, bideltoid_hipsB_A = funcs.avg_and_sd_calc(funcs.ratio_gen(funcs.cords_gen("bideltoidbreadth", "hipbreadth", dataset)))
whr_SD, whr_A = funcs.avg_and_sd_calc(funcs.ratio_gen(funcs.cords_gen("waistcircumference", "buttockcircumference", dataset)))
waist_shoulder_SD, waist_shoulder_A = funcs.avg_and_sd_calc(funcs.ratio_gen(funcs.cords_gen("shouldercircumference", "waistcircumference", dataset)))
height_SD, height_A = funcs.avg_and_sd_calc(funcs.list_gen("Heightin", dataset))

print(height_SD, height_A)
