import pandas as pd
import os


def pick_width_value():
    width_file = '../output/unbong/U_LAI.csv'

    df = pd.read_csv(width_file)
    df = df[df['item'] == 'width']
    df = df[df['date'] != '2020-03-22']
    df = df[df['date'] != '2020-04-12']
    # df = df[df['date'] != '2020-05-01']

    index_num = []
    for i in range(60):
        index_num.append(i)

    width_1 = df[0:60].copy()
    width_1.index = index_num
    width_1['width_1'] = width_1['value']
    width_2 = df[60:120].copy()
    width_2.index = index_num
    width_2['width_2'] = width_2['value']
    width_3 = df[120:180].copy()
    width_3.index = index_num
    width_3['width_3'] = width_3['value']


    return width_1['width_1'], width_2['width_2'], width_3['width_3']


def pick_length_value():
    length_file = '../output/unbong/U_LAI.csv'

    df = pd.read_csv(length_file)
    df = df[df['item'] == 'length']
    df = df[df['date'] != '2020-03-22']
    df = df[df['date'] != '2020-04-12']
    # df = df[df['date'] != '2020-05-01']

    index_num = []
    for i in range(60):
        index_num.append(i)

    length_1 = df[0:60].copy()
    length_1.index = index_num
    length_1['length_1'] = length_1['value']
    length_2 = df[60:120].copy()
    length_2.index = index_num
    length_2['length_2'] = length_2['value']
    length_3 = df[120:180].copy()
    length_3.index = index_num
    length_3['length_3'] = length_3['value']

    return length_1['length_1'], length_2['length_2'], length_3['length_3']


def merge_data_time():
    # da = pd.read_csv('../output/cleandata/data/leaf_time_dataset.csv')
    db = pd.read_csv('../output/cleandata/data/seed_time_dataset.csv')
    # dc = pd.read_csv('../output/cleandata/data/stem_time_dataset.csv')

    lengths = pick_length_value()
    widths = pick_width_value()

    # da.insert(2, 'seed_dryweight_1', db['seed_dryweight_1'])
    # da.insert(2, 'stem_dryweight_1', dc['stem_dryweight_1'])

    # da.insert(5, 'seed_freshweight_1', db['seed_freshweight_1'])
    # da.insert(5, 'stem_freshweight_1', dc['stem_freshweight_1'])

    # da.insert(8, 'seed_watercontent_1', db['seed_watercontent_1'])
    # da.insert(8, 'stem_watercontent_1', dc['stem_watercontent_1'])
    db.insert(5, 'length_1', lengths[0])
    db.insert(6, 'width_1', widths[0])

    db.insert(13, 'length_2', lengths[1])
    db.insert(14, 'width_2', widths[1])

    db.insert(21, 'length_3', lengths[2])
    db.insert(22, 'width_3', widths[2])
    return db

    # da.insert(16, 'seed_dryweight_2', db['seed_dryweight_2'])
    # da.insert(16, 'stem_dryweight_2', dc['stem_dryweight_2'])

    # da.insert(19, 'seed_freshweight_2', db['seed_freshweight_2'])
    # da.insert(19, 'stem_freshweight_2', dc['stem_freshweight_2'])

    # da.insert(22, 'seed_watercontent_2', db['seed_watercontent_2'])
    # da.insert(22, 'stem_watercontent_2', dc['stem_watercontent_2'])

    # db.insert(27, 'length_2', lengths[1])
    # dbinsert(27, 'width_2', widths[1])
    #
    # return da


def save_data_to_time():
    output_dir = "../output/cleandata"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    data = merge_data_time()
    data.to_csv(os.path.join(output_dir, 'time_dataset.csv'), index=False, encoding='utf-8')


def main():
    save_data_to_time()


if __name__ == '__main__':
    main()