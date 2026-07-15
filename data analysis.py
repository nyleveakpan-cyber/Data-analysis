# Life Expectancy Assignment

filename = "life-expectancy.csv"

# Initialize overall values
overall_max = -1
overall_min = 999

overall_max_country = ""
overall_max_year = ""

overall_min_country = ""
overall_min_year = ""

# Ask the user for a year
year_choice = input("Enter the year of interest: ")

# Variables for selected year
year_total = 0
year_count = 0

year_max = -1
year_min = 999

year_max_country = ""
year_min_country = ""

with open(filename) as file:
    # Skip the header row
    next(file)

    for line in file:
        parts = line.strip().split(",")

        country = parts[0]
        year = parts[2]
        life_expectancy = float(parts[3])

        # Overall maximum
        if life_expectancy > overall_max:
            overall_max = life_expectancy
            overall_max_country = country
            overall_max_year = year

        # Overall minimum
        if life_expectancy < overall_min:
            overall_min = life_expectancy
            overall_min_country = country
            overall_min_year = year

        # Data for the chosen year
        if year == year_choice:
            year_total += life_expectancy
            year_count += 1

            if life_expectancy > year_max:
                year_max = life_expectancy
                year_max_country = country

            if life_expectancy < year_min:
                year_min = life_expectancy
                year_min_country = country

# Display overall results
print()
print(f"The overall max life expectancy is: {overall_max:.3f} from {overall_max_country} in {overall_max_year}")
print(f"The overall min life expectancy is: {overall_min:.3f} from {overall_min_country} in {overall_min_year}")

# Display results for selected year
print()

if year_count > 0:
    average = year_total / year_count

    print(f"For the year {year_choice}:")
    print(f"The average life expectancy across all countries was {average:.2f}")
    print(f"The max life expectancy was in {year_max_country} with {year_max:.3f}")
    print(f"The min life expectancy was in {year_min_country} with {year_min:.3f}")
else:
    print(f"No data was found for the year {year_choice}.")