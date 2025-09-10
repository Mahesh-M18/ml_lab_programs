import csv
import random

# -----------------------------
# Define categories
# -----------------------------
age_values = ['SuperSeniorCitizen', 'SeniorCitizen', 'MiddleAged', 'Youth', 'Teen']
gender_values = ['Male', 'Female']
family_history_values = ['Yes', 'No']
diet_values = ['High', 'Medium', 'Low']
lifestyle_values = ['Athlete', 'Active', 'Moderate', 'Sedetary']
cholesterol_values = ['High', 'BorderLine', 'Normal']
heart_disease_values = ['Yes', 'No']

# -----------------------------
# Generate synthetic dataset
# -----------------------------
rows = []
num_samples = 200  # change this to make dataset larger/smaller

for _ in range(num_samples):
    age = random.choice(age_values)
    gender = random.choice(gender_values)
    family_history = random.choice(family_history_values)
    diet = random.choice(diet_values)
    lifestyle = random.choice(lifestyle_values)
    cholesterol = random.choice(cholesterol_values)

    # Simple heuristic rule to generate target
    if (age in ['SuperSeniorCitizen', 'SeniorCitizen']) and (cholesterol == 'High') and (lifestyle in ['Moderate', 'Sedetary']):
        heart_disease = 'Yes'
    elif (family_history == 'Yes' and cholesterol == 'High'):
        heart_disease = 'Yes'
    else:
        heart_disease = random.choice(heart_disease_values)

    rows.append([age, gender, family_history, diet, lifestyle, cholesterol, heart_disease])

# -----------------------------
# Save to CSV file
# -----------------------------
filename = "heart_disease_data.csv"
with open(filename, "w", newline="") as f:
    writer = csv.writer(f)
    # ❌ No header (your code expects pure data)
    writer.writerows(rows)

print(f"CSV file '{filename}' with {num_samples} records created successfully!")
