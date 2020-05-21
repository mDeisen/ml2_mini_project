import pandas as pd


# Takes a dataframe, the column to groupby, and a list of columns
# Applies percent change to columns within each group
def apply_pct_change(df: pd.DataFrame, groupby: str,
                         columns: list) -> pd.DataFrame:
    ids = df[groupby].unique()
    output_df = pd.DataFrame()

    for current_id in ids:
        current = df.loc[df[groupby] == current_id]
        current[columns] = current[columns].pct_change(fill_method='ffill')
        output_df = output_df.append(current)
    return output_df
