def instructions():
   text = '''
Write function bmi that calculates body mass index (bmi = weight / height2).
if bmi <= 18.5 return "Underweight
if bmi <= 25.0 return "Normal
if bmi <= 30.0 return "Overweight
if bmi > 30 return "Obese"
   '''
   return text
def bmi(weight, height):
    height = height ** 2
    your_bmi = weight / height
    if your_bmi <= 18.5:
        return "Underweight"
    elif your_bmi <= 25.0:
        return "Normal"
    elif your_bmi <= 30.0:
        return "Overweight"
    elif your_bmi > 30.0:
        return "Obese"