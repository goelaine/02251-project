import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv("your_csv_file.csv")

# Your dictionary of pathways (pathway to set of genes)
pathway_genes = {
    "pathway1": {"gene1", "gene2", "gene3"},
    "pathway2": {"gene4", "gene5", "gene6"},
    # Add more pathways as needed
}

# Dictionary to store pathway-wise gene arrays for each column
pathway_gene_arrays = {}

# Iterate over each pathway
for pathway, genes_in_pathway in pathway_genes.items():
    # Create an empty dictionary to store gene arrays for each column
    pathway_gene_arrays[pathway] = {}
    
    # Iterate over each column in the DataFrame
    for column_name, column_data in df.iteritems():
        # Initialize an empty list to store genes in the pathway for this column
        genes_in_column = []
        
        # Iterate over each gene in the column
        for gene in column_data:
            # Check if the gene belongs to the pathway
            if gene in genes_in_pathway:
                genes_in_column.append(gene)
        
        # Store the gene array for this column and pathway
        pathway_gene_arrays[pathway][column_name] = genes_in_column

# Now pathway_gene_arrays contains pathway-wise gene arrays for each column
# pathway_gene_arrays[pathway][column_name] gives the gene array for pathway and column_name
