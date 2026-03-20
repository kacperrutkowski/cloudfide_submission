import pandas as pd
import string
import re
df_fruits = pd.DataFrame({"product" : ["banana", "apple"],
                   "quantity" : [10, 3],
                   "price" : [10, 1]})
print(df_fruits)

def check_column_name(column_name, allowed_symbols):
    #checks if the name of the column consists of allowed symbols
    if set(column_name).issubset(allowed_symbols):
        return True
    else:
        return False

def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame:

    df = df.copy()
    df_column_names = df.columns.tolist()
    column1, operation, column2 = re.findall(r'[^\s+\-*]+|[+\-*]', role)

    # checking if names of columns given in role are the names of the columns in df
    if column1 not in df_column_names or column2 not in df_column_names:
        return pd.DataFrame()

    #checking if columns has right names
    all_columns = df_column_names + [column1, column2] + [new_column]
    allowed_symbols = string.ascii_uppercase + string.ascii_lowercase + "_"
    for column_name in all_columns:
        if not check_column_name(column_name, allowed_symbols):
            return pd.DataFrame()

    #the main mechanism of the function, performs mathematical operations between columns
    if operation == "+":
        df[new_column] = df[column1] + df[column2]
    elif operation == "-":
        df[new_column] = df[column1] - df[column2]
    elif operation == "*":
        df[new_column] = df[column1] * df[column2]
    return df

df_fruits = add_virtual_column(df_fruits, "quantity + price", "fruits")
print(df_fruits)

