import seaborn
import seaborn as sns
import pandas as pd


def plot_segment_interim(system_dict: dict, system_name: str):

    sns_plot = []
    for keys in system_dict.keys():
        sns_plot = seaborn.lineplot(data=system_dict[keys], x='achieved_load_pps', y='p99', label=keys)

    sns_plot.savefig(f'./dataset/1m20phs/segmented/{system_name}_p99.png')

    # seaborn.lineplot(data=system_dict['2mb_pages'], x='offered_load', y='achieved_load', label='2mb_pages')



def plot_segment_sized(system_dict: dict, segment_size: str, system_name: str):
    pass