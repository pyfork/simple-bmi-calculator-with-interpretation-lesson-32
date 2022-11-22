# Get data from user
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

# Calculate BMI, round it up to next integer
bmi = round(weight / height ** 2)

# Stringify BMI
# bmi_str = str(bmi)

# Output BMI reading and interpretation
# F-string method
if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.\n")
elif bmi > 18.5:
  if bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.\n")
  elif bmi > 25:
    if bmi < 30:
      print(f"Your BMI is {bmi}, you are slightly overweight.\n")
    elif bmi > 30:
      if bmi < 35:
        print(f"Your BMI is {bmi}, you are obese.\n")
      elif bmi >= 35:
        print(f"Your BMI is {bmi}, you are clinically obese.\n")
        