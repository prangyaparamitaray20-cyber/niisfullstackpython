def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Calling with varying keyword arguments
print_info(name="Alice", age=30, city="New York")
# Output:
# name: Alice
# age: 30
# city: New York
print_info(brand="Toyota", model="Corolla", year=2020)
# Output:
# brand: Toyota
# model: Corolla
# year: 2020