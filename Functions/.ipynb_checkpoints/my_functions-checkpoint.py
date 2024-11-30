
    import pandas as pd

def check_duplicates_rows(df):
   
    if df.duplicated().any():
        return "Duplicates found."
    else:
        return "No duplicates." 