import numpy as np
import pandas as pd

# Generate data for 1000 people
num_people = 1000

# Generate random names
names = np.random.choice(['John', 'Jane', 'Michael', 'Emma', 'William', 'Olivia', 'James', 'Sophia'], num_people)

# Generate random ages between 18 and 60
ages = np.random.randint(18, 61, num_people)

# Basic Needs
food_supply = np.random.randint(0, 31, num_people)  # days of food supply
water_per_day = np.random.uniform(1, 5, num_people)  # liters of water per day per person

# Health and Medical Supplies
first_aid_kits = np.random.randint(0, 11, num_people)
antibiotics = np.random.randint(0, 21, num_people)
painkillers = np.random.randint(0, 51, num_people)

# Security and Defense
weapons_available = np.random.randint(0, 101, num_people)  # number of weapons available
defensive_structures = np.random.randint(0, 11, num_people)  # number of defensive structures
training_level = np.random.randint(0, 6, num_people)  # level of combat training (0-5)

# Communication and Information
radios_available = np.random.randint(0, 21, num_people)  # number of radios available
reliable_information = np.random.choice(["Yes", "No"], num_people)

# Psychological Well-being
support_groups_available = np.random.choice(["Yes", "No"], num_people)
entertainment_available = np.random.choice(["Books", "Games"], num_people)

# Create a DataFrame
data = pd.DataFrame({
    'Name': names,
    'Age': ages,
    'Food Supply (Days)': food_supply,
    'Water per Day (Liters)': water_per_day,
    'First Aid Kits': first_aid_kits,
    'Antibiotics': antibiotics,
    'Painkillers': painkillers,
    'Weapons Available': weapons_available,
    'Defensive Structures': defensive_structures,
    'Training Level': training_level,
    'Radios Available': radios_available,
    'Access to Reliable Information': reliable_information,
    'Support Groups Available': support_groups_available,
    'Entertainment Available': entertainment_available
})

# Save to CSV
data.to_csv('war_survival_data.csv', index=False)

print("Data saved to war_survival_data.csv")
