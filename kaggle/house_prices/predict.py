#

import numpy as np
import pandas as pd
from xgboost import XGBClassifier
from sklearn.preprocessing import LabelEncoder
import missingno as msno
import seaborn as sns

def main():
    target_key = 'SalePrice'
    # 学習データ、テストデータの読み込み
    train = pd.read_csv('train.csv')
    test = pd.read_csv('test.csv')

    print(train.dtypes)

    # msno.matrix(df=train, figsize=(20, 14), color=(0.5, 0, 0))
    sns.heatmap(train.isnull(), cbar=False)
    return
    # 学習データを特徴量と目的変数に分ける
    train_x = train.drop([target_key], axis=1)
    train_y = train[target_key]

    # テストデータは特徴量のみなので、そのままでよい
    test_x = test.copy()

    necessary_number_keys = ['LotFrontage', 'LotArea', 'OverallQual', 'OverallCond', 'YearBuilt', 'YearRemodAdd', 'MasVnrArea', 'BsmtFinSF1', 'BsmtFinSF2',
                             'BsmtUnfSF', 'TotalBsmtSF', '1stFlrSF', '2ndFlrSF', 'GrLivArea', 'GarageCars', 'GarageArea']
    necessary_num_zero_keys = ['GarageYrBlt', 'WoodDeckSF']

    category_keys = ['MSZoning', 'Street', 'Alley', 'LotShape', 'LandContour', 'Utilities', 'LotConfig', 'LandSlope', 'Neighborhood',
                     'Condition1', 'Condition2', 'BldgType', 'HouseStyle', 'RoofStyle','Foundation','BsmtQual','BsmtCond',
                     'BsmtExposure','BsmtFinType1','Heating','HeatingQC','CentralAir','Electrical','KitchenQual','Functional',
                     'GarageType', 'GarageFinish','GarageQual','Fence','SaleType','SaleCondition']
    # 不要カラムの削除
    train_x = train_x[necessary_number_keys + necessary_num_zero_keys + category_keys]
    test_x = test_x[necessary_number_keys + necessary_num_zero_keys + category_keys]

    concat_x = pd.concat([train_x, test_x], axis=0)
    for col in necessary_number_keys:
        train_x[col].fillna(concat_x[col].mean(), inplace=True)
        test_x[col].fillna(concat_x[col].mean(), inplace=True)

    for col in necessary_num_zero_keys:
        train_x[col].fillna(0, inplace=True)
        test_x[col].fillna(0, inplace=True)
    # カテゴリ変数の処理
    # それぞれのカテゴリ変数にlabel encodingを適用する

    for c in category_keys:
        # 学習データに基づいてどう変換するかを定める
        # print(c)

        le = LabelEncoder()
        le.fit(concat_x[c].fillna('NA'))

        # 学習データ、テストデータを変換する
        train_x[c] = le.transform(train_x[c].fillna('NA'))
        test_x[c] = le.transform(test_x[c].fillna('NA'))

    # モデルの作成および学習データを与えての学習
    from sklearn import linear_model
    model = linear_model.LinearRegression()
    model.fit(train_x, train_y)

    # テストデータの予測値を出力する
    pred = model.predict(test_x)
    # print('pred')
    # print(pred)

    # 提出用ファイルの作成
    submission = pd.DataFrame({'Id': test['Id'], 'SalePrice': pred})
    submission.to_csv('submission_first.csv', index=False)
    print('Done.')

if __name__ == '__main__':
    main()