import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from xgboost import XGBRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.metrics import mean_absolute_error, r2_score
from matplotlib import font_manager, rc


font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

df = pd.read_csv('../output/cleandata/time_dataset.csv')
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
    elif 'stem' in name:
        del df[name]
    elif 'leaf' in name:
        del df[name]


def main():
    X = df.drop('yield', axis=1).select_dtypes(exclude=['object'])
    X = pd.concat([X, pd.get_dummies(df.group, prefix='WaterCond')], axis=1)

    y = df['yield']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=100 )

    scaler = StandardScaler()
    scaler.fit(X_train)

    X_train_scaled = scaler.transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    var_ratio = []

    for i in range(1, len(df.columns), 1):
        pca = PCA(n_components=i)
        pca.fit_transform(X_train_scaled)
        ratio = pca.explained_variance_ratio_.sum()
        var_ratio.append(ratio)

    sns.lineplot(x=range(1, len(df.columns), 1), y=var_ratio)
    plt.title('주성분 개수에 따른 데이터 반영 비율')
    plt.xlabel('주성분 개수')
    plt.ylabel('데이터 반영 비율')
    plt.show()

    pca = PCA(n_components=10, random_state=42)
    pca.fit(X_train_scaled)
    X_train_scaled_pca = pca.transform(X_train_scaled)
    X_test_scaled_pca = pca.transform(X_test_scaled)

    model = XGBRegressor(
        n_estimators=500,
        max_depth=5,
        eval_metric='mae',
        objective='reg:squarederror',
        learning_rate=0.3,
        min_child_weight=2,
    )
    # model = LinearRegression()
    model.fit(X_train_scaled, y_train)
    pred = model.predict(X_test_scaled)
    mae = mean_absolute_error(pred, y_test)
    r2c = r2_score(pred, y_test)
    print(f'주성분분석 전 MAE = {mae:.3f}')
    print(f'주성분분석 전 R2C = {r2c:.3f}')
    print('------------------------')

    model_pca = XGBRegressor(
        n_estimators=500,
        max_depth=5,
        eval_metric='mae',
        objective='reg:squarederror',
        learning_rate=0.3,
        min_child_weight=2
    )
    # model_pca = LinearRegression()
    model_pca.fit(X_train_scaled_pca, y_train)
    pred_pca = model_pca.predict(X_test_scaled_pca)
    mae_pca = mean_absolute_error(pred_pca, y_test)
    r2c_pca = r2_score(pred_pca, y_test)
    print(f'주성분분석 후 MAE = {mae_pca:.3f}')
    print(f'주성분분석 후 R2C = {r2c_pca:.3f}')

    plt.scatter(pred, y_test)
    plt.scatter(pred_pca, y_test, alpha=0.5)
    if max(pred) >= max(y_test):
        plt.plot([0, max(pred)], [0, max(pred)], 'red')
    else:
        plt.plot([0, max(y_test)], [0, max(y_test)], 'red')

    plt.show()


if __name__ == '__main__':
    main()