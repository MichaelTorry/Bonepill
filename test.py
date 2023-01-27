import ansur_functions as funcs

print("\n\n\nPassoide detector, enter your measurements and you will be given a passing score.")
print("The ratios measured are: hips-waist, hips-shoulder, shoulder-waist, and a raw value of height")
print("Closer to zero means closer to the average (passing)")
print("However lower scores are generally more feminine, and higher ones are more masculine")
print("You should also note that score are reletive to cis people of that gender\n\n")

print("All measurements are in cm unless otherwise indicated\n\n")
version = input("Which version of ANSUR would you like to use: (1/2) ")
gender = input("Enter your gender: (m/f) ")
bideltoid = int(input("Enter your Bideltoid Shoulder Breadth: "))*10
hipB = int(input("Enter you Hip Breadth: "))*10
shoulderC = int(input("Enter your Shoulder Circumference: "))*10
waistC = int(input("Enter you Waist Circumference: "))*10
hipC = int(input("Enter your Hips Circumference: "))*10
height = int(input("Enter you Height: "))/2.54

print(version, gender, bideltoid, hipB, shoulderC, waistC, hipC, height)

if gender == "f":
    dataset = "ansur2_female.csv"
elif gender == "m":
    dataset = "ansur2_male.csv"
else:
    print("chose m or f (make sure to use lowercase letters and no spaces")

if version == "2":
    bidel = "bideltoidbreadth"
    hipbreadth = "hipbreadth"
    waist = "waistcircumference"
    hipcirc = "buttockcircumference"
    shoulder = "shouldercircumference"
    heightV = "Heightin"

bideltoid_hipsB_SD, bideltoid_hipsB_A = funcs.avg_and_sd_calc(funcs.ratio_gen(funcs.cords_gen(bidel, hipbreadth, dataset)))
whr_SD, whr_A = funcs.avg_and_sd_calc(funcs.ratio_gen(funcs.cords_gen(waist, hipcirc, dataset)))
waist_shoulder_SD, waist_shoulder_A = funcs.avg_and_sd_calc(funcs.ratio_gen(funcs.cords_gen(shoulder, waist, dataset)))
height_SD, height_A = funcs.avg_and_sd_calc(funcs.list_gen(heightV, dataset))

bidel_hipB_sd_dif = ((bideltoid/hipB) - bideltoid_hipsB_A)/bideltoid_hipsB_SD
whr_sd_dif = ((waistC/hipC) -  whr_A)/whr_SD
waist_shoulder_sd_dif = ((shoulderC/waistC) - waist_shoulder_A)/waist_shoulder_SD
height_sd_dif = ((height) - height_A)/height_SD

print("\n\nBideltoid Shoulder to Hip Breadth Ratio")
print(f"Average: {round(bideltoid_hipsB_A, 2)}, SD: {round(bideltoid_hipsB_SD, 2)}. This means that 68% of people fall within a range of {round((bideltoid_hipsB_A - bideltoid_hipsB_SD), 2)} - {round((bideltoid_hipsB_A + bideltoid_hipsB_SD), 2)}")
print(f"Your Bideltoid Shoulder to Hip Breadth Ratio: {round((bideltoid/hipB), 2)}")
print(f"You are {round(bidel_hipB_sd_dif, 2)} standard deviations from the average bideltoid shoulder-hip breadth ratio. ")

print("\n\nHips Waist Ratio")
print(f"Average: {round(whr_A, 2)}, SD: {round(whr_SD, 2)}. This means that 68% of people fall within a range of {round((whr_A - whr_SD), 2)} - {round((whr_A + whr_SD), 2)}")
print(f"Your Hips Waist Ratio: {round((waistC/hipC), 2)}")
print(f"You are {round(whr_sd_dif, 2)} standard deviations from the average hips-waist ratio. ")

print("\n\nShoulder Waist Ratio")
print(f"Average: {round(waist_shoulder_A, 2)}, SD: {round(waist_shoulder_SD, 2)}. This means that 68% of people fall within a range of {round((waist_shoulder_A - waist_shoulder_SD), 2)} - {round((waist_shoulder_A + waist_shoulder_SD), 2)}")
print(f"Your Shoulder Waist Ratio: {round((shoulderC/waistC), 2)}")
print(f"You are {round(waist_shoulder_sd_dif, 2)} standard deviations from the average shoulder-waist ratio. ")

print("\n\nHeight")
print(f"Average: {round((height_A*2.54), 2)}, SD: {round((height_SD*2.54), 2)}. This means that 68% of people fall within a range of {round(((height_A*2.54) - (height_SD*2.54)), 2)} - {round(((height_A*2.54) + (height_SD*2.54)), 2)}")
print(f"Your Height: {round((height*2.54), 2)}")
print(f"You are {round(height_sd_dif, 2)} standard deviations from the average height. ")

print(f"\n\nYou are on average {round(((bidel_hipB_sd_dif+whr_sd_dif+waist_shoulder_sd_dif+height_sd_dif)/4),2)} standard deviations from average")