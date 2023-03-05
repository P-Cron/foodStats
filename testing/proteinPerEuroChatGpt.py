price_per_kg = float(input("Enter the price per kg: "))
calories_per_100g = float(input("Enter the number of calories per 100g: "))
protein_per_100g = float(input("Enter the amount of protein per 100g: "))

calories_per_kg = calories_per_100g * 10
protein_per_kg = protein_per_100g * 10

calories_per_euro = calories_per_kg / price_per_kg
protein_per_euro = protein_per_kg / price_per_kg

print("Calories per euro: {:.2f}".format(calories_per_euro))
print("Protein per euro: {:.2f}".format(protein_per_euro))