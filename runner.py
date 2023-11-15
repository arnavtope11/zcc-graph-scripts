from utils import *
from graphing_tools import *

DATASET_FILE_1M20PHS = "./dataset/1m20phs.csv"
dataset_dataframe = read_pandas_dataset(DATASET_FILE_1M20PHS)
segment_sizes = get_segment_sizes(dataset_dataframe)
system_names = get_system_names(dataset_dataframe)

vanilla_cornflakes_dict = {}
print(segment_sizes)
for seg_size in segment_sizes:
    seg_df = get_tp_lat_graph_entities(dataset_dataframe, seg_size, 'vanilla_cornflakes')
    vanilla_cornflakes_dict[seg_size] = seg_df
    # vanilla_cornflakes_dict[seg_size]['offered_load'] = seg_df['offered_load_pps'].tolist()
    # vanilla_cornflakes_dict[seg_size]['achieved_load'] = seg_df['achieved_load_pps'].tolist()
    # vanilla_cornflakes_dict[seg_size]['p99'] = seg_df['p99'].tolist()

plot_segment_interim(vanilla_cornflakes_dict, segment_sizes, 'vanilla_cornflakes')
