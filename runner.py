from utils import *
from graphing_tools import *
import pandas as pd


def get_all_heatmap_entities(dataset: pd.DataFrame, op_folder: str):
    segment_sizes = get_segment_sizes(dataset)
    system_names = get_system_names(dataset)
    for system in system_names:
        for segment in segment_sizes:
            (get_heatmap_system_segsize(dataset, segment, system).drop_duplicates().
             to_csv(f"{op_folder}/{system}_{segment}.csv", index=False))


if __name__ == '__main__':
    DATASET_FILE_1M20PHS = "./dataset/1m20phs.csv"
    DATASET_FILE_8M20PHS = "./dataset/8m20phs.csv"
    dataset_dataframe = read_pandas_dataset(DATASET_FILE_8M20PHS)
    get_all_heatmap_entities(dataset_dataframe, "./dataset/8m20phs/heatmap")
