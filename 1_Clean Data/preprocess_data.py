import pandas as pd
import os


def save_data():
    output_dir = "../output/cleandata"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    df = pd.read_csv("../output/cleandata/time_dataset.csv")
    df_f = pd.DataFrame()
    df_dates = pd.concat([df["date_1"], df["date_2"], df["date_3"]], ignore_index=True)
    groups = []
    for i in range(3):
        for group in df["group"]:
            groups.append(group)
    df_fresh = pd.concat([df["seed_freshweight_1"], df["seed_freshweight_2"], df["seed_freshweight_3"]], ignore_index=True)
    df_dry = pd.concat([df["seed_dryweight_1"], df["seed_dryweight_2"], df["seed_dryweight_3"]], ignore_index=True)
    df_water = pd.concat([df["seed_watercontent_1"], df["seed_watercontent_2"], df["seed_watercontent_3"]], ignore_index=True)
    df_length = pd.concat([df["length_1"], df["length_2"], df["length_3"]], ignore_index=True)
    df_width = pd.concat([df["width_1"], df["width_2"], df["width_3"]], ignore_index=True)
    df_lai = pd.concat([df["lai_1"], df["lai_2"], df["lai_3"]], ignore_index=True)
    df_spad = pd.concat([df["spad_1"], df["spad_2"], df["spad_3"]], ignore_index=True)

    df_f["date"] = df_dates
    df_f["group"] = groups
    df_f["freshweight"] = df_fresh
    df_f["dryweight"] = df_dry
    df_f["watercontent"] = df_water
    df_f["length"] = df_length
    df_f["width"] = df_width
    df_f["lai"] = df_lai
    df_f["spad"] = df_spad

    yields = []
    for i in range(3):
        for yid in df["yield"]:
            yields.append(yid)
    df_f["yield"] = yields

    df_f.to_csv(os.path.join(output_dir, "dataset.csv"), index=False, encoding="utf-8-sig")


def main():
    save_data()


if __name__ == '__main__':
    main()