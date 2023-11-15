import pandas as pd


# ['Unnamed: 0', 'system', 'size_distr', 'avg_size', 'num_keys', 'num_values', 'num_threads', 'num_clients',
# 'load_trace', 'access_trace', 'offered_load_pps', 'offered_load_gbps', 'num_pages_per_mempool', 'register_at_start',
# 'pinning_limit_2mb_pages', 'segment_size_2mb_pages', 'pin_on_demand', 'pinning_frequency_millis', 'achieved_load_pps',
# 'achieved_load_pps_sent', 'achieved_load_gbps', 'achieved_load_gbps_sent', 'percent_achieved_rate', 'avg', 'median',
# 'p99', 'p999']

VANILLA_CORNFLAKES_SYSTEM = 'vanilla_cornflakes'
ZCC_CORNFLAKES_MFU_SYSTEM = 'zcc_cornflakes_mfu'
CORNFLAKES_COPY = 'cornflakes_copy'

def read_pandas_dataset(filename: str):
    return pd.read_csv(filename)

def get_system_names(whole_dataframe: pd.DataFrame):
    return whole_dataframe['system'].unique().tolist()

def get_segment_sizes(whole_dataframe: pd.DataFrame):
    return whole_dataframe['segment_size_2mb_pages'].unique().tolist()

def get_offered_loads(whole_dataframe: pd.DataFrame):
    return whole_dataframe['offered_load_pps'].unique().tolist()

def get_p99s(whole_dataframe: pd.DataFrame):
    return whole_dataframe['p99'].unique().tolist()

def get_achievable_loads(whole_dataframe: pd.DataFrame):
    return whole_dataframe['achievable_load_pps'].unique().tolist()

def plot_throughput_latency_graph_system_segment(whole_dataframe: pd.DataFrame,
                                                 op_folder: str,
                                                 system_name: str,
                                                 segment_size: int):
    stripped_dataframe = whole_dataframe[['system', 'segment_size_2mb_pages', 'offered_load_pps', 'p99',
                                          'achievable_load_pps']]
    print(stripped_dataframe.head())



def split_based_on_segment_size(whole_dataframe: pd.DataFrame, op_folder: str):
    segment_sizes = whole_dataframe['segment_size_2mb_pages'].unique()
    segmented_dataframes = [whole_dataframe[whole_dataframe['segment_size_2mb_pages'] == _] for _ in segment_sizes]
    for dataframe in segmented_dataframes:
        system_dataframe = [dataframe[dataframe['system'] == _] for _ in dataframe['system'].unique()]
        for sys_df in system_dataframe:
            dropped_column_df = sys_df.drop(columns=['Unnamed: 0'])
            dropped_column_df.drop_duplicates(inplace=True)
            segment_size_string = dataframe['segment_size_2mb_pages'].unique().item()
            system_string = sys_df['system'].unique().item()
            dropped_column_df.to_csv(f'./{op_folder}/1m20phs_{segment_size_string}_{system_string}.csv', index=False)



if __name__ == '__main__':
    # split_based_on_segment_size(read_pandas_dataset('./dataset/1m20phs.csv'), op_folder='./dataset/1m20phs/segmented')
    
    plot_throughput_latency_graph_system_segment(read_pandas_dataset('./dataset/1m20phs.csv'),
                                                 op_folder='./dataset/1m20phs/segmented',
                                                 system_name=VANILLA_CORNFLAKES_SYSTEM,
                                                 segment_size=)