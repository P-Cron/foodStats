import json

# Load the previous results from a JSON file
try:
    with open("results.json", "r") as f:
        previous_results = json.load(f)
except FileNotFoundError:
    previous_results = []

weightInput = input("Enter the weight in grams, the default is 1kg if left blank: ")

weight = 1000.0 if weightInput.isspace()  else float(weightInput)
priceForWeight = float(input("Enter the price per weight given (({}g): ".format(weight)))
pricePer100g = (priceForWeight / weight)

calories_per_100g = float(input("Enter the number of calories per 100g: "))
protein_per_100g = float(input("Enter the amount of protein in grams per 100g: "))

calories_per_euro = calories_per_100g / pricePer100g
protein_per_euro = protein_per_100g / pricePer100g

# Add the new results to the list of previous results
previous_results.append({"pricePer100g": pricePer100g,
                         "pricePerKg": pricePer100g*10,
                         "calories_per_euro": calories_per_euro,
                         "protein_per_euro": protein_per_euro})

# Save the updated list of results to the JSON file
with open("results.json", "w") as f:
    json.dump(previous_results, f)

print("Calories per euro: {:.2f}".format(calories_per_euro))
print("Protein per euro: {:.2f}".format(protein_per_euro))