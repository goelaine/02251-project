import pandas as pd

df = pd.read_csv("/Users/wanbo/Desktop/MATRIX_yang.csv", index_col=0)  # Assuming row index represents pathways

# Standardize the data across each row (pathway)
standardized_data = (df.sub(df.mean(axis=1), axis=0)).div(df.std(axis=1), axis=0)

# Save the standardized data to a new CSV file
standardized_data.to_csv("standardized_data_yang.csv")