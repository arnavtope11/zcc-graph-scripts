import pandas as pd
import seaborn
import matplotlib.pyplot as plt
from utils import (get_system_names, get_pinning_limit_for_system, get_segment_sizes_for_system,
                   get_tp_latency_item_for_system, read_pandas_dataset, get_pinning_limits,
                   get_tp_latency_item_for_segment_pinning_limit)


def two_line_plot(df1: pd.DataFrame, df2: pd.DataFrame, x_axis: str, y_axis: str, title: str):
    sns_plot = seaborn.lineplot(data=df1, x=x_axis, y=y_axis, label='vanilla_cornflakes')
    sns_plot = seaborn.lineplot(data=df2, x=x_axis, y=y_axis, label='cornflakes_copy')
    sns_plot.set_title(title)
    sns_plot.set_xlabel(x_axis)
    sns_plot.set_ylabel(y_axis)
    sns_plot.legend()
    sns_plot.figure.savefig(f'./graphs/1m20phs/{title}.png')


def multiple_line_plot(df_list: list, x_axis: str, y_axis: str, title: str):
    print(f"Length of line plot dict is: {len(df_list)}")
    print(df_list[2]['data'], df_list[2]['label'])
    sns_plot = seaborn.lineplot(data=df_list[0]['data'], x=x_axis, y=y_axis, label=df_list[0]['label'])
    for df in df_list[1:]:
        sns_plot = seaborn.lineplot(data=df['data'], x=x_axis, y=y_axis, label=df['label'])
    sns_plot.set_title(title)
    sns_plot.set_xlabel(x_axis)
    sns_plot.set_ylabel(y_axis)
    sns_plot.legend()
    sns_plot.figure.savefig(f'./graphs/{title}.png')
    plt.clf()


def plot_tp_latency_curve_const_segment(whole_dataframe: pd.DataFrame):
    system_names = ['vanilla_cornflakes', 'cornflakes_copy']

    # Vanilla cornflakes Extraction
    minimized_df_cf = get_tp_latency_item_for_system(whole_dataframe, system_names[0])
    idx = minimized_df_cf.groupby('offered_load_pps')['p99'].idxmax()
    max_idx_cf = minimized_df_cf.loc[idx]

    # Cornflakes Copy Extraction
    minimized_df_copy = get_tp_latency_item_for_system(whole_dataframe, system_names[1])
    idx = minimized_df_copy.groupby('offered_load_pps')['p99'].idxmax()
    max_idx_copy = minimized_df_copy.loc[idx]

    segment_sizes = get_segment_sizes_for_system(whole_dataframe, 'zcc_cornflakes_mfu')

    for segment_size in segment_sizes:
        pinning_limits = get_pinning_limits(whole_dataframe, 'zcc_cornflakes_mfu', segment_size)
        plot_lines = [
            {
                'data': max_idx_cf,
                'label': 'vanilla_cornflakes'
            },

            {
                'data': max_idx_copy,
                'label': 'cornflakes_copy'

            },
        ]

        print(f" Length of pinning limits is: {len(pinning_limits)}")
        for pin_limit in pinning_limits:
            plot_lines.append({
                'data': get_tp_latency_item_for_segment_pinning_limit(whole_dataframe, 'zcc_cornflakes_mfu',
                                                                      segment_size, pin_limit),
                'label': f'zcc_cornflakes_mfu_{segment_size}_{pin_limit}'
            })
            # print(plot_lines[-1]['data'], plot_lines[-1]['label'])
        multiple_line_plot(plot_lines, 'achieved_load_pps', 'p99',
                           f'p99 vs achieved_load_pps_ss{segment_size}_1m20phs')
        del plot_lines
    # two_line_plot(max_idx_cf, max_idx_copy, 'offered_load_pps', 'p99', 'p99 vs offered_load_pps')


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


if __name__ == '__main__':
    DATASET_FILE_1M20PHS = "./dataset/1m20phs.csv"
    DATASET_FILE_8M20PHS = "./dataset/8m20phs_100g.csv"
    dataset_dataframe = read_pandas_dataset(DATASET_FILE_1M20PHS)
    plot_tp_latency_curve(dataset_dataframe)
