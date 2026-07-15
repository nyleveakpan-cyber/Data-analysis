import os

print("Current folder:", os.getcwd())
print("Files:", os.listdir())

filename = "life-expectancy.csv"

lowest = float("inf")
highest = float("-inf")

with open(filename) as file:
    next(file)  # Skip header

    for line in file:
        parts = line.strip().split(",")

        life_expectancy = float(parts[3])

        if life_expectancy < lowest:
            lowest = life_expectancy

        if life_expectancy > highest:
            highest = life_expectancy

print(f"The lowest life expectancy is: {lowest}")
print(f"The highest life expectancy is: {highest}")