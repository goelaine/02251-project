import pandas as pd

# Function to extract substring before '|'
def extract_substring(text):
    return text.split('|')[0]

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


df = pd.read_csv("/Users/wanbo/Desktop/compbio project csv manipulation core genes testing - Sheet1.csv", skiprows = [1, 2])

# Your dictionary of pathways (pathway to set of genes)
pathway_genes = {
    "A": {"123", "234", "345"},
    "B": {"123", "345", "567"},
    # Add more pathways as needed
}

keys = pathway_genes.keys()
min = 1000


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

        
        first_col = df.iloc[:, 0]
        # num_rows = len(first_col)
        
        # Iterate over each gene in the column
        for g in genes:
            # Check if the gene belongs to the pathway
            # for index, row in df.iterrows():
            ind = binary_search(first_col,int(g))
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
        # sortedExp = sorted(G[patient][pathway]).reverse()
        n = len(sortedExp)
        # for i in range(len(sortedExp)):
        for i in range(min):
            score = sortedExp[i] * (n - i) / n
            #ASD;LKFJAS;DLFJS SHOULD BE N HERE? OR MIN? IDKKKKKKKKDKFA;LSDKJFA;LSKDJF;ALKJSDF;LKAJ
            total += score
        G[patient][pathway] = total

# Now pathway_gene_arrays contains pathway-wise gene arrays for each column
# pathway_gene_arrays[pathway][column_name] gives the gene array for pathway and column_name