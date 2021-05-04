
#https://pythonbasics.org/pandas-web-scraping/

import pandas as pd

# Webpage url
url = 'https://www.bls.gov/oes/current/oes_nat.htm'

# Extract tables
dfs = pd.read_html(url)

# Get first table
df = dfs[0]

# Extract columns
df2 = df[['Occupation code','Level']]
print(df2)

df.to_excel("scraped_output.xlsx")