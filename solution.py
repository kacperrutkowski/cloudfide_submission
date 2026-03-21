import pandas as pd
import string
import re

def check_column_name(column_name, allowed_symbols):
    #checks if the name of the column consists of allowed symbols
    if set(column_name).issubset(allowed_symbols):
        return True
    else:
        return False

def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame:

    df = df.copy()
    columns_and_operators = re.findall(r'[^\s+\-*]+|[+\-*]', role)

    # there must be one operator and two column names
    if  len(columns_and_operators) != 3:
        return pd.DataFrame()
    else:
        column1, operation, column2 = columns_and_operators

    # checking if names of columns given in role are the names of the columns in df
    if (column1 not in df.columns) or (column2 not in df.columns):
        return pd.DataFrame()

    # both columns must be of type int or float
    if (not pd.api.types.is_numeric_dtype(df[column1])) or (not pd.api.types.is_numeric_dtype(df[column2])):
        return pd.DataFrame()

    #checking if columns has right names
    allowed_symbols = string.ascii_uppercase + string.ascii_lowercase + "_"
    for column_name in [column1, column2, new_column]:
        if not check_column_name(column_name, allowed_symbols):
            return pd.DataFrame()

    #the main mechanism of the function, performs mathematical operations between columns
    if operation == "+":
        df[new_column] = df[column1] + df[column2]
    elif operation == "-":
        df[new_column] = df[column1] - df[column2]
    elif operation == "*":
        df[new_column] = df[column1] * df[column2]
    else: #the operation is not supported
        return pd.DataFrame()

    return df