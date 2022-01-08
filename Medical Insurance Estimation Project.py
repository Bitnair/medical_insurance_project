Examine how factors such as age, sex, BMI, number of children, and smoking status contribute to medical insurance costs.

names = []
estimated_insurance_data = []
insurance_costs = [4150.0, 5320.0, 35210.0]  # The cost people actually paid
insurance_data = zip(names, insurance_costs) # pair names and insurance_costs in the list insurance_data

# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
  estimated_insurance_data.append((name, estimated_cost))
  names.append(name)
  return estimated_cost
 
# Estimate people's insurance cost
maria_insurance_cost = estimate_insurance_cost(name = "Maria", age = 31, sex = 0, bmi = 23.1, num_of_children = 1, smoker = 0)
rohan_insurance_cost = estimate_insurance_cost(name = "Rohan", age = 25, sex = 1, bmi = 28.5, num_of_children = 3, smoker = 0)
valentina_insurance_cost = estimate_insurance_cost(name = "Valentina", age = 53, sex = 0, bmi = 31.4, num_of_children = 0, smoker = 1)

insurance_data_converted = list(insurance_data)

print('The actual insurance cost is : ', str(insurance_data_converted))
print('The estimated insurance cost is : ', str(estimated_insurance_data))