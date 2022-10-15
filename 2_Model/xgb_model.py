import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
import matplotlib.pyplot as plt
from sklearn.metrics import make_scorer, mean_absolute_error
from sklearn.metrics import r2_score
from matplotlib import font_manager, rc
import os

font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)


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

    y = df['yield']

    X = df.drop(['yield'], axis=1).select_dtypes(exclude=['object'])

    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.6, random_state=42)


    model = XGBRegressor()

    model.fit(X_train, y_train)

    y_predict = model.predict(X_test)

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

    ax.scatter(y_predict, y_test, alpha=0.6, color="cadetblue")

    if max(y_predict) >= max(y_test):
        ax.plot([0, max(y_predict)], [0, max(y_predict)], 'darkviolet')
    else:
        ax.plot([0, max(y_test)], [0, max(y_test)], 'darkviolet')

    ax.set_title('XGBoost')
    ax.set_xlabel('Predict Value')
    ax.set_ylabel('Real Value')
    fig.tight_layout()
    fig.savefig(os.path.join(output_dir, "XGBoost.png"), dpi=600)

    print('MAE: {:.2f}'.format(mae))
    print('R2C: {:.2f}'.format(r2c))

    # import shap
    #
    # plt.figure(figsize=(6, 8))
    # explainer = shap.TreeExplainer(model)  # Tree model Shap Value 확인 객체 지정
    # shap_values = explainer.shap_values(X_test)  # Shap Values 계산
    # shap.summary_plot(shap_values, X_test)
    # plt.show()

    # bar chart
    # sorted_idx = model.feature_importances_.argsort()
    # plt.figure(figsize=(15, 6))
    # plt.barh(X.columns[sorted_idx], model.feature_importances_[sorted_idx])
    # plt.xlabel("Xgboost Feature Importance")
    # plt.show()

    # save to csv
    feature_importance = pd.DataFrame(model.feature_importances_.reshape((1, -1)), columns=X_train.columns, index=['feature_importance'])
    feature_importance = feature_importance.transpose()
    namelist = ['SPAD_3', '잎너비_3', '잎너비_1', 'LAI_1', 'LAI_2', 'SPAD_1', 'SPAD_2',
                '수분함량_2', '잎길이_1', 'seed_watercontent_1', 'seed_freshweight_2',
                '생체중_1', 'seed_watercontent_3', 'lai_3', 'width_2', 'length_2', 'length_3', 'seed_freshweight_3']
    df = feature_importance.sort_values('feature_importance', ascending=False)
    df.insert(0, 'item', namelist)
    df.to_csv(os.path.join(output_dir, 'xgb_importance.csv'), index=False, encoding='utf-8-sig')


if __name__ == '__main__':
    main()
