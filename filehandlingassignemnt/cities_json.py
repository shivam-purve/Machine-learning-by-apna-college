import json

# Step 1: Create and save cities
cities = {
    "Delhi": 32900000,
    "Mumbai": 20800000,
    "Bangalore": 13600000
}

with open("./filehandlingassignemnt/cities.json", "w") as f:
    json.dump(cities, f, indent=4)

# Step 2: Load and display cities
with open("./filehandlingassignemnt/cities.json", "r") as f:
    cities = json.load(f)

for city, population in cities.items():
    print(f"{city} : {population}")

# Step 3: Take user input
new_city = input("Enter new city name: ")
new_population = int(input("Enter population: "))

# Update dictionary
cities[new_city] = new_population

# Step 4: Save updated data
with open("./filehandlingassignemnt/cities.json", "w") as f:
    json.dump(cities, f, indent=4)

print("City added successfully!")
