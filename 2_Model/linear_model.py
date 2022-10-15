import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, r2_score
import math
import numpy as np
import os


def main():
    output_dir = "../output/result"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    df = pd.read_csv("../output/cleandata/time_dataset.csv")

    # A(한발)구역 제외
    df = df.iloc[15:]

    index_num = []
    for l in range(len(df)):
        index_num.append(l)
    df.index = index_num

    # 중복 변수 제거
    for name in df.columns:
        if 'dryweight' in name:
            del df[name]
        elif 'width' in name:
            del df[name]
        elif '_3' in name:
            del df[name]
        elif 'spad' in name:
            del df[name]

    y = df['yield']

    X = df.drop(['yield'], axis=1).select_dtypes(exclude=['object'])

    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.6, random_state=42)
    mlr = LinearRegression()
    mlr.fit(X_train, y_train)
    y_predict = mlr.predict(X_test)

    mae = mean_absolute_error(y_predict, y_test)
    r2c = r2_score(y_predict, y_test)

    size = 18

    params = {'legend.fontsize': size,
              'axes.labelsize': size * 1.2,
              'axes.titlesize': size * 1.2,
              'xtick.labelsize': size,
              'ytick.labelsize': size,
              }

    plt.rcParams.update(params)
    fig, ax = plt.subplots(figsize=(7.5, 6))

    ax.scatter(y_predict, y_test, alpha=0.6, color="coral")

    if max(y_predict) >= max(y_test):
        ax.plot([0, max(y_predict)], [0, max(y_predict)], 'darkviolet')
    else:
        ax.plot([0, max(y_test)], [0, max(y_test)], 'darkviolet')

    ax.set_title('Linear Regression')
    ax.set_xlabel('Predict Value')
    ax.set_ylabel('Real Value')
    fig.tight_layout()
    fig.savefig(os.path.join(output_dir, "LinearRegression.png"), dpi=600)


    print('MAE: {:.2f}'.format(mae))
    print('R2C: {:.2f}'.format(r2c))

    print(f'절편 : {mlr.intercept_:.2f}')

    new_name = ['생체중_1', '수분함량_1', '잎길이_1', 'LAI_1',
       '생체중_2', '수분함량_2', '잎길이_2', 'LAI_2']

    dataset = []
    for name, val in zip(X.columns, mlr.coef_):
        std = math.sqrt(np.var(X[name]))
        if name == 'seed_freshweight_1':
            n = new_name[0]
        elif name == 'seed_watercontent_1':
            n = new_name[1]
        elif name == 'length_1':
            n = new_name[2]
        elif name == 'lai_1':
            n = new_name[3]
        elif name == 'seed_freshweight_2':
            n = new_name[4]
        elif name == 'seed_watercontent_2':
            n = new_name[5]
        elif name == 'length_2':
            n = new_name[6]
        else:
            n = new_name[7]
        dataset.append({
            'item': n,
            'coef*std': val * std
        })
    df_data = pd.DataFrame(dataset)
    df_data.to_csv(os.path.join(output_dir, 'linear_importance.csv'), index=False, encoding='utf-8-sig')


if __name__ == '__main__':
    main()
