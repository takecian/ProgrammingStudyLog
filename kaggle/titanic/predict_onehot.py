#

import numpy as np
import pandas as pd
from xgboost import XGBClassifier
from sklearn.preprocessing import OneHotEncoder


def main():
    # 学習データ、テストデータの読み込み
    train = pd.read_csv('train.csv')
    test = pd.read_csv('test.csv')

    # 学習データを特徴量と目的変数に分ける
    train_x = train.drop(['Survived'], axis=1)
    train_y = train['Survived']

    # テストデータは特徴量のみなので、そのままでよい
    test_x = test.copy()

    # 変数PassengerIdを除外する
    train_x = train_x.drop(['PassengerId'], axis=1)
    test_x = test_x.drop(['PassengerId'], axis=1)

    # 変数Name, Ticket, Cabinを除外する
    train_x = train_x.drop(['Name', 'Ticket', 'Cabin'], axis=1)
    test_x = test_x.drop(['Name', 'Ticket', 'Cabin'], axis=1)

    for c in ['Sex', 'Embarked']:
        all_x = pd.concat([train_x, test_x])
        all_x = pd.get_dummies(all_x, columns=[c])

        train_x = all_x.iloc[:train_x.shape[0], :].reset_index(drop=True)
        test_x = all_x.iloc[train_x.shape[0]:, :].reset_index(drop=True)

    # モデルの作成および学習データを与えての学習
    model = XGBClassifier(n_estimators=20, random_state=71, max_depth=7, min_child_weight=2)
    model.fit(train_x, train_y)

    # テストデータの予測値を確率で出力する
    pred = model.predict_proba(test_x)

    print('pred1')
    print(pred)

    pred = pred[:, 1]
    print('pred2')
    print(pred)

    # テストデータの予測値を二値に変換する
    pred_label = np.where(pred > 0.5, 1, 0)
    # print('pred_label')
    # print(pred_label)

    # 提出用ファイルの作成
    submission = pd.DataFrame({'PassengerId': test['PassengerId'], 'Survived': pred_label})
    submission.to_csv('submission_onehot.csv', index=False)

if __name__ == '__main__':
    main()