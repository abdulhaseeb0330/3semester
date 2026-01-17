import pandas as pd
import matplotlib as plt
import numpy as np
from sklearn.model_selection import train_test_split

data=pd.read_csv("D:\\python projects\old\Border_Crossing_Entry_Data.csv")
# newdata=pd.dropna(data)
# print(data.to_string())

# dic={"name":["ali","ahmed","sara","jack","jhon","asdf","sd","qwe","zxcv","rtyu","ghjkl"],
#      "age":[23,45,34,23,45,67,89,12,34,56,78],
#      "city":["cairo","alex","giza","aswan","luxor","so","hag","minya","qena","fayoum","ismailia"]}
# df=pd.DataFrame(dic)
# print(df)  
# print("=----=")
# sf=pd.Series(df["age"])
# print(sf,end=None)
# print("=----=")
# print(sf.describe())

# print(data.head())
# print(data.tail())
# print(data[:1])
# print(data.info())

newdata=data.dropna()
print(newdata.to_string())

data["Date"] = pd.to_datetime(data["Date"])
data = data.dropna(subset=["Value"])
data["year"]=data["Date"].dt.year
data["month"]=data["Date"].dt.month
data["day"]=data["Date"].dt.day
data = pd.get_dummies(
    data,
    columns=["Port Name", "State", "Border", "Measure"],
    drop_first=True
)
X = data.drop(columns=["Value", "Date", "Point"])
y = data["Value"]



X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, shuffle=False
)




