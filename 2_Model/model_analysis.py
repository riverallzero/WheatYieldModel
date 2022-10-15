import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import os


def main():
    df = pd.read_csv("../output/cleandata/time_dataset.csv")

    # A(한발)구역 제외
    df = df.iloc[15:]

    index_num = []
    for l in range(len(df)):
        index_num.append(l)
    df.index = index_num

    for name in df.columns:
        if 'dryweight' in name:
            del df[name]

    y = df['yield']

    X = df.drop(['yield'], axis=1).select_dtypes(exclude=['object'])

    train_X, test_X, train_y, test_y = train_test_split(X, y, train_size=0.6, random_state=42)

    xgb = XGBRegressor()
    xgb.fit(train_X, train_y)
    pred_xgb = xgb.predict(test_X)

    df = pd.read_csv("../output/cleandata/time_dataset.csv")

    # A(한발)구역 제외
    df = df.iloc[15:]

    index_num = []
    for l in range(len(df)):
        index_num.append(l)
    df.index = index_num

    # 중복 변수 제거
    for name in df.columns:
        if 'freshweight' in name:
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
    pred_mlr = mlr.predict(X_test)

    output_dir = "../output/result"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)


    # 실제, 예측 그래프
    lengths = []
    for l in range(len(y_test)):
        lengths.append(l)
    plt.figure(figsize=(10, 4))
    plt.plot(lengths, y_test, label="Real", color="darkviolet", linewidth=3)
    plt.plot(lengths, pred_xgb, label="XGBoost", color="cadetblue", linewidth=3, linestyle="--")
    plt.plot(lengths, pred_mlr, label="Linear", color="coral", linewidth=3, linestyle="-.")

    plt.title("Model Result")
    plt.ylabel("Yield")
    plt.legend()
    plt.savefig(os.path.join(output_dir, 'result.png'))
    plt.show()


if __name__ == "__main__":
    main()