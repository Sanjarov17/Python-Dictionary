config = {}
for i in range(3):
    key = input(f"{i+1}-setting nomini kiriting: ")
    value = input(f"{key} uchun qiymat kiriting: ")
    config[key] = value
print(config)
