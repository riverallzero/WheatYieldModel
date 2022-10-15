import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import os
from matplotlib import font_manager, rc


font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)


def draw_correlation(input_filename, output_filename):
    df = pd.read_csv(input_filename)

    # A(한발)구역 제외
    df = df.iloc[15:]

    index_num = []
    for l in range(len(df)):
        index_num.append(l)
    df.index = index_num

    # 중복 변수 제거
    # exclude_list = ['seed_freshweight_2', 'seed_freshweight_3', 'seed_watercontent_1', 'seed_watercontent_2']

    # 중복 변수 제거
    for name in df.columns:
        if 'dryweight' in name:
            del df[name]

    # df = df.drop(exclude_list, axis=1)

    corr = df.corr()
    fig, ax = plt.subplots(figsize=(30, 15))
    mask = np.triu(np.ones_like(corr, dtype=bool))
    cmap = sns.diverging_palette(230, 20, as_cmap=True)
    sns.heatmap(corr, annot=True, mask=mask, cmap=cmap)
    fig.tight_layout()
    plt.savefig(output_filename)


def main():
    output_dir = "../Output/CA(png)"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    input_filename1 = "../Output/cleandata/time_dataset.csv"
    output_filename1 = os.path.join(output_dir, "data.png")

    draw_correlation(input_filename1, output_filename1)


if __name__ == '__main__':
    main()