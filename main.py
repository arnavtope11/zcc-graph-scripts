import glob

import polars as pl


# Read a csv file
def reading_polardata(file_name):
    df = pl.read_csv(file_name)
    return df


def single_latency_files(file_list, op_filename):
    dataset_ = []
    for _ in file_list:
        dataset_.append(reading_polardata(_))
    new_dataset = pl.concat(dataset_)
    print(new_dataset.head(), new_dataset.tail())
    new_dataset.write_csv(op_filename)


def get_files(folder):
    return glob.glob(f"{folder}/*.log")


if __name__ == '__main__':
    files_list = get_files('./dataset/8m20phs_d6515/')
    single_latency_files(files_list, './dataset/8m20phs_d6515.csv')
