# How certain factors contribute to medical insurance costs. 
# Using a formula that estimates a person’s yearly insurance costs, investigate how different factors such as 
# age, sex, BMI, etc. affect the prediction.

# Variables for estimating medical insurance cost
age = 28
sex = 0                 #0 for female, 1 for male
bmi = 26.2              #individual’s body mass index
num_of_children = 3     #number of children the individual has
smoker = 0              #0 for a non-smoker, 1 for a smoker

## Insurance cost formula and message
insurance_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
message = 'This person\'s insurance cost is ' + str(insurance_cost) + ' dollars.'

## Age +4, insurance cost formula and message
age += 4
new_insurance_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
new_cost_message = 'The change in cost of insurance after increasing the age by 4 years is ' + str(change_in_insurance_cost) + ' dollars.'

##BMI factor
age = 28
bmi += 3.1
new_insurance_cost_bmi = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
change_in_insurance_cost_bmi = new_insurance_cost_bmi - insurance_cost
new_cost_message_bmi = 'The change in estimated insurance cost after increasing BMI by 3.1 is ' + str(change_in_insurance_cost_bmi) + ' dollars.'

##Male vs. Female Factor
bmi = 26.2
sex = 1
new_insurance_cost_sex = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
change_in_insurance_cost_sex = new_insurance_cost_sex - insurance_cost
new_cost_message_sex = 'The change in estimated cost for being male instead of female is ' + str(change_in_insurance_cost_sex) + ' dollars.'

print(message)
print(new_cost_message)
print(new_cost_message_bmi)
print(new_cost_message_sex)