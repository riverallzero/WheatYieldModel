import pandas as pd
import os

# 개화기 이후 05.10, 05.30에 생육조사한 생육데이터(Dryweight, Freshweight, Watercontent, LAI, SPAD yield)


def pick_dry_value():
    file = '../output/unbong/U_seed_DryWeight_bloom.csv'

    df_b = pd.read_csv(file)
    df_b = df_b[df_b['item'] == '건물중(면적당)']

    df_b = df_b[df_b['date'] == '2020-04-28']

    dry_file_list = ['../output/unbong/U_seed_DryWeight_0510.csv',
                 '../output/unbong/U_seed_DryWeight_0531.csv']

    dry_item_list = []
    dry_item_list.append(df_b)
    for file in dry_file_list:
        df = pd.read_csv(file)
        dry_item_list.append(df[df['item'] == '건물중(면적당)'])

    index_num = [i for i in range(60)]
    dry_item_list[0].index = index_num
    dry_item_list[1].index = index_num
    dry_item_list[2].index = index_num

    dry_list1 = []
    for d in range(len(dry_item_list[0])):
        dry_list1.append(dry_item_list[0]['value'][d])
    dry_list2 = []
    for d in range(len(dry_item_list[1])):
        dry_list2.append(dry_item_list[1]['value'][d])
    dry_list3 = []
    for d in range(len(dry_item_list[2])):
        dry_list3.append(dry_item_list[2]['value'][d])

    dataset = []
    for y in range(len(dry_list1)):
        dataset.append({'dryweight_1': dry_list1[y],
                        'dryweight_2': dry_list2[y],
                        'dryweight_3': dry_list3[y],
                        })

    return pd.DataFrame(dataset)


def pick_fresh_value():
    file = '../output/unbong/U_seed_FreshWeight_bloom.csv'

    df_b = pd.read_csv(file)
    df_b = df_b[df_b['item'] == '생체중(면적당)']

    df_b = df_b[df_b['date'] == '2020-04-28']

    fresh_file_list = ['../output/unbong/U_seed_FreshWeight_0510.csv',
                 '../output/unbong/U_seed_FreshWeight_0531.csv']

    fresh_item_list = []
    fresh_item_list.append(df_b)
    for file in fresh_file_list:
        df = pd.read_csv(file)
        fresh_item_list.append(df[df['item'] == '생체중(면적당)'])

    index_num = [i for i in range(60)]
    fresh_item_list[0].index = index_num
    fresh_item_list[1].index = index_num
    fresh_item_list[2].index = index_num

    fresh_list1 = []
    for d in range(len(fresh_item_list[0])):
        fresh_list1.append(fresh_item_list[0]['value'][d])
    fresh_list2 = []
    for d in range(len(fresh_item_list[1])):
        fresh_list2.append(fresh_item_list[1]['value'][d])
    fresh_list3 = []
    for d in range(len(fresh_item_list[2])):
        fresh_list3.append(fresh_item_list[2]['value'][d])

    dataset = []
    for y in range(len(fresh_list1)):
        dataset.append({'freshweight_1': fresh_list1[y],
                        'freshweight_2': fresh_list2[y],
                        'freshweight_3': fresh_list3[y],
                        })

    return pd.DataFrame(dataset)


def pick_water_value():
    file = '../output/unbong/U_seed_WaterContent_bloom.csv'

    df_b = pd.read_csv(file)
    df_b = df_b[df_b['item'] == '수분함량(면적당)']

    df_b = df_b[df_b['date'] == '2020-04-28']

    water_file_list = ['../output/unbong/U_seed_WaterContent_0510.csv',
                 '../output/unbong/U_seed_WaterContent_0531.csv']

    water_item_list = []
    water_item_list.append(df_b)
    for file in water_file_list:
        df = pd.read_csv(file)
        water_item_list.append(df[df['item'] == '수분함량(면적당)'])

    index_num = [i for i in range(60)]
    water_item_list[0].index = index_num
    water_item_list[1].index = index_num
    water_item_list[2].index = index_num

    water_list1 = []
    for d in range(len(water_item_list[0])):
        water_list1.append(water_item_list[0]['value'][d])
    water_list2 = []
    for d in range(len(water_item_list[1])):
        water_list2.append(water_item_list[1]['value'][d])
    water_list3 = []
    for d in range(len(water_item_list[2])):
        water_list3.append(water_item_list[2]['value'][d])

    dataset = []
    for y in range(len(water_list1)):
        dataset.append({'watercontent_1': water_list1[y],
                        'watercontent_2': water_list2[y],
                        'watercontent_3': water_list3[y]
                        })

    return pd.DataFrame(dataset)


def pick_lai_value():
    lai_file = '../output/unbong/U_LAI.csv'

    df = pd.read_csv(lai_file)
    df = df[df['item'] == 'LAI']
    df = df[df['date'] != '2020-03-22']
    df = df[df['date'] != '2020-04-12']

    index_num = []
    for i in range(60):
        index_num.append(i)

    lai_1 = df[0:60].copy()
    lai_1.index = index_num
    lai_1['lai_1'] = lai_1['value']
    lai_2 = df[60:120].copy()
    lai_2.index = index_num
    lai_2['lai_2'] = lai_2['value']
    lai_3 = df[120:180].copy()
    lai_3.index = index_num
    lai_3['lai_3'] = lai_3['value']

    return lai_1['lai_1'], lai_2['lai_2'], lai_3['lai_3']


def pick_spad_value():
    spad_file = '../output/unbong/U_SPAD.csv'

    df = pd.read_csv(spad_file)
    df = df[df['date'] != '2020-03-22']
    df = df[df['date'] != '2020-04-12']

    index_num = []
    for i in range(60):
        index_num.append(i)

    spad_1 = df[0:60].copy()
    spad_1.index = index_num
    spad_1['spad_1'] = spad_1['value']
    spad_2 = df[60:120].copy()
    spad_2.index = index_num
    spad_2['spad_2'] = spad_2['value']
    spad_3 = df[120:180].copy()
    spad_3.index = index_num
    spad_3['spad_3'] = spad_3['value']

    return spad_1['spad_1'], spad_2['spad_2'], spad_3['spad_3']


def pick_yield_value():
    lai_file = '../output/unbong/U_Yield.csv'

    df = pd.read_csv(lai_file)
    df = df[df['item'] == 'Yield']

    ds = df.groupby(['group', 'block'], as_index=False).mean()

    yield_list = []
    for d in range(len(ds)):
        for i in range(5):
            yield_list.append(ds['value'][d])

    dataset = []
    for y in yield_list:
        dataset.append({'yield': y})

    return pd.DataFrame(dataset)


def save_seed():
    output_dir = "../output/cleandata/data"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    dry = pick_dry_value()
    fresh = pick_fresh_value()
    water = pick_water_value()
    lai = pick_lai_value()
    spad = pick_spad_value()
    yield_data = pick_yield_value()

    # 시계열 데이터
    df = pd.DataFrame()

    date_0503 = []
    date_0517 = []
    date_0531 = []
    groups = []

    for i in range(60):
        date_0503.append('2020-05-03')
        date_0517.append('2020-05-17')
        date_0531.append('2020-05-31')

    grouplist = ['A(한발)', 'B(무처리)', 'C(적정)', 'D(과습)']
    for group in grouplist:
        for j in range(15):
            groups.append(group)

    df['date_1'] = date_0503
    df['group'] = groups
    df['seed_dryweight_1'] = dry['dryweight_1']
    df['seed_freshweight_1'] = fresh['freshweight_1']
    df['seed_watercontent_1'] = water['watercontent_1']
    df['lai_1'] = lai[0]
    df['spad_1'] = spad[0]

    df['date_2'] = date_0517
    df['seed_dryweight_2'] = dry['dryweight_2']
    df['seed_freshweight_2'] = fresh['freshweight_2']
    df['seed_watercontent_2'] = water['watercontent_2']
    df['lai_2'] = lai[1]
    df['spad_2'] = spad[1]

    df['date_3'] = date_0531
    df['seed_dryweight_3'] = dry['dryweight_3']
    df['seed_freshweight_3'] = fresh['freshweight_3']
    df['seed_watercontent_3'] = water['watercontent_3']
    df['lai_3'] = lai[2]
    df['spad_3'] = spad[2]


    df['yield'] = yield_data['yield']

    df.to_csv(os.path.join(output_dir, 'seed_time_dataset.csv'), index=False, encoding='utf-8')

    # 시계열 안한 데이터
    dn = pd.DataFrame()

    date = []
    date_list = [date_0503, date_0517, date_0531]
    for li in date_list:
        for i in range(len(li)):
            date.append(li[i])

    dn['date'] = date

    group = []
    for i in range(3):
        for j in groups:
            group.append(j)

    dn['group'] = group

    dry_list = []
    for dry1 in dry['dryweight_1']:
        dry_list.append(dry1)
    for dry2 in dry['dryweight_2']:
        dry_list.append(dry2)
    for dry3 in dry['dryweight_3']:
        dry_list.append(dry3)

    dn['seed_dryweight'] = dry_list

    fresh_list = []
    for fresh1 in fresh['freshweight_1']:
        fresh_list.append(fresh1)
    for fresh2 in fresh['freshweight_2']:
        fresh_list.append(fresh2)
    for fresh3 in fresh['freshweight_3']:
        fresh_list.append(fresh3)

    dn['seed_freshweight'] = fresh_list

    water_list = []
    for water1 in water['watercontent_1']:
        water_list.append(water1)
    for water2 in water['watercontent_2']:
        water_list.append(water2)
    for water3 in water['watercontent_3']:
        water_list.append(water3)

    dn['seed_watercontent'] = water_list

    lai_list = []
    for lai1 in lai[0]:
        lai_list.append(lai1)
    for lai2 in lai[1]:
        lai_list.append(lai2)
    for lai3 in lai[2]:
        lai_list.append(lai3)

    dn['lai'] = lai_list

    spad_list = []
    for spad1 in spad[0]:
        spad_list.append(spad1)
    for spad2 in spad[1]:
        spad_list.append(spad2)
    for spad3 in spad[2]:
        spad_list.append(spad3)

    dn['spad'] = spad_list

    yield_list = []
    for i in range(3):
        for yl in yield_data['yield']:
            yield_list.append(yl)

    dn['yield'] = yield_list

    dn.to_csv(os.path.join(output_dir, 'seed_dataset.csv'), index=False, encoding='utf-8')


def main():
    save_seed()


if __name__ == '__main__':
    main()