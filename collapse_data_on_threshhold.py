import pandas as pd

# Choose the column that data should be grouped by (such as countries, regions
# etc. Assumes, that a column contains multiple groups.
groupby = 'country_region'

# Choose the column that should be checked against a condidion to collapse the
# data
collapse_on = 'Cases'

# Choose the input file
df = pd.read_csv('./2020-05-03_GoogleMobilityDataGlobal_joined.csv')

# Choose the threshhold that each group should start on (e.g. start at 50
# cases)
threshhold = 50


# Takes a dataframe, the groupby and collapse_on parameter and a threshold
# Returns a dataframe that contains the grouped by data from the point >=
# threshhold. Starting at index 0 for each group.
def collapse_dataframe_into_new(df, groupby, collapse_on, threshhold):
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


collapse_dataframe_into_new(df, groupby, collapse_on, threshhold) \
    .to_csv('collapse_on_' + collapse_on + '.csv')
