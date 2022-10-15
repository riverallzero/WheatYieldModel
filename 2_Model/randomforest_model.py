from sklearn.ensemble import RandomForestRegressor
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
import os


def main():
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
        elif 'stem' in name:
            del df[name]
        elif 'leaf' in name:
            del df[name]

    y = df['yield']

    X = df.drop(['yield'], axis=1).select_dtypes(exclude=['object'])

    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.6, random_state=42)

    model = RandomForestRegressor()
    model.fit(X_train, y_train)

    y_predict = model.predict(X_test)

    mae = mean_absolute_error(y_predict, y_test)
    r2c = r2_score(y_predict, y_test)

    plt.scatter(y_predict, y_test)

    if max(y_predict) >= max(y_test):
        plt.plot([0, max(y_predict)], [0, max(y_predict)], 'red')
    else:
        plt.plot([0, max(y_test)], [0, max(y_test)], 'red')

    plt.title(f'Randomforest_Prediction(MAE {mae:.2f})')
    plt.xlabel('Predict Value')
    plt.ylabel('Real Value')

    output_dir = "../output/result"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    plt.savefig(os.path.join(output_dir, 'randomforest_result.png'))

    plt.show()

    print('MAE: {:.2f}'.format(mae))
    print('R2C: {:.2f}'.format(r2c))

    output_dir = "../output/cleandata/data"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # import shap
    # explainer = shap.TreeExplainer(model)  # Tree model Shap Value 확인 객체 지정
    # shap_values = explainer.shap_values(X_test)  # Shap Values 계산
    # shap.summary_plot(shap_values, X_test)
    feature_importance = pd.DataFrame(model.feature_importances_.reshape((1, -1)), columns=X_train.columns,
                                      index=['feature_importance'])
    feature_importance = feature_importance.transpose()
    print(feature_importance.sort_values('feature_importance', ascending=False))


if __name__ == '__main__':
    main()