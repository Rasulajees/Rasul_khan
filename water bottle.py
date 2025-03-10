water_level=0
max_capacity=1000
fill_rate=200

while water_level <max_capacity:
    water_level += fill_rate
    print(f'Water level: {water_level} liters')

print('Water tank is full')