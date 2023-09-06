import pandas as pd

df = pd.read_excel('projects.xlsx')

def extract_project_data(df, project_title):
    project_data = df[df['TITULO'] == project_title][['ID', 'TITULO', 'GESTOR', 'COORDENADOR', 'EMPRESA']]
    return project_data


project_titles = ['title1', 'title2', 'title3', 'title4', 'title5', 'title6', 'title7']

project_data_list = []
for title in project_titles:
    project_data = extract_project_data(df, title)
    project_data_list.append(project_data)

final_data = pd.concat(project_data_list)
final_data.to_excel('output.xlsx', index=False)