import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import json
# from sklearn.model_selection import train_test_split
# from pandas.plotting import scatter_matrix
# from sklearn.preprocessing import Imputer
# from sklearn.preprocessing import LabelEncoder
# from sklearn.preprocessing import OneHotEncoder
# from sklearn.pipeline import Pipeline
# from sklearn.preprocessing import StandardScaler
# from sklearn.metrics import precision_score, recall_score, accuracy_score
# from sklearn.metrics import roc_curve
# from sklearn.model_selection import cross_val_predict




def ml():
    # read in data
    # columns_names = [Cocoa (minimum), &nbsp;  Soluble fiber, Vitamin B12 (cobalamin), Alcohol, Energy from fat, Sodium, file_name, Cholesterol, Selenium, Caffeine, Vitamin B1 (Thiamin), Taurine, &nbsp;  Insoluble fiber, Omega3 EPA (Eicosapentaenoic Acid), Trans fat, Omega3 DHA (Docosahexaenoic Acid), Erythritol, Omega3 Other, Polyunsaturated fat, Vitamin E, Vitamin B9 (Folic acid), FIBRA DI\xc9TETICA, Potassium, Fat, Sugar alcohols (Polyols), Biotin, NutriScore, nutrition_label_src, Vitamin B2 (Riboflavin), Fruits, vegetables and nuts (minimum), &nbsp;  Lactose, Phosphorus, Pantothenic acid / Pantothenate (Vitamin B5), Vitamin B6 (Pyridoxin), Omega 6 fatty acids, Molybdenum, Folates (total folates), sno, added sugars, Dietary fiber, Proteins, Manganese, Calcium, Vitamin A, Magnesium, Iron, Monounsaturated fat, Vitamin K, Carbon footprint / CO2 emissions, Salt, Vitamin D, Nutrition score  France, Copper, Iodine, Vitamin B3 / Vitamin PP (Niacin), Omega 3 fatty acids, url, Fruits, vegetables and nuts (estimate from ingredients list), Energy, Sugars, Guarana Seed Extract, Carbohydrate, Saturated fat, Zinc, FIBRA DIET\xc9TICA, &nbsp;  Oleic acid (18:1 n-9), Vitamin C (ascorbic acid), Chromium, Ecological footprint]
    label_info = pd.DataFrame(columns=["Calcium", "Carbohydrate", "Cholesterol", "Dietary fiber", "Energy",
        "Energy from fat", "Fat", "Iron", "NutriScore", "Nutrition score  France", "Potassium", "Proteins",
        "Salt", "Saturated fat", "Sodium", "Sugars", "Trans fat", "Vitamin A", "Vitamin C (ascorbic acid)",
        "Vitamin D", "file_name", "nutrition_label_src", "sno", "url"])
    with open('data.json') as f:
        data = json.load(f)
    i = 0
    for title in data:
        label_info.loc[i] = pd.Series(data[title])
    print('----------------------- Original Data + Info -----------------------')
    print(label_info.head())

    # data info
    print(label_info.info())
    print(label_info.describe())
    print('----------------------- Columns -----------------------')
    print(list(label_info))
    # data clean

    # data split

    # training

    # testing

    # output



if __name__ == '__main__':
    ml()
