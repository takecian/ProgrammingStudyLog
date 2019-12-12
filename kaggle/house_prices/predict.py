#

import numpy as np
import pandas as pd
from xgboost import XGBClassifier
from sklearn.preprocessing import LabelEncoder

def main():
    target_key = 'SalePrice'
    # 学習データ、テストデータの読み込み
    train = pd.read_csv('train.csv')
    test = pd.read_csv('test.csv')

    # 学習データを特徴量と目的変数に分ける
    train_x = train.drop([target_key], axis=1)
    train_y = train[target_key]

    # テストデータは特徴量のみなので、そのままでよい
    test_x = test.copy()

    necessary_keys = ['1stFlrSF', '2ndFlrSF', 'YearBuilt', 'MSSubClass', 'GarageCars', 'YrSold']

    labelled_keys = ['MSZoning', 'Street', 'LotShape', 'LandContour', 'Condition1', 'Condition2', 'BldgType', 'HouseStyle', 'RoofStyle','Foundation','BsmtQual','BsmtCond','BsmtExposure','BsmtFinType1','Heating','HeatingQC','CentralAir','Electrical','KitchenQual','Functional','GarageType', 'GarageFinish','GarageQual','Fence','SaleType','SaleCondition']
    # 不要カラムの削除
    unnecessary_keys = ['Id', 'Alley', 'Utilities', 'LotConfig', 'LandSlope', 'Neighborhood', 'RoofMatl','Exterior1st','Exterior2nd','MasVnrType', 'ExterQual', 'ExterCond','BsmtFinType2','BsmtFinSF2','1stFlrSF','2ndFlrSF','FireplaceQu','GarageCond','PavedDrive','PoolQC','MiscFeature']
    train_x = train_x[necessary_keys + labelled_keys]
    test_x = test_x[necessary_keys + labelled_keys]

    concat_x = pd.concat([train_x, test_x], axis=0)
    for col in necessary_keys:
        train_x[col].fillna(concat_x[col].mean(), inplace=True)
        test_x[col].fillna(concat_x[col].mean(), inplace=True)

    # カテゴリ変数の処理
    # それぞれのカテゴリ変数にlabel encodingを適用する

    for c in labelled_keys:
        # 学習データに基づいてどう変換するかを定める
        print(c)

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