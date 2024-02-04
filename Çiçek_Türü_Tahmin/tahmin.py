import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from PIL import Image

icon = Image.open("cicek.png")
st.set_page_config(
    page_title="Çicek Türü Tahmini",
    page_icon=icon,
    layout="centered",
    initial_sidebar_state="auto",
)


@st.cache_data
def load_data():
    data = pd.read_csv("Iris.csv") 
    return data

data = load_data()


X = data.drop("species", axis=1)
y = data["species"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = RandomForestClassifier()
model.fit(X_train, y_train)


def predict_species(model, sepal_length, sepal_width, petal_length, petal_width):
    input_data = [[sepal_length, sepal_width, petal_length, petal_width]]
    prediction = model.predict(input_data)
    return prediction[0]


st.title("Iris Çiçeği Türü Tahmini")


sepal_length = st.slider("Sepal Length", min_value=4.0, max_value=8.0, step=0.1)
sepal_width = st.slider("Sepal Width", min_value=2.0, max_value=4.5, step=0.1)
petal_length = st.slider("Petal Length", min_value=1.0, max_value=7.0, step=0.1)
petal_width = st.slider("Petal Width", min_value=0.1, max_value=2.5, step=0.1)


if st.button("Tahmin Et"):
    prediction = predict_species(model, sepal_length, sepal_width, petal_length, petal_width)
    st.success(f"Tahmin Edilen Tür: {prediction}")
