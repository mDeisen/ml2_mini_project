import pandas as pd

# Takes a dataframe, the groupby, collapse_on and a threshold parameter
# Returns a dataframe that contains the grouped by data from the point >=
# threshhold. Starting at index 0 for each group.
def collapse_dataframe_into_new(df: pd.DataFrame, groupby: str, collapse_on: str, threshhold: int) -> pd.DataFrame:
    ids = df[groupby].unique()
    output_df = pd.DataFrame()

    for current_id in ids:
        current = df.loc[df[groupby] == current_id]

        # Apparently fastest way to do this:
        # https://stackoverflow.com/questions/47601118/find-only-the-first-row-satisfying-a-given-condition-in-pandas-dataframe
        for j in range(len(current)):
            if current[collapse_on].iloc[j] >= threshhold:
                first_row_threshold = j
                current.reset_index(inplace=True)
                current = current.truncate(before=first_row_threshold)
                current.reset_index(inplace=True)
                output_df = output_df.append(current)
                break
    return output_df

