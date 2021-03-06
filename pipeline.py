import pandas as pd

from ml2_mini_project.dataPrep.apply_moving_average import apply_moving_average
from ml2_mini_project.dataPrep.apply_pct_change import apply_pct_change
from ml2_mini_project.dataPrep.collapse_dataframe_into_new import \
    collapse_dataframe_into_new
from ml2_mini_project.dataPrep.normalize_by_columns import normalize_by_columns

# Choose the column that data should be grouped by (such as countries, regions
# etc. Assumes, that a column contains multiple groups.
# str
groupby = 'country_region'

# Choose the column that should be checked against a condidion to collapse the
# data
# str
collapse_on = 'Deaths'

# Choose the threshhold that each group should start on (e.g. start at 50
# cases)
# int
threshhold = 20


# Define the columns that should be normalized (after collapse)
# list
columns_to_normalize = ["Cases", "Deaths"]

# Apply moving average window (will be applied to columns_to_normalize)
# int
window = 7

# Choose the input file
df = pd.read_csv('./2020-05-16_GoogleMobilityDataGlobal_joined.csv')

# First collapse the data Collapse step
df = collapse_dataframe_into_new(df, groupby, collapse_on, threshhold)
df.to_csv('./collapse_on_' + collapse_on + '.csv')

# Normalization step
# Only necessary if change in %_cases is not used
# df = normalize_by_columns(df, groupby, columns_to_normalize)
# df.to_csv('./normalized_df.csv')

# Try Moving Average over period X
df = apply_moving_average(df, groupby, columns_to_normalize, window)
df.to_csv('./moving_average.csv')

# Calculate %_change in target variable
df = apply_pct_change(df, groupby, columns_to_normalize)
df.to_csv('./pct_change.csv')

