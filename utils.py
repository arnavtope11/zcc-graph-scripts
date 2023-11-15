import pandas as pd


def read_pandas_dataset(filename: str):
    return pd.read_csv(filename)


def split_based_on_segment_size(whole_dataframe: pd.DataFrame):
    pass

def get_unique_column_entries(dataframe: pl.DataFrame, column_name):
    return dataframe[column_name].unique()


def convert_to_plotting_dict(dataframe: pl.DataFrame):
    system_names = dataframe[['system']].unique()
    return system_names


def extract_string_from_polars_series(series: pl.Series):
    return series.to_list()[0]