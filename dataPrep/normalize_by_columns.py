import pandas as pd
from sklearn import preprocessing

# Takes a dataframe, the column to groupby, and a list of columns
# Normalizes them within each group
def normalize_by_columns(df: pd.DataFrame, groupby: str, columns: list) -> pd.DataFrame:
    ids = df[groupby].unique()
    output_df = pd.DataFrame()

    for current_id in ids:
        current = df.loc[df[groupby] == current_id]
        current[columns] = current[columns].apply(lambda x: (x - x.min()) / (x.max() - x.min()))
        output_df = output_df.append(current)
    return output_df

