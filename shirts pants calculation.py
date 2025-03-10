"""shirts=[
    {"name":"cotton shirts","price": 550},
    {"name":"linen shirts", "price": 600},
    {"name":"denim shirts", "price": 700},
    {"name":"formal shirts","price": 800}
]
pants=[
    {"name":"cotton pants","price": 600},
    {"name":"linen pants", "price": 650},
    {"name":"denim pants", "price": 750},
    {"name":"formal pants","price": 850}
]
#user input for shirts section:

print("available Shirts")
for index,shirts in enumerate(shirts,start=1):
    print(f"{index}.{shirts['name']}-${shirts['price']}")
shirt_choice=int(input("Enter the shirt number:"))-1
selected_shirt=shirts[shirt_choice]

#user input for shirts size:
shirt_size=input("Enter the shirt size (M,L,XL,XXL):")
if shirt_size() not in ["M","L","XL","XXL"]:
    print("Invalid size")
    shirt_size=input("Enter the shirt size (M,L,XL,XXL):")

#user input for pants section:
print("\navailable Pants:")

for index,pants in enumerate(pants,start=1):
    print(F"{index}.{pants['name']}-${pants['price']}")
pants_choice=int(input("Enter the pants number:"))-1
selected_pants=pants[pants_choice]

#user input for pants size:
pants_size=input("Enter the pants size (30,32,34,36):")

if pants_size.upper() not in ["30","32","34","36"]:
    print("Invalid size")
    pants_size=input("Enter the pants size (30,32,34,36):")

#display selectred products:
print("\nSelected products are:")

print(f"1.Shirt: {selected_shirt['name']} - Size: {shirt_size} - Price: {selected_shirt['price']}")

print(f"2.Pants: {selected_pants['name']} - Size: {pants_size} - Price: {selected_pants['price']}")

#total price calculation:
total_price=selected_shirt['price']+selected_pants['price']
print(f"\nTotal price: ${total_price}")
"""

shirts = [
    {"name": "Cotton Shirt", "price": 500},
    {"name": "Linen Shirt", "price": 700},
    {"name": "Denim Shirt", "price": 1000},
    {"name": "Formal Shirt", "price": 800}
]

pants = [
    {"name": "Jeans Pant", "price": 1200},
    {"name": "Chinos Pant", "price": 1000},
    {"name": "Formal Pant", "price": 1500},
    {"name": "Cargo Pant", "price": 1300}
]

# User input for Shirt Selection
print("Available Shirts:")
for index, shirt in enumerate(shirts, start=1):
    print(f"{index}. {shirt['name']} - ₹{shirt['price']}")
shirt_choice = int(input("Select Shirt by number: ")) - 1
selected_shirt = shirts[shirt_choice]

# User Input for Shirt Size
shirt_size = input("Enter Shirt Size (M, L, XL, XXL): ")
if shirt_size.upper() not in ["M", "L", "XL", "XXL"]:
    print("Invalid size, default size M selected")
    shirt_size = "M"

# User input for Pant Selection
print("\nAvailable Pants:")
for index, pant in enumerate(pants, start=1):
    print(f"{index}. {pant['name']} - ₹{pant['price']}")
pant_choice = int(input("Select Pant by number: ")) - 1
selected_pant = pants[pant_choice]

# User Input for Pant Size
pant_size = input("Enter Pant Size (30, 32, 34, 36): ")
if pant_size not in ["30", "32", "34", "36"]:
    print("Invalid size, default size 32 selected")
    pant_size = "32"

# Display Selected Products
print("\nSelected Products:")
print(f"1. Shirt: {selected_shirt['name']} ({shirt_size}) - ₹{selected_shirt['price']}")
print(f"2. Pant: {selected_pant['name']} ({pant_size}) - ₹{selected_pant['price']}")

# Calculate Total Price
total_price = selected_shirt['price'] + selected_pant['price']
print(f"\nTotal Price: ₹{total_price}")
