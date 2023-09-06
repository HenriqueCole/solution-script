import pandas as pd

df = pd.read_excel('projects.xlsx')

# Function to remove extra spaces from a string
def remove_extra_spaces(title):
    return ' '.join(title.split())

# Applying the function to the 'TITULO' column to remove extra spaces
df['TITULO'] = df['TITULO'].apply(remove_extra_spaces)

# Saving the updated DataFrame to a new excel file
df.to_excel('projects_updated.xlsx', index=False)

print("Excel file updated with extra spaces removed.")
