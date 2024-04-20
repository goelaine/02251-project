import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv("compbio project csv manipulation core genes testing - Sheet1.csv", skiprows = [1,2])

# Your dictionary of pathways (pathway to set of genes)
pathway_genes = {
    "A": {"123", "234", "345"},
    "B": {"123", "345", "567"},
    # Add more pathways as needed
}

keys = pathway_genes.keys()
min = len(pathway_genes[keys[0]])


# Dictionary to store pathway-wise gene arrays for each column
P = {}

df_excluded_first_column = df.iloc[:, 1:]

# Iterate over each pathway
for col_label, colum in df_excluded_first_column.items():
    # Create an empty dictionary to store gene arrays for each column
    P[col_label] = {}
    
    # Iterate over each column in the DataFrame
    for path in keys:

        length = len(pathway_genes[path])
        if length<min:
            min = length

        genes = pathway_genes[path]
        # Initialize an empty list to store genes in the pathway for this column
        P[col_label][path] = []
        
        # Iterate over each gene in the column
        for g in genes:
            # Check if the gene belongs to the pathway
            for index, row in df.interrows():
                if g == row[0]:
                    P[col_label][path].append(row[col_label])
                break
        
        # Store the gene array for this column and pathway
        # pathway_gene_arrays[pathway][column_name] = genes_in_column
print(P)
print(min)
# Now pathway_gene_arrays contains pathway-wise gene arrays for each column
# pathway_gene_arrays[pathway][column_name] gives the gene array for pathway and column_name
