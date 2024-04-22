import pandas as pd
from get_symbols import *
import random


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        # Check if the target is present at mid
        if arr[mid] == target:
            return mid
        
        # If the target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
        
        # If the target is smaller, ignore right half
        else:
            right = mid - 1
    
    # If the element is not present in the array
    return -1

def getExp():

    df = pd.read_csv("/Users/wanbo/Desktop/selected_genes.csv")

    # Your dictionary of pathways (pathway to set of genes)
    pathway_genes = getDict()

    # print(pathway_genes)

    keys = pathway_genes.keys()
    min = 1000

    # reduce the number of genes
    for key in pathway_genes:
        length = len(pathway_genes[key])
        if length<min:
            min = length


    # Dictionary to store pathway-wise gene arrays for each column
    P = {}

    df_excluded_first_column = df.iloc[:, 1:]

    # Iterate over each pathway
    for col_label, colum in df_excluded_first_column.items():
        # Create an empty dictionary to store gene arrays for each column
        P[col_label] = {}

        
        # Iterate over each column in the DataFrame
        for path in keys:

            # length = len(pathway_genes[path])
            # if length<min:
            #     min = length


            genes = pathway_genes[path]
            # Initialize an empty list to store genes in the pathway for this column
            P[col_label][path] = []
            
            first_col = df.iloc[:, 0]
            # num_rows = len(first_col)
            
            # Iterate over each gene in the column
            for g in genes:
                # Check if the gene belongs to the pathway
                # for index, row in df.iterrows():
                ind = binary_search(first_col,g)
                if ind != -1:
                    P[col_label][path].append(df.iloc[ind][col_label])
                        # break
                P[col_label][path].sort(reverse=True)
            
            # Store the gene array for this column and pathway
            # pathway_gene_arrays[pathway][column_name] = genes_in_column
    print(P)
    print(min)

    G = P # result from previous code

    for patient in G:
        for pathway in G[patient]:
            total = 0
            sortedExp = G[patient][pathway]
            n = len(sortedExp)
            
            for i in range(n):
                # if i > n:
                #     print(i, sortedExp)
                score = sortedExp[i] * (n - i) / n
                total += score
            G[patient][pathway] = total
    
    for path in keys:
        # sumPath = sum([G[patient][path] for patient in G])
        for patient in G:
            G[patient][path] = G[patient][path]/sum([G[patient][path] for path in G[patient]])
    return G

data = getExp()

df = pd.DataFrame.from_dict(data, orient='index')

transposed_df = df.transpose()

# Write the DataFrame to a CSV file
transposed_df.to_csv('MATRIXXX.csv')
    # Now pathway_gene_arrays contains pathway-wise gene arrays for each column
    # pathway_gene_arrays[pathway][column_name] gives the gene array for pathway and column_name