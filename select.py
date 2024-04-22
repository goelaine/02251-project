import pandas as pd
from get_symbols import *
# This is the code to remove the numbers in the first column and to filter out unnecessary genes 

# Function to extract substring before '|'
def extract_substring(text):
    return text.split('|')[0]

df = pd.read_csv("/Users/wanbo/Desktop/TNexp.csv", skiprows = [1])

df.iloc[:, 0] = df.iloc[:, 0].str.split('|').str[0]

allGenes = set()

pathway_genes = getDict()
for key in pathway_genes:
    allGenes = allGenes | set(pathway_genes[key])

filtered_df = df[df.iloc[:, 0].isin(allGenes)]

filtered_df.to_csv("selected_genes2.csv", index = False)