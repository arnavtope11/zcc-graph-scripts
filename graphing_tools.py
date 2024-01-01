import pandas as pd
import seaborn
import matplotlib.pyplot as plt
from utils import get_system_names, get_pinning_limit_for_system, get_segment_sizes_for_system


def plot_tp_latency_graph_const_seg_size(whole_dataframe: pd.DataFrame,
                                         system_name: str,
                                         segment_size: str,
                                         pinning_limit: str):
    system_names = get_system_names(whole_dataframe)
    pinning_limit_dict = {}
    segment_size_dict = {}
    for system_name in system_names:
        pinning_limit_dict[system_name] = get_pinning_limit_for_system(whole_dataframe, system_name)
        segment_size_dict[system_name] = get_segment_sizes_for_system(whole_dataframe, system_name)





def plot_segment_interim(system_dict: dict, system_name: str):

    sns_plot = []
    for keys in system_dict.keys():
        sns_plot = seaborn.lineplot(data=system_dict[keys], x='achieved_load_pps', y='p99', label=keys)

    sns_plot.savefig(f'./dataset/1m20phs/segmented/{system_name}_p99.png')

    # seaborn.lineplot(data=system_dict['2mb_pages'], x='offered_load', y='achieved_load', label='2mb_pages')



def plot_segment_sized(system_dict: dict, segment_size: str, system_name: str):
    pass