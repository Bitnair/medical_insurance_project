# Examine how factors such as age, sex, BMI, number of children, and smoking status contribute to 
# medical insurance costs.

# Variables for estimating medical insurance cost
# age = 0
# sex = 0                 # 0 for female, 1 for male
# bmi = 0                 # individual’s body mass index
# num_of_children = 0     # number of children the individual has
# smoker = 0              # 0 for a non-smoker, 1 for a smoker

# According to the WHO (World Health Organization), here are the nutritional statuses for various BMI ranges:
# BMI > 30: obese
# BMI >= 25 and bmi <= 30: overweight
# BMI >= 18.5 and bmi < 25: normal weight
# BMI < 18.5: underweight


# Function that calculate the BMI:
# weight in kilograms
# height in meters
def bmi_calculation(weight, height):
    bmi_formula = weight / (height**2)
    print('Your BMI is : ' + str(round(bmi_formula, 1)))
    return (round(bmi_formula, 1))

# Function that analyzes an individual’s smoking status:
def analyze_smoker(smoker_status):
    if smoker_status == 1:
        print('To lower your cost, you should consider quitting smoking.')
    else:
        print('Smoking is not an issue for you.')
        
# Function that analyzes an individual’s BMI (body mass index):
def analyze_bmi(bmi_value):
    bmi_value_to_lower = bmi_value - 22   # BMI value to lower in order to bring it to a normal weight range
    if bmi_value > 30:
        print('Your BMI is in the obese range. To lower your cost, you should significantly lower your BMI.')
        print('In order to reach a healthy weight range, you would have to lower your BMI by ' + str(round(bmi_value_to_lower, 1)) + ' points')
    elif bmi_value >= 25 and bmi_value <= 30:
        print('Your BMI is in the overweight range. To lower your cost, you should lower your BMI.')
        print('In order to reach a healthy weight range, you would have to lower your BMI by ' + str(round(bmi_value_to_lower, 1)) + ' points')
    elif bmi_value >= 18.5 and bmi_value < 25:
        print('Your BMI is in a healthy range.')
    else:
        print('Your BMI is in the underweight range. Increasing your BMI will not help lower your cost, but it will help improve your health.')

# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
    estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
    print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
    analyze_smoker(smoker)
    analyze_bmi(bmi)
    return estimated_cost
 
# Estimate Keanu's insurance cost:
keanu_insurance_cost = estimate_insurance_cost(name = 'Keanu', age = 29, sex = 1, bmi = 26.2, num_of_children = 3, smoker = 1)

# Estimate my insurance cost:
geoffrey_insurance_cost = estimate_insurance_cost(name = 'Geoffrey', age = 36, sex = 1, bmi = 24, num_of_children = 0, smoker = 0)