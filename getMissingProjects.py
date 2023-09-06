import pandas as pd

df = pd.read_excel('projects.xlsx')

# Defining the list of numbers
numbers_list = [1, 2, 3, 4, 5, 6, 7]

# Converting the "Item" column to a set for faster lookup
items_set = set(df['Item'])

# Finding missing numbers
missing_numbers = [num for num in numbers_list if num not in items_set]

print("Missing numbers:", missing_numbers)