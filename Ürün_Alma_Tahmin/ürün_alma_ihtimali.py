import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

@st.cache_data
def load_data():
    data=pd.read_csv("ecommerce.csv")
    return data

data = load_data()

X=data.drop("Satin_aldi",axis=1)
y=data["Satin_aldi"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

def predict_purchase(model, age, salary):
    input_data = [[age, salary]]
    prediction = model.predict(input_data)
    return prediction[0]

st.title("Ürün Satın Alma Olasılığı Tahmini")

age = st.slider("Yaş", min_value=18, max_value=70, step=1)
salary = st.slider("Maaş (bin TL)", min_value=20, max_value=200, step=5)

if st.button("Tahmin Et"):
    prediction = predict_purchase(model, age, salary)
    if prediction == 1:
        st.success("Ürün Satın Alma Olasılığı: Yüksek")
    else:
        st.success("Ürün Satın Alma Olasılığı: Düşük")