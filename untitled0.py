from openpyxl import load_workbook
import pandas as pd


wb = load_workbook(filename='2022 Carga MBI v3.xlsx', data_only=True)



ws = wb['MBI META']

#sadasd

data = ws.values

# Get the first line in file as a header line

columns = next(data)[0:]

# Create a DataFrame based on the second and subsequent lines of data

df = pd.DataFrame(data, columns=columns)



df.head(30)
#hola