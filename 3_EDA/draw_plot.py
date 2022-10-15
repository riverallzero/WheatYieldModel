import os
import platform
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

if platform.system() == "Darwin":
    plt.rc('font', family='AppleGothic')
elif platform.system() == "Windows":
    font_path = "C:/Windows/Fonts/NGULIM.TTF"
    font = font_manager.FontProperties(fname=font_path).get_name()
    rc('font', family=font)


def drawing(filename):

    df = pd.read_csv(filename)

    df_week_1 = df[df['date'] == '2020-05-03']

    index_num = []
    for i in range(len(df_week_1)):
        index_num.append(i)

    df_week_2 = df[df['date'] == '2020-05-17']
    df_week_2.index = index_num

    df_week_3 = df[df['date'] == '2020-05-31']
    df_week_3.index = index_num

    items = ['watercontent', 'freshweight', 'length', 'width', 'lai', 'spad']

    output_dir = "../Output/figures"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    size = 20

    params = {'legend.fontsize': size,
              'axes.labelsize': size * 1.8,
              'axes.titlesize': size * 1.6,
              'xtick.labelsize': size * 0.8,
              'ytick.labelsize': size * 0.8,
              }

    plt.rcParams.update(params)

    for item in items:
        fig, ax = plt.subplots(ncols=3, figsize=(15, 6), sharex=True, sharey=True)
        x1 = df_week_1['group']
        y1 = df_week_1[item]
        x2 = df_week_2['group']
        y2 = df_week_2[item]
        x3 = df_week_3['group']
        y3 = df_week_3[item]

        g1 = sns.stripplot(x=x1, y=y1, ax=ax[0])
        g2 = sns.stripplot(x=x2, y=y2,  ax=ax[1])
        g3 = sns.stripplot(x=x3, y=y3,  ax=ax[2])

        g1.set_xlabel("")
        if "lai" in item:
            g1.set_ylabel("LAI")
        elif "spad" in item:
            g1.set_ylabel("SPAD")
        g2.set_xlabel("")
        g2.set_ylabel("")
        g3.set_xlabel("")
        g3.set_ylabel("")

        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, f'{item}.png'))


def main():
    drawing('../output/cleandata/dataset.csv')


if __name__ == "__main__":
    main()
