# Read a CSV file containing sales data. Calculate the total sales for 
#each product and write the results to a new CSV file.

import pandas as pd

def calculate_total_sales(input_file, output_file):
    try:
        # Read the sales data from the input CSV file
        df = pd.read_csv(input_file)

        # Group by 'Product' and sum the 'Sales'
        total_sales = df.groupby('Product', as_index=False)['Sales'].sum()

        # Rename the columns for clarity
        total_sales.columns = ['Product', 'Total Sales']

        # Write the total sales to the output CSV file
        total_sales.to_csv(output_file, index=False)

        print(f"Total sales have been written to {output_file}.")
    
    except FileNotFoundError:
        print(f"The file {input_file} does not exist.")
    except KeyError as e:
        print(f"Missing expected column in the CSV file: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_file = 'sales_data.csv'  
output_file = 'total_sales.csv'  
calculate_total_sales(input_file, output_file)