import matplotlib.pyplot as plt
import pandas as pd
import os


def main():
    size = 18

    params = {'legend.fontsize': size,
              'axes.labelsize': size * 1.2,
              'axes.titlesize': size * 1.2,
              'xtick.labelsize': size,
              'ytick.labelsize': size,
              }

    plt.rcParams.update(params)
    fig, ax = plt.subplots(figsize=(6, 6))

    # XGBoost feature importance
    xgb_fi = pd.read_csv('../output/result/xgb_importance.csv')
    xgb_fi = xgb_fi.sort_values(by='feature_importance', ascending=True)
    xgb_fi = xgb_fi.iloc[-6:-1]
    # Linear Regression coef_ * std
    linear_fi = pd.read_csv('../output/result/linear_importance.csv')

    linear_fi = linear_fi.sort_values(by='coef*std', ascending=True)
    linear_fi = linear_fi.reset_index()
    linear_fi = linear_fi[3:]

    output_dir = "../output/result"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    plt.figure(figsize=(8, 6))
    xgb_fi.plot.barh(x='item', y='feature_importance', rot=0, label='feature importance', color="cadetblue", alpha=0.4)
    plt.tight_layout()
    plt.xlabel("")
    plt.ylabel("")
    plt.savefig(os.path.join(output_dir, 'xgb_importance.png'))
    plt.show()

    plt.figure(figsize=(8, 6))
    linear_fi.plot.barh(x='item', y='coef*std', rot=0, label='coef * std', color="coral", alpha=0.4)
    plt.tight_layout()
    plt.xlabel("")
    plt.ylabel("")
    plt.savefig(os.path.join(output_dir, 'linear_importance.png'))
    plt.show()


if __name__ == '__main__':
    main()