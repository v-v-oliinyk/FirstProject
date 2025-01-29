salaries_2023 = {
    "John": 50000,
    "Alice": 60000,
    "Bob": 45000,
    "Eve": 52000
}

salaries_updates_2024 = {
    "Alice": 62000,
    "Eve": 54000,
    "Alex": 47000
}

salaries_2023.update(salaries_updates_2024)

for name, salary in salaries_2023.items():
    print(f"{name} have actual salary: {salary}")